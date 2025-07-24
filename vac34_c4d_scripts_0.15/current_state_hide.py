import c4d

def create_hide_null(doc):
    """Создает Null-объект 'hide' с отключенной видимостью."""
    hide_null = c4d.BaseObject(c4d.Onull)
    if hide_null is None:
        raise RuntimeError("Failed to create 'hide' null object.")
    
    hide_null.SetName("hide")
    hide_null[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 0  # Видим в редакторе
    hide_null[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = 0  # Видим в рендере
    doc.InsertObject(hide_null)
    doc.AddUndo(c4d.UNDOTYPE_NEW, hide_null)
    return hide_null

def main():
    doc = c4d.documents.GetActiveDocument()
    if not doc:
        return
    
    # Проверяем, зажат ли Shift
    bc = c4d.BaseContainer()
    shift_pressed = (
        c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, c4d.KEY_SHIFT, bc) 
        and bc[c4d.BFM_INPUT_VALUE]
    )
    
    original_object = doc.GetActiveObject()
    if not original_object:
        c4d.gui.MessageDialog("No object selected.")
        return
    
    # Начинаем Undo-блок
    doc.StartUndo()
    
    try:
        # Создаем Current State to Object
        c4d.CallCommand(12233)  # Current State to Object
        new_object = doc.GetActiveObject()
        if not new_object:
            raise RuntimeError("Failed to create Current State object.")
        
        # Если Shift зажат, перемещаем оригинальный объект в null "hide"
        if shift_pressed:
            hide_null = doc.SearchObject("hide")
            if not hide_null:
                hide_null = create_hide_null(doc)
            
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, original_object)
            original_object.Remove()
            original_object.InsertUnder(hide_null)
        
        # Скрываем оригинальный объект и переименовываем
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, original_object)
        original_object[c4d.ID_BASEOBJECT_VISIBILITY_EDITOR] = 1  # Скрыт в редакторе
        original_object[c4d.ID_BASEOBJECT_VISIBILITY_RENDER] = 1  # Скрыт в рендере
        original_object.SetName(f"{original_object.GetName()}_hided")
        original_object.Message(c4d.MSG_UPDATE)
        
        # Выделяем новый объект (и снимаем выделение)
        doc.SetActiveObject(new_object, c4d.SELECTION_NEW)
        doc.SetActiveObject(None)  # Снимаем выделение (опционально)
        
    except Exception as e:
        c4d.gui.MessageDialog(f"Error: {str(e)}")
    finally:
        doc.EndUndo()  # Завершаем Undo-блок
        c4d.EventAdd()  # Обновляем сцену

if __name__ == '__main__':
    main()