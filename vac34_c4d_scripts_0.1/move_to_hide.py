import c4d

def main():
    # Get the active document
    doc = c4d.documents.GetActiveDocument()

    # Get the active objects (selected objects)
    selected_objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)

    # Check if any objects are selected
    if not selected_objects:
        c4d.gui.MessageDialog('No objects selected.')
        return

    # Search for the null object named "hide"
    hide_null = doc.SearchObject('hide')

    # If the "hide" null doesn't exist, create it
    if hide_null is None:
        # Start an undo action for creating the "hide" null
        doc.StartUndo()

        # Create the "hide" null object
        hide_null = c4d.BaseObject(c4d.Onull)
        hide_null.SetName('hide')
        doc.InsertObject(hide_null)

        # Add undo command for creating the "hide" null
        doc.AddUndo(c4d.UNDOTYPE_NEW, hide_null)

        # End the undo action
        doc.EndUndo()

    # Start an undo action for moving objects under the "hide" null
    doc.StartUndo()

    # Move selected objects under the "hide" null
    for obj in selected_objects:
        # Add undo command for moving object
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)

        # Reparent the object under the "hide" null
        obj.Remove()  # Remove from current hierarchy
        obj.InsertUnder(hide_null)  # Insert under "hide"

        # Turn off visibility for the object
        obj[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 1
        obj[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = 1

    # End the undo action for moving objects
    doc.EndUndo()

    # Turn off visibility for the "hide" null object
    hide_null[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 1
    hide_null[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = 1

    # Deselect the "hide" null object
    doc.SetActiveObject(None, c4d.SELECTION_NEW)

    # Update the Cinema 4D interface
    c4d.EventAdd()

# Execute the main function
if __name__ == '__main__':
    main()
