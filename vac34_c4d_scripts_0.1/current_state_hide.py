import c4d

def main():
    # Get the active document
    doc = c4d.documents.GetActiveDocument()

    # Start an undo action
    doc.StartUndo()

    # Check if Shift key is pressed
    bc = c4d.BaseContainer()
    shift_pressed = c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, c4d.KEY_SHIFT, bc) and bc[c4d.BFM_INPUT_VALUE]

    # Get the currently selected original object
    original_object = doc.GetActiveObject()
    if original_object is None:
        c4d.gui.MessageDialog("No object selected.")
        return

    # Make a Current State of the currently selected original object
    c4d.CallCommand(12233)  # 'Current State to Object' command
    new_object = doc.GetActiveObject()
    if new_object is None:
        c4d.gui.MessageDialog("No object created.")
        return

    # If Shift is pressed, move the original object to the "hide" null
    if shift_pressed:
        hide_null = doc.SearchObject("hide")
        if hide_null is None:
            hide_null = c4d.BaseObject(c4d.Onull)
            hide_null.SetName("hide")
            hide_null[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 0  # On in Editor
            hide_null[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = 0  # On in Renderer
            doc.InsertObject(hide_null)
            doc.AddUndo(c4d.UNDOTYPE_NEW, hide_null)

        original_object.Remove()
        original_object.InsertUnder(hide_null)
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, original_object)

    # Hide the original object
    original_object[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 1  # Off in Editor
    original_object[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = 1  # Off in Renderer
    original_object.SetName(original_object.GetName() + "_hided")  # Append "_hided" to the original object's name
    original_object.Message(c4d.MSG_UPDATE)
    doc.AddUndo(c4d.UNDOTYPE_CHANGE, original_object)

    # Select the new created Current state object
    doc.SetActiveObject(new_object, c4d.SELECTION_NEW)

    # Deselect the object
    doc.SetActiveObject(None)

    # End the undo action
    doc.EndUndo()

    # Make sure to update the scene to reflect the changes
    c4d.EventAdd()

if __name__ == '__main__':
    main()
