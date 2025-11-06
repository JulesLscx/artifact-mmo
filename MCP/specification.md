# Model Context Protocol Server

This document specifies the Model Context Protocol (MCP) for the Artifact MMO game. The MCP is a set of tools that a model can use to interact with the game world.

## Authentication

Not needed

## Tools

The following tools are available to the model:

### `get_server_details()`

Return the status of the game server.

#### Response

```json
{
  "version": "6.0.1",
  "server_time": "2025-11-04T15:00:00Z",
  "max_level": 50,
  "max_skill_level": 100,
  "characters_online": 123,
  "season": {
    "name": "Season 1",
    "number": 1,
    "start_date": "2025-10-28T00:00:00Z",
    "badges": [
      {
        "code": "season_1_badge_1",
        "description": "Season 1 Badge 1",
        "required_points": 100
      }
    ],
    "skins": [
      {
        "code": "season_1_skin_1",
        "description": "Season 1 Skin 1",
        "required_points": 200
      }
    ]
  },
  "rate_limits": [
    {
      "type": "per_minute",
      "value": "60"
    }
  ]
}
```

### `get_my_characters()`

List all your characters

#### Arguments

#### Response

```json
{
  "data": [
    {
      "name": "string",
      "account": "string",
      "skin": "men1",
      "level": 0,
      "xp": 0,
      "max_xp": 0,
      "gold": 0,
      "speed": 0,
      "mining_level": 0,
      "mining_xp": 0,
      "mining_max_xp": 0,
      "woodcutting_level": 0,
      "woodcutting_xp": 0,
      "woodcutting_max_xp": 0,
      "fishing_level": 0,
      "fishing_xp": 0,
      "fishing_max_xp": 0,
      "weaponcrafting_level": 0,
      "weaponcrafting_xp": 0,
      "weaponcrafting_max_xp": 0,
      "gearcrafting_level": 0,
      "gearcrafting_xp": 0,
      "gearcrafting_max_xp": 0,
      "jewelrycrafting_level": 0,
      "jewelrycrafting_xp": 0,
      "jewelrycrafting_max_xp": 0,
      "cooking_level": 0,
      "cooking_xp": 0,
      "cooking_max_xp": 0,
      "alchemy_level": 0,
      "alchemy_xp": 0,
      "alchemy_max_xp": 0,
      "hp": 0,
      "max_hp": 0,
      "haste": 0,
      "critical_strike": 0,
      "wisdom": 0,
      "prospecting": 0,
      "initiative": 0,
      "threat": 0,
      "attack_fire": 0,
      "attack_earth": 0,
      "attack_water": 0,
      "attack_air": 0,
      "dmg": 0,
      "dmg_fire": 0,
      "dmg_earth": 0,
      "dmg_water": 0,
      "dmg_air": 0,
      "res_fire": 0,
      "res_earth": 0,
      "res_water": 0,
      "res_air": 0,
      "x": 0,
      "y": 0,
      "layer": "interior",
      "map_id": 0,
      "cooldown": 0,
      "weapon_slot": "string",
      "rune_slot": "string",
      "shield_slot": "string",
      "helmet_slot": "string",
      "body_armor_slot": "string",
      "leg_armor_slot": "string",
      "boots_slot": "string",
      "ring1_slot": "string",
      "ring2_slot": "string",
      "amulet_slot": "string",
      "artifact1_slot": "string",
      "artifact2_slot": "string",
      "artifact3_slot": "string",
      "utility1_slot": "string",
      "utility1_slot_quantity": 0,
      "utility2_slot": "string",
      "utility2_slot_quantity": 0,
      "bag_slot": "string",
      "task": "string",
      "task_type": "string",
      "task_progress": 0,
      "task_total": 0,
      "inventory_max_items": 0
    }
  ]
}
```

If `name` is provided, the response will be the details of the specified character:

