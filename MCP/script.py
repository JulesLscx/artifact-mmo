from server import mcp
from fastmcp.client import Client
import asyncio
import os
url = os.getenv("MCP_SERVER_URL", "http://localhost:8000")
client = Client(url)
characters = ["Jules", "Jules2", "Jules3", "Jules4", "Jules5"]
map_important_locations = {
    "starting_area": {"x": 0, "y": 0},
    "copper_mine": {"x": 2, "y": 0},
    "chicken_area": {"x": 0, "y": 1},
    "blacksmith": {"x": 1, "y": 5},
    "tool_shop": {"x": 2, "y": 1},
}
async def gather_copper(character_name="Jules", n=60):
    async with client:
        # Move to 2,0 add to queue
        await client.call_tool("enqueue_action", {"character_name": character_name, "action": "move", "body": map_important_locations["copper_mine"]})
        for _ in range(n):
            # Mine copper
            await client.call_tool("enqueue_action", {"character_name": character_name, "action": "gathering", "body": {"resource": "copper"}})

async def kill_chickens(character_name="Jules2", n=20):
    async with client:
        await client.call_tool("enqueue_action", {"character_name": character_name, "action": "move", "body": map_important_locations["chicken_area"]})
        for _ in range(n):
            # Fight chicken
            await client.call_tool("enqueue_action", {"character_name": character_name, "action": "fight", "body": {"target": "chicken"}})
            await client.call_tool("enqueue_action", {"character_name": character_name, "action": "rest"})
async def craft_copper_pickaxe(character_name="Jules"):
    async with client:
        await client.call_tool("enqueue_action", {"character_name": character_name, "action": "move", "body": map_important_locations["blacksmith"]})
        await client.call_tool("enqueue_action", {"character_name": character_name, "action": "crafting", "body": {"code": "copper_bar", "quantity": 6}})
        await client.call_tool("enqueue_action", {"character_name": character_name, "action": "move", "body": map_important_locations["tool_shop"]})
        await client.call_tool("enqueue_action", {"character_name": character_name, "action": "crafting", "body": {"code": "copper_pickaxe", "quantity": 1}})
if __name__ == "__main__":
    for i, character in enumerate(characters):
        asyncio.run(kill_chickens(character_name=character, n=1))
