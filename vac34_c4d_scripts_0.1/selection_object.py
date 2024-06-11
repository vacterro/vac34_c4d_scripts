import c4d

def main():
    # Get the active document
    doc = c4d.documents.GetActiveDocument()

    # Start an undo operation
    doc.StartUndo()

    # Store the last selected object for later use
    last_selected = None
    selection = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_SELECTIONORDER)
    if selection:
        last_selected = selection[-1]  # Get the last selected object from the selection

    # Call the "Create Selection Object" command with its specific ID
    c4d.CallCommand(69000, 917)  # Replace these IDs with the correct ones if needed

    # Function to find the last object in the hierarchy under the given object
    def find_last_object(obj):
        while obj.GetDown():
            obj = obj.GetDown()
        return obj

    # Find the actual last object in the document to assume it's the Selection Object
    selection_object = find_last_object(doc.GetFirstObject())

    # Rename and reposition the Selection Object, if valid and applicable
    if selection_object and last_selected and selection_object != last_selected:
        # Rename the Selection Object to inherit the last selected object's name with " Selection" suffix
        selection_object_name = last_selected.GetName() + " Selection"
        selection_object.SetName(selection_object_name)

        # Reposition the Selection Object at the top of the list
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, selection_object)
        selection_object.Remove()  # Remove from current position
        doc.InsertObject(selection_object, None, None)  # Insert at the top

    # End the undo operation
    doc.EndUndo()

    # Make sure to update Cinema 4D to reflect any changes
    c4d.EventAdd()

# Execute the main function
if __name__=='__main__':
    main()
