import c4d
from c4d import gui

def create_instance_objects(doc, reference_obj, target_objects):
    """
    Creates instance objects for each target object, referencing the reference object.
    
    Args:
        doc (c4d.documents.BaseDocument): The active document
        reference_obj (c4d.BaseObject): The object to instance
        target_objects (list): Objects to replace with instances
        
    Returns:
        list: Created instance objects
    """
    instances = []
    
    for obj in target_objects:
        if not obj:
            continue
            
        # Store original transform and hierarchy info
        obj_matrix = obj.GetMg()
        parent = obj.GetUp()
        pred = obj.GetPred()
        
        try:
            # Create and configure instance
            instance = c4d.BaseObject(c4d.Oinstance)
            if not instance:
                raise RuntimeError("Failed to create instance object")
                
            instance[c4d.INSTANCEOBJECT_LINK] = reference_obj
            instance[c4d.INSTANCEOBJECT_RENDERINSTANCE_MODE] = 1  # Render Instance
            instance.SetName(f"{obj.GetName()}_instance")
            
            # Insert in scene
            doc.InsertObject(instance, parent=parent, pred=pred, checknames=True)
            instance.SetMg(obj_matrix)
            
            # Register undo operations
            doc.AddUndo(c4d.UNDOTYPE_NEW, instance)
            doc.AddUndo(c4d.UNDOTYPE_DELETE, obj)
            
            # Remove original object
            obj.Remove()
            
            instances.append(instance)
            
        except Exception as e:
            print(f"Error processing {obj.GetName()}: {str(e)}")
            
    return instances

def main():
    doc = c4d.documents.GetActiveDocument()
    if not doc:
        gui.MessageDialog("No active document found")
        return

    selected_objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    if not selected_objects:
        gui.MessageDialog("No objects selected")
        return

    if len(selected_objects) < 2:
        gui.MessageDialog("Select at least 1 reference object and 1 target object")
        return

    doc.StartUndo()
    try:
        reference_obj = selected_objects[0]
        target_objects = selected_objects[1:]
        
        instances = create_instance_objects(doc, reference_obj, target_objects)
        
        if instances:
            # Select all created instances
            doc.SetActiveObject(None, c4d.SELECTION_NEW)  # Clear selection first
            for instance in instances:
                doc.SetActiveObject(instance, c4d.SELECTION_ADD)
            
            gui.MessageDialog(f"Created {len(instances)} instance objects")
        else:
            gui.MessageDialog("No instances were created")
            
    except Exception as e:
        gui.MessageDialog(f"Error: {str(e)}")
    finally:
        doc.EndUndo()
        c4d.EventAdd()

if __name__ == '__main__':
    main()