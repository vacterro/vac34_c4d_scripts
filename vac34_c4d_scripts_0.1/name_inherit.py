import c4d

def main():
    # Get the active Cinema 4D document
    doc = c4d.documents.GetActiveDocument()
    if doc is None:
        return

    # Get the selected object in the Object Manager
    selected_object = doc.GetActiveObject()
    if selected_object is None:
        return

    # Get the first child of the selected object
    first_child = selected_object.GetDown()
    if first_child is None:
        return

    # Get the name of the first child and set it as the name of the selected object
    new_name = first_child.GetName()
    selected_object.SetName(new_name)

    # Update the Cinema 4D UI
    c4d.EventAdd()

if __name__=='__main__':
    main()
