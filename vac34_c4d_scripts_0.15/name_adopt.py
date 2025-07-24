import c4d

def main():
    doc = c4d.documents.GetActiveDocument()
    selected_objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)

    if not selected_objects:
        print("No objects selected.")
        return

    doc.StartUndo()
    try:
        for obj in selected_objects:
            parent = obj.GetUp()
            if parent:
                # Сохраняем undo на изменение имени
                doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)

                parent_name = parent.GetName()
                obj.SetName(parent_name)
    finally:
        doc.EndUndo()
        c4d.EventAdd()

if __name__ == '__main__':
    main()
