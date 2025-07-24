import c4d

def toggle_visibility():
    # Get the active document
    doc = c4d.documents.GetActiveDocument()
    
    # Get the selected objects
    objs = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    if not objs:
        print("No objects selected.")
        return

    # Start an undo action
    doc.StartUndo()

    # Get the current state of the first selected object's visibility
    first_obj = objs[0]
    renderVisibility = first_obj[c4d.ID_BASEOBJECT_VISIBILITY_RENDER]
    editorVisibility = first_obj[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR]
    
    # Calculate the new visibility state for all objects based on the first object
    newRenderVisibility = 1 if renderVisibility != 1 else 2
    newEditorVisibility = 1 if editorVisibility != 1 else 2
    
    for obj in objs:
        # Register undo for visibility change
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)

        # Apply the new visibility state to all objects
        obj[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = newRenderVisibility
        obj[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = newEditorVisibility

    # End the undo action
    doc.EndUndo()

    # Update the document
    c4d.EventAdd()

if __name__=='__main__':
    toggle_visibility()
