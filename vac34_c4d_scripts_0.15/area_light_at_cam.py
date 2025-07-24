import c4d
from c4d import gui

def main():
    doc = c4d.documents.GetActiveDocument()
    if doc is None:
        return

    doc.StartUndo()

    try:
        # Снятие выделения вручную с Undo
        selected_objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_0)
        for obj in selected_objects:
            doc.AddUndo(c4d.UNDOTYPE_BITS, obj)
            obj.DelBit(c4d.BIT_ACTIVE)

        c4d.EventAdd()

        # Сохраняем список объектов до создания света
        objects_before = set(doc.GetObjects())

        # Команда создания Redshift Area Light
        c4d.CallCommand(1038672)  # Убедись, что ID верен

        # Список после
        objects_after = set(doc.GetObjects())
        new_objects = list(objects_after - objects_before)

        if not new_objects:
            gui.MessageDialog('Redshift Area Light was not created. Check the command ID.')
            return

        new_light = new_objects[-1]
        doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, new_light)

        # Уникальное имя
        highest_num = 0
        for obj in doc.GetObjects():
            if obj.GetName().startswith("area_light_"):
                try:
                    num = int(obj.GetName().split("_")[-1])
                    highest_num = max(highest_num, num)
                except ValueError:
                    pass

        new_name = f"area_light_{highest_num + 1}"
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, new_light)
        new_light.SetName(new_name)

        # Камера
        bd = doc.GetActiveBaseDraw()
        cam = bd.GetSceneCamera(doc) or bd.GetEditorCamera()
        if not cam:
            gui.MessageDialog('Active camera not found!')
            return

        doc.AddUndo(c4d.UNDOTYPE_CHANGE, new_light)
        new_light.SetMg(cam.GetMg())

    finally:
        doc.EndUndo()
        c4d.EventAdd()

if __name__ == '__main__':
    main()
