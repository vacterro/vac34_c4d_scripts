<div align="center">

# vac34 Cinema 4D Scripts

**Small workflow scripts for Maxon Cinema 4D: hierarchy cleanup, naming, visibility, selections, instances, materials, lights, and repetitive Object Manager actions.**

![Cinema 4D](https://img.shields.io/badge/Cinema%204D-2024%2B-011A6A?style=flat-square)
![Python](https://img.shields.io/badge/Cinema%204D-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Collection](https://img.shields.io/badge/collection-0.15-D4B86A?style=flat-square)

</div>

## Install

Copy the folder `vac34_c4d_scripts_0.15` into your Cinema 4D scripts directory:

```text
%APPDATA%\Maxon\Maxon Cinema 4D 2024_XXXXXXXX\library\scripts
```

Press **Win+R**, enter `%appdata%`, and navigate from there if you do not know the exact Maxon profile folder.

Each script includes its matching toolbar icon where available.

## Script catalog

| Script | What it does |
|---|---|
| `area_light_at_cam.py` | creates a Redshift Area Light at the current viewport/camera view |
| `color_chooser.py` | opens a color picker and applies the chosen Object Manager icon color to selected objects |
| `create_target_null.py` | adds a Target tag and creates a target null; Shift changes placement behavior and multi-selection can share one null |
| `current_state_hide.py` | runs Current State to Object, hides the source, and marks it as hidden; Shift can move results under a `hide` null |
| `execute_axis_center.py` | triggers the Execute action from Axis Center, useful as a hotkey |
| `find_selected_material.py` | finds and selects scene objects using the currently selected material and reports hierarchy paths |
| `hide_unhide.py` | toggles selected objects' viewport and render visibility |
| `move_to_hide.py` | hides selected objects and moves them under a `hide` null, creating it when needed |
| `multiple_instance.py` | converts selected objects after the first selection into Render Instances of the first object |
| `name_adopt.py` | adopts the parent object's name |
| `name_inherit.py` | inherits a child object's name |
| `remove_empty_nulls.py` | recursively removes empty null objects |
| `remove_still_keyframes.py` | removes keyframes that do not change transform coordinates across the timeline |
| `selection_object.py` | creates a Selection Object from the current object selection |
| `sort_by_type_name.py` | sorts children by Cinema 4D object type and name; Shift sorts alphabetically only |
| `top_list.py` | moves selected objects to the top of the Object Manager list; Shift keeps the move inside the parent |
| `update_polygon_selection.py` | triggers Update for the selected Polygon Selection tag |

### Collection 0.15

- `create_target_null`: Shift + multi-object selection can create one shared null.
- Added `sort_by_type_name`.
- Script undo behavior was repaired across the collection.

## Visual reference

<details>
<summary><b>Open script icon / behavior gallery</b></summary>

<br>

<table>
<tr><td width="25%">![area light](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/04f924b5-4e75-4920-bc5f-c838b4609e53)</td><td width="25%">![color chooser](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/813c00ee-0652-4094-bff5-51ffae7339e8)</td><td width="25%">![target null](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/5bb6e60c-3d79-42b8-a7a2-a334aeb6770c)</td><td width="25%">![hide](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/bdc2e437-390d-44f1-a4b3-ac6ebe30f646)</td></tr>
</table>

</details>


## Project network

Part of the broader **SAIPEN / vacterro** project ecosystem.

[**Author hub**](https://github.com/vacterro) · [**SAIPEN HQ**](https://github.com/saipenhq) · [**SAIPEN Core**](https://github.com/vacterro/saipen) · [**ZAICODE**](https://github.com/vacterro/zaicode) · [**FastPrompter**](https://github.com/vacterro/FastPrompter) · [**SAIPEN Community**](https://discord.gg/SEYaYkuVgN)

For reproducible bugs and durable feature requests, use [GitHub Issues](https://github.com/vacterro/vac34_c4d_scripts/issues).

<!-- VACTERRO_SUPPORT:BEGIN -->
---
<sub>If the Cinema 4D script collection is useful to you, optional support: [Buy Me a Coffee](https://buymeacoffee.com/vacuum34) · [Boosty](https://boosty.to/vacuum34/donate) · [PayPal](https://paypal.me/AlexNelin) · [other ways](https://github.com/vacterro/vacterro/blob/main/SUPPORT.md)</sub>
<!-- VACTERRO_SUPPORT:END -->
