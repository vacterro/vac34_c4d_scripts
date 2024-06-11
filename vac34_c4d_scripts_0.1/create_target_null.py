import c4d

def main():
    # Get the active document
    doc = c4d.documents.GetActiveDocument()

    # Get the currently selected objects
    selected_objs = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_SELECTIONORDER)

    # Check if any objects are selected
    if not selected_objs:
        print("No objects selected. Please select one or more objects.")
        return

    # Detect if the shift key is pressed
    bc = c4d.BaseContainer()
    shift_pressed = c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, c4d.KEY_SHIFT, bc) and bc.GetInt32(c4d.BFM_INPUT_VALUE)

    # Start an undo group
    doc.StartUndo()

    # Loop through each selected object and create a target null
    for selected_obj in selected_objs:
        # Determine the position for the null object
        obj_pos = c4d.Vector(0, 0, 0) if shift_pressed else selected_obj.GetMg().off

        # Create a Null object as the target for the selected object
        null_obj = c4d.BaseObject(c4d.Onull)
        null_obj_name = selected_obj.GetName() + "_target"  # Set the name of the target null
        null_obj.SetName(null_obj_name)

        # Set the position of the Null object to the determined position
        null_obj.SetAbsPos(obj_pos)

        # Insert the Null object into the document
        doc.InsertObject(null_obj)
        doc.AddUndo(c4d.UNDOTYPE_NEW, null_obj)

        # Add a Target Tag to the selected object
        target_tag = selected_obj.MakeTag(c4d.Ttargetexpression)
        if not target_tag:
            print(f"Failed to create a Target Tag for {selected_obj.GetName()}.")
            continue  # Skip to the next selected object

        # Add an undo step for creating the Target Tag
        doc.AddUndo(c4d.UNDOTYPE_NEW, target_tag)

        # Set the Null object as the target in the Target Tag properties
        target_tag[c4d.TARGETEXPRESSIONTAG_LINK] = null_obj

    # End the undo group
    doc.EndUndo()

    # Update the document
    c4d.EventAdd()

# Execute main()
if __name__ == '__main__':
    main()
