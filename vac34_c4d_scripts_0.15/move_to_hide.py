import c4d

def create_hide_null(doc):
    """Creates and returns a new 'hide' null object with proper undo handling."""
    doc.StartUndo()
    try:
        hide_null = c4d.BaseObject(c4d.Onull)
        if not hide_null:
            raise RuntimeError("Failed to create 'hide' null object.")
        
        hide_null.SetName('hide')
        doc.InsertObject(hide_null)
        doc.AddUndo(c4d.UNDOTYPE_NEW, hide_null)
        
        # Set initial visibility
        hide_null[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 1
        hide_null[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = 1
        
        return hide_null
    finally:
        doc.EndUndo()

def move_objects_to_hide(doc, objects, hide_null):
    """Moves objects under hide_null with proper undo handling."""
    if not objects or not hide_null:
        return False
    
    doc.StartUndo()
    try:
        for obj in objects:
            if not obj:
                continue
                
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
            obj.Remove()
            obj.InsertUnder(hide_null)
            
            # Set visibility
            obj[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 1
            obj[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = 1
            
        return True
    finally:
        doc.EndUndo()

def main():
    doc = c4d.documents.GetActiveDocument()
    if not doc:
        return

    selected_objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    if not selected_objects:
        c4d.gui.MessageDialog('No objects selected.')
        return

    hide_null = doc.SearchObject('hide')
    if not hide_null:
        hide_null = create_hide_null(doc)
        if not hide_null:
            c4d.gui.MessageDialog('Failed to create "hide" null object.')
            return

    if not move_objects_to_hide(doc, selected_objects, hide_null):
        c4d.gui.MessageDialog('Failed to move objects to "hide" null.')
        return

    # Final cleanup
    doc.SetActiveObject(None, c4d.SELECTION_NEW)
    c4d.EventAdd()

if __name__ == '__main__':
    main()