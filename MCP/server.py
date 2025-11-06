from fastmcp import FastMCP
import httpx
import dotenv
import os
import asyncio
import uuid
import json
import atexit

dotenv.load_dotenv()

mcp = FastMCP("Artifact MMO MCP Server")

ARTIFACTS_TOKEN = os.getenv("ARTIFACTS_TOKEN")
MEMORY_FILE = "server_memory.json"

# Memory structures
ACTION_QUEUES = {}
TASK_STATUSES = {}
PERSISTENT_MEMORY = {"queues": {}, "statuses": {}}


def get_client():
    """Create and return an HTTP client for the Artifact MMO API."""
    return httpx.AsyncClient(
        base_url="https://api.artifactsmmo.com",
        headers={
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {ARTIFACTS_TOKEN}",
        },
    )


# ------------------------
# Persistent Memory Helpers
# ------------------------
def load_memory():
    """Load queues and task statuses from disk."""
    global PERSISTENT_MEMORY, TASK_STATUSES
    if os.path.exists(MEMORY_FILE):
        try:
            with open(MEMORY_FILE, "r") as f:
                PERSISTENT_MEMORY = json.load(f)
            TASK_STATUSES.update(PERSISTENT_MEMORY.get("statuses", {}))
            print("[Server] Loaded persistent memory.")
        except Exception as e:
            print(f"[Server] Failed to load memory: {e}")


def save_memory():
    """Persist current queues and task statuses to disk."""
    try:
        # Convert asyncio queues to lists of pending actions
        queues_serializable = {
            char: list(queue._queue) for char, queue in ACTION_QUEUES.items()
        }
        data = {
            "queues": queues_serializable,
            "statuses": TASK_STATUSES,
        }
        with open(MEMORY_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print(f"[Server] Failed to save memory: {e}")


atexit.register(save_memory)


async def memory_autosave(interval=30):
    """Background task to periodically save state."""
    while True:
        save_memory()
        await asyncio.sleep(interval)


# ------------------------
# Core Action Queue Logic
# ------------------------
async def process_action_queue(character_name):
    """Process the action queue for a specific character."""
    while True:
        action, body, task_id = await ACTION_QUEUES[character_name].get()
        TASK_STATUSES[task_id] = {"status": "in_progress"}
        save_memory()

        try:
            result = await character_action(character_name, action, body)
            TASK_STATUSES[task_id] = {"status": "completed"}
            save_memory()
            if "cooldown" in result["data"] and "remaining_seconds" in result["data"]["cooldown"]:
                print(f"[Server] Action '{action}' for '{character_name}' on cooldown for {result['data']['cooldown']['remaining_seconds']} seconds.")
                await asyncio.sleep(result["data"]["cooldown"]["remaining_seconds"])
        except Exception as e:
            TASK_STATUSES[task_id] = {"status": "failed", "error": str(e)}
            save_memory()
        finally:
            ACTION_QUEUES[character_name].task_done()


@mcp.tool(description="Enqueue an action for a character to be executed asynchronously. Returns a task_id to track the action's status.")
async def enqueue_action(character_name: str, action: str, body: dict = None):
    """Enqueue an action for a character."""
    if character_name not in ACTION_QUEUES:
        ACTION_QUEUES[character_name] = asyncio.Queue()
        asyncio.create_task(process_action_queue(character_name))

    task_id = str(uuid.uuid4())
    await ACTION_QUEUES[character_name].put((action, body, task_id))
    TASK_STATUSES[task_id] = {"status": "pending"}
    save_memory()
    return {"task_id": task_id}


@mcp.tool(description="Manually dequeue the next action for a character. This is a debugging/admin tool.")
async def dequeue_action(character_name: str):
    """Manually dequeue the next action for a character (for debugging or admin)."""
    if character_name not in ACTION_QUEUES or ACTION_QUEUES[character_name].empty():
        return {"status": "empty"}

    action, body, task_id = await ACTION_QUEUES[character_name].get()
    ACTION_QUEUES[character_name].task_done()
    save_memory()
    return {"removed_task_id": task_id, "action": action, "body": body}


@mcp.tool(description="Get the status of a previously enqueued action using its task_id.")
async def get_task_status(task_id: str):
    """Get the status of a task."""
    return TASK_STATUSES.get(task_id, {"status": "not_found"})


async def character_action(character_name: str, action: str, body: dict = None):
    """Perform an action with a character."""
    async with get_client() as client:
        endpoint = f"/my/{character_name}/action/{action}"
        response = await client.post(endpoint, json=body or {})
        response.raise_for_status()
        return response.json()


# ------------------------
# Additional Utility Tools
# ------------------------
@mcp.tool(description="Retrieves a list of all characters belonging to the user.")
async def get_my_characters():
    async with get_client() as client:
        response = await client.get("/my/characters")
        response.raise_for_status()
        return response.json()


@mcp.tool(description="Return details and statistics about the game server.")
async def get_server_details():
    async with get_client() as client:
        response = await client.get("/")
        response.raise_for_status()
        return response.json()


@mcp.tool(description="Retrieves detailed information about a specific map, including its layout and interactions.")
async def get_map_details(map_id: int):
    async with get_client() as client:
        response = await client.get(f"/maps/{map_id}")
        response.raise_for_status()
        return response.json()


@mcp.tool(description="Retrieves detailed information about a specific item, including its stats and properties.")
async def get_item_details(code: str):
    async with get_client() as client:
        response = await client.get(f"/items/{code}")
        response.raise_for_status()
        return response.json()


@mcp.tool(description="Fetch all available items")
async def get_all_items():
    async with get_client() as client:
        response = await client.get("/items")
        response.raise_for_status()
        return response.json()


@mcp.tool(description="Fetch all available maps")
async def get_all_maps():
    async with get_client() as client:
        response = await client.get("/maps")
        response.raise_for_status()
        return response.json()


@mcp.tool(description="Retrieves a list of all monsters in the game.")
async def get_all_monsters():
    async with get_client() as client:
        response = await client.get("/monsters")
        response.raise_for_status()
        return response.json()


@mcp.tool(description="Retrieves detailed information about a specific monster, including its stats and loot.")
async def get_monster_details(code: str):
    async with get_client() as client:
        response = await client.get(f"/monsters/{code}")
        response.raise_for_status()
        return response.json()


# ------------------------
# Server Startup
# ------------------------
if __name__ == "__main__":
    load_memory()
    mcp.run(transport="http", background_tasks=[memory_autosave()], debug=True)