```json
{
  "data": {
    "name": "string",
    "account": "string",
    "skin": "men1",
    "level": 0,
    "xp": 0,
    "max_xp": 0,
    "gold": 0,
    "speed": 0,
    "mining_level": 0,
    "mining_xp": 0,
    "mining_max_xp": 0,
    "woodcutting_level": 0,
    "woodcutting_xp": 0,
    "woodcutting_max_xp": 0,
    "fishing_level": 0,
    "fishing_xp": 0,
    "fishing_max_xp": 0,
    "weaponcrafting_level": 0,
    "weaponcrafting_xp": 0,
    "weaponcrafting_max_xp": 0,
    "gearcrafting_level": 0,
    "gearcrafting_xp": 0,
    "gearcrafting_max_xp": 0,
    "jewelrycrafting_level": 0,
    "jewelrycrafting_xp": 0,
    "jewelrycrafting_max_xp": 0,
    "cooking_level": 0,
    "cooking_xp": 0,
    "cooking_max_xp": 0,
    "alchemy_level": 0,
    "alchemy_xp": 0,
    "alchemy_max_xp": 0,
    "hp": 0,
    "max_hp": 0,
    "haste": 0,
    "critical_strike": 0,
    "wisdom": 0,
    "prospecting": 0,
    "initiative": 0,
    "threat": 0,
    "attack_fire": 0,
    "attack_earth": 0,
      "attack_water": 0,
      "attack_air": 0,
      "dmg": 0,
      "dmg_fire": 0,
      "dmg_earth": 0,
      "dmg_water": 0,
      "dmg_air": 0,
      "res_fire": 0,
      "res_earth": 0,
      "res_water": 0,
      "res_air": 0,
      "x": 0,
      "y": 0,
      "layer": "interior",
      "map_id": 0,
      "cooldown": 0,
      "weapon_slot": "string",
      "rune_slot": "string",
      "shield_slot": "string",
      "helmet_slot": "string",
      "body_armor_slot": "string",
      "leg_armor_slot": "string",
      "boots_slot": "string",
      "ring1_slot": "string",
      "ring2_slot": "string",
      "amulet_slot": "string",
      "artifact1_slot": "string",
      "artifact2_slot": "string",
      "artifact3_slot": "string",
      "utility1_slot": "string",
      "utility1_slot_quantity": 0,
      "utility2_slot": "string",
      "utility2_slot_quantity": 0,
      "bag_slot": "string",
      "task": "string",
      "task_type": "string",
      "task_progress": 0,
      "task_total": 0,
      "inventory_max_items": 0
  }
}
```

### `get_map_details(map_id: int)`

Get the details of a specific map.

#### Arguments

- `map_id` (int): The ID of the map to get the details of.

#### Response

```json
{
  "data": {
    "map_id": 0,
    "name": "string",
    "skin": "string",
    "x": 0,
    "y": 0,
    "layer": "interior",
    "access": {
      "type": "standard",
      "conditions": [
        {
          "code": "string",
          "operator": "eq",
          "value": 0
        }
      ]
    },
    "interactions": {
      "content": {
        "type": "monster",
        "code": "string"
      },
      "transition": {
        "map_id": 0,
        "x": 0,
        "y": 0,
        "layer": "interior",
        "conditions": [
          {
            "code": "string",
            "operator": "eq",
            "value": 0
          }
        ]
      }
    }
  }
}
```

### `get_item_details(code: str)`

Get the details of a specific item.

#### Arguments

- `code` (str): The code of the item to get the details of.

#### Response

```json
{
  "data": {
    "code": "string",
    "name": "string",
    "description": "string",
    "type": "string",
    "slot": "string",
    "rarity": "string",
    "level": 0,
    "is_tradable": true,
    "is_craftable": true,
    "is_purchasable": true,
    "is_lootable": true,
    "is_equipable": true,
    "is_consumable": true,
    "is_seasonal": true,
    "crafting_recipe": [
      {
        "item_code": "string",
        "quantity": 0
      }
    ],
    "equipment_stats": {
      "hp": 0,
      "haste": 0,
      "critical_strike": 0,
      "wisdom": 0,
      "prospecting": 0,
      "initiative": 0,
      "threat": 0,
      "attack_fire": 0,
      "attack_earth": 0,
      "attack_water": 0,
      "attack_air": 0,
      "dmg": 0,
      "dmg_fire": 0,
      "dmg_earth": 0,
      "dmg_water": 0,
      "dmg_air": 0,
      "res_fire": 0,
      "res_earth": 0,
      "res_water": 0,
      "res_air": 0
    },
    "consumable_effects": [
      {
        "effect": "string",
        "value": 0,
        "duration": 0
      }
    ]
  }
}
```

