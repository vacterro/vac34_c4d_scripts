import c4d

def main():
    doc = c4d.documents.GetActiveDocument()
    selected_objs = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_SELECTIONORDER)

    if not selected_objs:
        print("No objects selected. Please select one or more objects.")
        return

    # Проверка нажатия Shift
    bc = c4d.BaseContainer()
    shift_pressed = c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, c4d.KEY_SHIFT, bc) and bc.GetInt32(c4d.BFM_INPUT_VALUE)

    doc.StartUndo()
    try:
        shared_null = None

        if shift_pressed:
            # Общая позиция
            avg_pos = c4d.Vector()
            for obj in selected_objs:
                avg_pos += obj.GetMg().off
            avg_pos /= len(selected_objs)

            shared_null = c4d.BaseObject(c4d.Onull)
            shared_null.SetName("Shared_Target")
            shared_null.SetAbsPos(avg_pos)

            doc.AddUndo(c4d.UNDOTYPE_NEW, shared_null)
            doc.InsertObject(shared_null)

        for obj in selected_objs:
            if shift_pressed:
                target_null = shared_null
            else:
                target_null = c4d.BaseObject(c4d.Onull)
                target_null.SetName(f"{obj.GetName()}_target")
                target_null.SetAbsPos(obj.GetMg().off)

                doc.AddUndo(c4d.UNDOTYPE_NEW, target_null)
                doc.InsertObject(target_null)

            # Сохраняем изменение объекта до модификации
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)

            # Добавляем Target Tag
            target_tag = obj.MakeTag(c4d.Ttargetexpression)
            if not target_tag:
                print(f"Failed to create Target Tag for {obj.GetName()}")
                continue

            doc.AddUndo(c4d.UNDOTYPE_NEW, target_tag)
            target_tag[c4d.TARGETEXPRESSIONTAG_LINK] = target_null

    finally:
        doc.EndUndo()
        c4d.EventAdd()

# Запуск
if __name__ == '__main__':
    main()
