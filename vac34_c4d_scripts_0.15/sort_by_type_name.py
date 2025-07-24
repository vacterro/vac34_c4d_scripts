import c4d
from c4d import gui

def sort_children_by_type_and_name(parent_obj, ignore_types=False):
    """
    Сортирует дочерние объекты по типу и имени (или только по имени)
    """
    if not parent_obj:
        return
    
    # Получаем всех детей
    children = []
    child = parent_obj.GetDown()
    while child:
        children.append(child)
        child = child.GetNext()
    
    if not children:
        return
    
    # Функция для получения ключа сортировки
    def get_sort_key(obj):
        if ignore_types:
            return (obj.GetName().lower(),)
        
        # Актуальные идентификаторы типов объектов
        type_order = {
            # Генераторы
            5100: 0,  # Cube
            5118: 0,  # Sphere
            5124: 0,  # Plane
            5178: 0,  # Spline
            
            # Деформеры
            1018544: 1,  # Bend
            1018545: 1,  # Bulge
            1018546: 1,  # Shear
            
            # SDS
            1028089: 2,  # Subdivision Surface
            
            # Полигональные объекты
            5140: 3,  # Polygon
            
            # Нулевые объекты
            5142: 4,  # Null
            
            # Источники света
            5101: 5,  # Light
            
            # Камеры
            5103: 6,  # Camera
            
            # Инстансы
            5126: 7,  # Instance
        }
        return (type_order.get(obj.GetType(), 999), obj.GetName().lower())
    
    # Сортируем детей
    sorted_children = sorted(children, key=get_sort_key)
    
    # Перестраиваем иерархию
    doc = parent_obj.GetDocument()
    doc.StartUndo()
    
    try:
        for child in children:
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, child)
            child.Remove()
        
        prev_child = None
        for child in sorted_children:
            doc.AddUndo(c4d.UNDOTYPE_CHANGE, child)
            child.InsertUnder(parent_obj)
            if prev_child:
                child.InsertAfter(prev_child)
            prev_child = child
            
    finally:
        doc.EndUndo()
        c4d.EventAdd()

def main():
    # Проверяем нажатие Shift
    bc = c4d.BaseContainer()
    shift_pressed = c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, c4d.KEY_SHIFT, bc) and bc[c4d.BFM_INPUT_VALUE]
    
    doc = c4d.documents.GetActiveDocument()
    if not doc:
        return
    
    selected_objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    if not selected_objects:
        gui.MessageDialog("Выберите родительский объект")
        return
    
    for obj in selected_objects:
        sort_children_by_type_and_name(obj, ignore_types=shift_pressed)
    
    c4d.EventAdd()

if __name__ == '__main__':
    main()