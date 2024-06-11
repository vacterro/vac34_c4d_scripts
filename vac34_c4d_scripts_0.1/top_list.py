import c4d
from c4d import gui

def main():
    doc = c4d.documents.GetActiveDocument()
    selected_objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    
    if not selected_objects:
        gui.MessageDialog("No objects selected.")
        return

    # Check if the Shift key is pressed
    bc = c4d.BaseContainer()
    shift_pressed = c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, c4d.KEY_SHIFT, bc) and bc[c4d.BFM_INPUT_VALUE]

    # Start undo recording
    doc.StartUndo()

    for obj in selected_objects:
        if shift_pressed:
            # The Shift key is pressed, move to the first position within the parent if it exists
            parent = obj.GetUp()
            if parent:
                doc.AddUndo(c4d.UNDOTYPE_DELETE, obj)
                obj.Remove()
                doc.InsertObject(obj, parent=parent, pred=None, checknames=True)
                doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
            else:
                doc.AddUndo(c4d.UNDOTYPE_DELETE, obj)
                obj.Remove()
                doc.InsertObject(obj, pred=None, checknames=True)
                doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
        else:
            # The Shift key is not pressed, move to the top of the Object Manager
            doc.AddUndo(c4d.UNDOTYPE_DELETE, obj)
            obj.Remove()
            doc.InsertObject(obj, pred=None, checknames=True)
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)

    # End undo recording
    doc.EndUndo()

    # Force a document update
    c4d.EventAdd(c4d.EVENT_FORCEREDRAW)

if __name__ == '__main__':
    main()