### `get_all_items()`

Get the list of all items.

#### Response

```json
{
  "data": [
    {
      "code": "string",
      "name": "string",
      "description": "string",
      "type": "string",
      "slot": "string",
      "rarity": "string",
      "level": 0,
      "is_tradable": true,
      "is_craftable": true,
      "is_purchasable": true,
      "is_lootable": true,
      "is_equipable": true,
      "is_consumable": true,
      "is_seasonal": true
    }
  ]
}
```

### `get_all_maps()`

Get the list of all maps.

#### Response

```json
{
  "data": [
    {
      "map_id": 0,
      "name": "string",
      "skin": "string",
      "x": 0,
      "y": 0,
      "layer": "interior",
      "access": {
        "type": "standard",
        "conditions": [
          {
            "code": "string",
            "operator": "eq",
            "value": 0
          }
        ]
      },
      "interactions": {
        "content": {
          "type": "monster",
          "code": "string"
        },
        "transition": {
          "map_id": 0,
          "x": 0,
          "y": 0,
          "layer": "interior",
          "conditions": [
            {
              "code": "string",
              "operator": "eq",
              "value": 0
            }
          ]
        }
      }
    }
  ]
}
```

### `get_all_monsters()`

Get the list of all monsters.

#### Response

```json
{
  "data": [
    {
      "code": "string",
      "name": "string",
      "description": "string",
      "level": 0,
      "is_boss": true,
      "hp": 0,
      "speed": 0,
      "initiative": 0,
      "attack_fire": 0,
      "attack_earth": 0,
      "attack_water": 0,
      "attack_air": 0,
      "dmg": 0,
      "dmg_fire": 0,
      "dmg_earth": 0,
      "dmg_water": 0,
      "dmg_air": 0,
      "res_fire": 0,
      "res_earth": 0,
      "res_water": 0,
      "res_air": 0,
      "loots": [
        {
          "item_code": "string",
          "quantity": 0,
          "rate": 0
        }
      ]
    }
  ]
}
```

### `get_monster_details(code: str)`

Get the details of a specific monster.

#### Arguments

- `code` (str): The code of the monster to get the details of.

#### Response

```json
{
  "data": {
    "code": "string",
    "name": "string",
    "description": "string",
    "level": 0,
    "is_boss": true,
    "hp": 0,
    "speed": 0,
    "initiative": 0,
    "attack_fire": 0,
    "attack_earth": 0,
    "attack_water": 0,
    "attack_air": 0,
    "dmg": 0,
    "dmg_fire": 0,
    "dmg_earth": 0,
    "dmg_water": 0,
    "dmg_air": 0,
    "res_fire": 0,
    "res_earth": 0,
    "res_water": 0,
    "res_air": 0,
    "loots": [
      {
        "item_code": "string",
        "quantity": 0,
        "rate": 0
      }
    ]
  }
}
```

### `character_action(character_name: str, action: str, **kwargs)`

Perform an action with a character.

#### Arguments

- `character_name` (str): The name of the character to perform the action with.
- `action` (str): The action to perform. Must be one of the following:
  - `move`: Moves a character on the map using either the map's ID or X and Y position.
  - `transition`: Execute a transition from the current map to another layer.
  - `rest`: Recovers hit points by resting.
  - `equip`: Equip an item on your character.
  - `unequip`: Unequip an item on your character.
  - `use`: Use an item as a consumable.
  - `fight`: Start a fight against a monster on the character's map.
  - `gathering`: Harvest a resource on the character's map.
  - `crafting`: Craft an item. The character must be on a map with a workshop.
  - `deposit_gold`: Deposit gold in a bank on the character's map.
  - `deposit_item`: Deposit multiple items in a bank on the character's map.
  - `withdraw_item`: Take items from your bank and put them in the character's inventory.
  - `withdraw_gold`: Withdraw gold from your bank.
  - `buy_bank_expansion`: Buy a 20 slots bank expansion.
  - `npc_buy`: Buy an item from an NPC on the character's map.
  - `npc_sell`: Sell an item to an NPC on the character's map.
  - `ge_buy`: Buy an item at the Grand Exchange on the character's map.
  - `ge_sell`: Create a sell order at the Grand Exchange on the character's map.
  - `ge_cancel`: Cancel a sell order at the Grand Exchange on the character's map.
  - `complete_task`: Complete a task.
  - `task_exchange`: Exchange 6 tasks coins for a random reward.
  - `new_task`: Accepting a new task.
  - `task_trade`: Trading items with a Tasks Master.
  - `task_cancel`: Cancel a task for 1 tasks coin.
  - `give_gold`: Give gold to another character in your account on the same map.
  - `give_item`: Give items to another character in your account on the same map.
  - `delete_item`: Delete an item from your character's inventory.
  - `change_skin`: Change the skin of your character.
