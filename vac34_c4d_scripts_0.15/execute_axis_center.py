import c4d

def center_object_axis(doc, obj):
    """Центрирует ось выбранного объекта с поддержкой Undo."""
    if not doc or not obj:
        return False
    
    doc.StartUndo()
    
    try:
        # Добавляем объект в Undo перед изменением
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
        
        # Выполняем команду "Axis Center"
        c4d.CallCommand(1011982)  # Axis Center
        
        return True
    
    except Exception as e:
        print(f"Error centering axis: {e}")
        return False
    
    finally:
        doc.EndUndo()
        c4d.EventAdd()

def main():
    doc = c4d.documents.GetActiveDocument()
    if not doc:
        return
    
    obj = doc.GetActiveObject()
    if not obj:
        c4d.gui.MessageDialog("Please select an object.")
        return
    
    if not center_object_axis(doc, obj):
        c4d.gui.MessageDialog("Failed to center object axis.")

if __name__ == '__main__':
    main()