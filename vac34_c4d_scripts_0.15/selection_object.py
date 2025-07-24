import c4d

def find_last_object(obj):
    """
    Finds the last object in the hierarchy under the given object.
    
    Args:
        obj (c4d.BaseObject): The starting object
        
    Returns:
        c4d.BaseObject: The deepest child object in the hierarchy
    """
    if not obj:
        return None
        
    while obj.GetDown():
        obj = obj.GetDown()
    return obj

def create_selection_object(doc):
    """
    Creates a selection object and returns it.
    
    Args:
        doc (c4d.documents.BaseDocument): The active document
        
    Returns:
        c4d.BaseObject: The created selection object or None
    """
    try:
        # Call the "Create Selection Object" command
        c4d.CallCommand(69000, 917)  # Create Selection Object
        return find_last_object(doc.GetFirstObject())
    except:
        return None

def process_selection_object(doc, selection_object, last_selected):
    """
    Processes the selection object by renaming and repositioning it.
    
    Args:
        doc (c4d.documents.BaseDocument): The active document
        selection_object (c4d.BaseObject): The selection object to process
        last_selected (c4d.BaseObject): The last selected object
    """
    if not selection_object or not last_selected or selection_object == last_selected:
        return

    # Rename the Selection Object
    new_name = f"{last_selected.GetName()} Selection"
    doc.AddUndo(c4d.UNDOTYPE_CHANGE, selection_object)
    selection_object.SetName(new_name)

    # Reposition the Selection Object at the top
    doc.AddUndo(c4d.UNDOTYPE_CHANGE, selection_object)
    selection_object.Remove()
    doc.InsertObject(selection_object, None, None)

def main():
    doc = c4d.documents.GetActiveDocument()
    if not doc:
        return

    doc.StartUndo()
    try:
        # Get the last selected object
        selection = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_SELECTIONORDER)
        last_selected = selection[-1] if selection else None

        # Create selection object
        selection_object = create_selection_object(doc)
        
        # Process the selection object
        if selection_object:
            process_selection_object(doc, selection_object, last_selected)

    except Exception as e:
        c4d.gui.MessageDialog(f"Error: {str(e)}")
    finally:
        doc.EndUndo()
        c4d.EventAdd()

if __name__ == '__main__':
    main()