- `**json`: Additional arguments for the action. See the following sections for the arguments for each action.

#### Responses

The response will vary depending on the action. See the following sections for the response for each action.

#### `move`

##### Arguments

- `x` (int, optional): The x coordinate of the destination.
- `y` (int, optional): The y coordinate of the destination.
- `map_id` (int, optional): The map ID of the destination.

Either `map_id` or both `x` and `y` must be provided.

##### Response

```json
{
  "data": {
    "cooldown": {
      "total_seconds": 0,
      "remaining_seconds": 0,
      "started_at": "2025-11-04T15:00:00Z",
      "expiration": "2025-11-04T15:00:00Z",
      "reason": "movement"
    },
    "destination": {
      "map_id": 0,
      "name": "string",
      "skin": "string",
      "x": 0,
      "y": 0,
      "layer": "interior",
      "access": {
        "type": "standard",
        "conditions": [
          {
            "code": "string",
            "operator": "eq",
            "value": 0
          }
        ]
      },
      "interactions": {
        "content": {
          "type": "monster",
          "code": "string"
        },
        "transition": {
          "map_id": 0,
          "x": 0,
          "y": 0,
          "layer": "interior",
          "conditions": [
            {
              "code": "string",
              "operator": "eq",
              "value": 0
            }
          ]
        }
      }
    },
    "path": [
      [
        0,
        0
      ]
    ],
    "character": {
      "name": "string",
      "account": "string",
      "skin": "men1",
      "level": 0,
      "xp": 0,
      "max_xp": 0,
      "gold": 0,
      "speed": 0,
      "mining_level": 0,
      "mining_xp": 0,
      "mining_max_xp": 0,
      "woodcutting_level": 0,
      "woodcutting_xp": 0,
      "woodcutting_max_xp": 0,
      "fishing_level": 0,
      "fishing_xp": 0,
      "fishing_max_xp": 0,
      "weaponcrafting_level": 0,
      "weaponcrafting_xp": 0,
      "weaponcrafting_max_xp": 0,
      "gearcrafting_level": 0,
      "gearcrafting_xp": 0,
      "gearcrafting_max_xp": 0,
      "jewelrycrafting_level": 0,
      "jewelrycrafting_xp": 0,
      "jewelrycrafting_max_xp": 0,
      "cooking_level": 0,
      "cooking_xp": 0,
      "cooking_max_xp": 0,
      "alchemy_level": 0,
      "alchemy_xp": 0,
      "alchemy_max_xp": 0,
      "hp": 0,
      "max_hp": 0,
      "haste": 0,
      "critical_strike": 0,
      "wisdom": 0,
      "prospecting": 0,
      "initiative": 0,
      "threat": 0,
      "attack_fire": 0,
      "attack_earth": 0,
      "attack_water": 0,
      "attack_air": 0,
      "dmg": 0,
      "dmg_fire": 0,
      "dmg_earth": 0,
      "dmg_water": 0,
      "dmg_air": 0,
      "res_fire": 0,
      "res_earth": 0,
      "res_water": 0,
      "res_air": 0,
      "x": 0,
      "y": 0,
      "layer": "interior",
      "map_id": 0,
      "cooldown": 0,
      "weapon_slot": "string",
      "rune_slot": "string",
      "shield_slot": "string",
      "helmet_slot": "string",
      "body_armor_slot": "string",
      "leg_armor_slot": "string",
      "boots_slot": "string",
      "ring1_slot": "string",
      "ring2_slot": "string",
      "amulet_slot": "string",
      "artifact1_slot": "string",
      "artifact2_slot": "string",
      "artifact3_slot": "string",
      "utility1_slot": "string",
      "utility1_slot_quantity": 0,
      "utility2_slot": "string",
      "utility2_slot_quantity": 0,
      "bag_slot": "string",
      "task": "string",
      "task_type": "string",
      "task_progress": 0,
      "task_total": 0,
      "inventory_max_items": 0
    }
  }
}
```

