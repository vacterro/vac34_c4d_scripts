# vac34_c4d_scripts_0.1
My custom Cinema 4D Scripts. 

Installing:

Just copy the folder with scripts to C:\Users\ [USERNAME] \AppData\Roaming\Maxon\Maxon Cinema 4D 2024_XXXXXXXX\library\scripts

To quickly get to the AppData folder, just hit WIN + R, type there %appdata%, Enter.

---
![area_cam](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/04f924b5-4e75-4920-bc5f-c838b4609e53)
area_light_at_cam
- Creates RS Area Light at current viewport view.

---

![create_target_null](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/5bb6e60c-3d79-42b8-a7a2-a334aeb6770c)
create_target_null
- When Object is Selected: adds to the object Target Tag and creates the targeted null at the object position.
- Shift-Click: Creates at World origin.

---

![current_state_hide](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/5e19a575-eabe-4c2e-8b25-df5c27eaedf0)
current_state_hide

- When Object is Selected: executes "Current State to Object", hides the original object (render/viewport Off) and adds to the name _hided.
- Shift-Click: Also moves as children to the "hide" null. Creates the null named "hide" if it does not exist.

---

![execute_axis_center](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/4ccb79a5-1729-410a-9a3d-e5c3c6fd6b7c)
execute_axis_center

- Executes the "Execute" button in "Axis center" tab. (_Can be a hotkey_)

![2024-06-12_005639](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/c5384a2a-0931-4560-8cc5-ed038d899cb9)

---

![hide_unhide](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/bdc2e437-390d-44f1-a4b3-ac6ebe30f646)
hide_unhide

- When Object is Selected: Toggles the Viewport/Renderer Visibility: On and Off.

---

![move_to_hide](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/15a0c149-9c55-4b1e-a41f-cdedba987e4a)
move_to_hide

- When Object(s) is Selected: Sets its visibility to "Off" and Moves as children to the "hide" null. Creates the "hide" null if it does not exists.

---

![name_adopt](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/a23fc9fc-e33d-42a3-a22e-7b5e52feae70)
name_adopt

- When Object is Selected: Adopts the name from the Parent
![adopt](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/63c6f0bc-b1c1-4128-850d-1df47324e1dd)

---

![name_inherit](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/89ef3150-9100-4506-8fc9-8cabb634a18f)
name_inherit

- When Object is Selected: Inherits the name from the Children
![inherit](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/a4167067-6a2a-402b-bc17-8d8d9bba0a95)

---

![remove_still_keyframes](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/1d027f80-ff0d-408f-aa82-67e4dad940ae)
remove_still_keyframes

- When Object is Selected: Clears keyframes, that does not transforming coordinates in whole timeline.

---

![selection_object](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/04e5c721-c9c2-46fd-ba48-12c9fb55a574)
selection_object

- When Objects are Selected: Creates the "Selection Object".

![2024-06-12_013637](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/708f26f7-de84-4c37-a1dd-d20161582a8d)

---

![top_list](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/46cd14fe-de60-4e38-8dad-3bb5a435ad2e)
top_list

- When Object(s) is Selected: Moves to the first order place in the "Object Manager" list.
- Shift + Click: Moves to the first order place within the Parent hierarchy.

---

![update_polygon_selection](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/01cfdced-5b50-485b-b028-3b91baabb93f)
update_polygon_selection

- When Selected "Polygon Selection" on the Object: Executes the "Update" button. (_Can be a hotkey_)

![update_polygon_selection_example](https://github.com/vacterro/vac34_c4d_scripts/assets/143219053/5ba1dd9e-3069-45ea-811c-0a0d6e3cec5d)
