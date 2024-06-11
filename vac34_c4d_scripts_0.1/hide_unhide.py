import c4d

def toggle_visibility():
    # Get the active document
    doc = c4d.documents.GetActiveDocument()
    
    # Get the selected object
    obj = doc.GetActiveObject()
    if not obj:
        print("No object selected.")
        return

    # Start an undo action
    doc.StartUndo()
    
    # Register undo for visibility change
    doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)

    # Get the current state of visibility in the viewport and renderer
    renderVisibility = obj[c4d.ID_BASEOBJECT_VISIBILITY_RENDER]
    editorVisibility = obj[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR]
    
    # Calculate the new visibility state
    # Visibility states: 0 - default, 1 - invisible, 2 - visible
    newRenderVisibility = 1 if renderVisibility != 1 else 2
    newEditorVisibility = 1 if editorVisibility != 1 else 2
    
    # Apply the new visibility state to the object
    obj[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = newRenderVisibility
    obj[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = newEditorVisibility

    # End the undo action
    doc.EndUndo()

    # Update the document
    c4d.EventAdd()

if __name__=='__main__':
    toggle_visibility()