#### `transition`

##### Arguments

No arguments required.

##### Response

```json
{
  "data": {
    "cooldown": {
      "total_seconds": 0,
      "remaining_seconds": 0,
      "started_at": "2025-11-04T15:00:00Z",
      "expiration": "2025-11-04T15:00:00Z",
      "reason": "transition"
    },
    "destination": {
      "map_id": 0,
      "name": "string",
      "skin": "string",
      "x": 0,
      "y": 0,
      "layer": "interior",
      "access": {
        "type": "standard",
        "conditions": [
          {
            "code": "string",
            "operator": "eq",
            "value": 0
          }
        ]
      },
      "interactions": {
        "content": {
          "type": "monster",
          "code": "string"
        },
        "transition": {
          "map_id": 0,
          "x": 0,
          "y": 0,
          "layer": "interior",
          "conditions": [
            {
              "code": "string",
              "operator": "eq",
              "value": 0
            }
          ]
        }
      }
    },
    "transition": {
      "map_id": 0,
      "x": 0,
      "y": 0,
      "layer": "interior",
      "conditions": [
        {
          "code": "string",
          "operator": "eq",
          "value": 0
        }
      ]
    },
    "character": {
      "name": "string",
      "account": "string",
      "skin": "men1",
      "level": 0,
      "xp": 0,
      "max_xp": 0,
      "gold": 0,
      "speed": 0,
      "mining_level": 0,
      "mining_xp": 0,
      "mining_max_xp": 0,
      "woodcutting_level": 0,
      "woodcutting_xp": 0,
      "woodcutting_max_xp": 0,
      "fishing_level": 0,
      "fishing_xp": 0,
      "fishing_max_xp": 0,
      "weaponcrafting_level": 0,
      "weaponcrafting_xp": 0,
      "weaponcrafting_max_xp": 0,
      "gearcrafting_level": 0,
      "gearcrafting_xp": 0,
      "gearcrafting_max_xp": 0,
      "jewelrycrafting_level": 0,
      "jewelrycrafting_xp": 0,
      "jewelrycrafting_max_xp": 0,
      "cooking_level": 0,
      "cooking_xp": 0,
      "cooking_max_xp": 0,
      "alchemy_level": 0,
      "alchemy_xp": 0,
      "alchemy_max_xp": 0,
      "hp": 0,
      "max_hp": 0,
      "haste": 0,
      "critical_strike": 0,
      "wisdom": 0,
      "prospecting": 0,
      "initiative": 0,
      "threat": 0,
      "attack_fire": 0,
      "attack_earth": 0,
      "attack_water": 0,
      "attack_air": 0,
      "dmg": 0,
      "dmg_fire": 0,
      "dmg_earth": 0,
      "dmg_water": 0,
      "dmg_air": 0,
      "res_fire": 0,
      "res_earth": 0,
      "res_water": 0,
      "res_air": 0,
      "x": 0,
      "y": 0,
      "layer": "interior",
      "map_id": 0,
      "cooldown": 0,
      "weapon_slot": "string",
      "rune_slot": "string",
      "shield_slot": "string",
      "helmet_slot": "string",
      "body_armor_slot": "string",
      "leg_armor_slot": "string",
      "boots_slot": "string",
      "ring1_slot": "string",
      "ring2_slot": "string",
      "amulet_slot": "string",
      "artifact1_slot": "string",
      "artifact2_slot": "string",
      "artifact3_slot": "string",
      "utility1_slot": "string",
      "utility1_slot_quantity": 0,
      "utility2_slot": "string",
      "utility2_slot_quantity": 0,
      "bag_slot": "string",
      "task": "string",
      "task_type": "string",
      "task_progress": 0,
      "task_total": 0,
      "inventory_max_items": 0
    }
  }
}
```

