import c4d
from c4d import gui

def is_shift_pressed():
    """Check if Shift key is pressed."""
    bc = c4d.BaseContainer()
    if c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, c4d.KEY_SHIFT, bc):
        return bc[c4d.BFM_INPUT_VALUE]
    return False

def move_object_to_top(doc, obj):
    """Move object to top level of Object Manager."""
    if not obj:
        return False
    
    # Store original transform
    original_matrix = obj.GetMg()
    
    # Remove and reinsert at top level
    doc.AddUndo(c4d.UNDOTYPE_DELETE, obj)
    obj.Remove()
    doc.InsertObject(obj, pred=None, checknames=True)
    doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
    
    # Restore transform
    obj.SetMg(original_matrix)
    return True

def move_object_to_first_in_parent(doc, obj):
    """Move object to first position within its parent."""
    if not obj:
        return False
    
    parent = obj.GetUp()
    if not parent:
        return move_object_to_top(doc, obj)
    
    # Store original transform
    original_matrix = obj.GetMg()
    
    # Remove and reinsert as first child of parent
    doc.AddUndo(c4d.UNDOTYPE_DELETE, obj)
    obj.Remove()
    doc.InsertObject(obj, parent=parent, pred=None, checknames=True)
    doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
    
    # Restore transform
    obj.SetMg(original_matrix)
    return True

def main():
    doc = c4d.documents.GetActiveDocument()
    if not doc:
        return

    selected_objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    if not selected_objects:
        gui.MessageDialog("No objects selected.")
        return

    shift_pressed = is_shift_pressed()
    doc.StartUndo()
    
    try:
        for obj in selected_objects:
            if not obj:
                continue
                
            if shift_pressed:
                move_object_to_first_in_parent(doc, obj)
            else:
                move_object_to_top(doc, obj)
                
    except Exception as e:
        gui.MessageDialog(f"Error: {str(e)}")
    finally:
        doc.EndUndo()
        c4d.EventAdd(c4d.EVENT_FORCEREDRAW)

if __name__ == '__main__':
    main()