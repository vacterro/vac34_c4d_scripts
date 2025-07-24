import c4d

def main():
    doc = c4d.documents.GetActiveDocument()
    if doc is None:
        return

    selected_object = doc.GetActiveObject()
    if selected_object is None:
        return

    first_child = selected_object.GetDown()
    if first_child is None:
        return

    doc.StartUndo()
    try:
        # Сохраняем undo на изменение родителя
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, selected_object)

        new_name = first_child.GetName()
        selected_object.SetName(new_name)
    finally:
        doc.EndUndo()
        c4d.EventAdd()

if __name__ == '__main__':
    main()
