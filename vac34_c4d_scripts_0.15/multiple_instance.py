import c4d

def main():
    # Get the active document
    doc = c4d.documents.GetActiveDocument()
    if not doc:
        return

    # Get selected objects
    selected_objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    if not selected_objects:
        return

    # Ensure we have at least one reference object and one target object
    if len(selected_objects) < 2:
        print("Select at least one reference object and one target object.")
        return

    # The first selected object is the reference object
    reference_object = selected_objects[0]

    # Start undo recording
    doc.StartUndo()

    # Create an Instance object for each subsequent selected object
    instances = []
    for obj in selected_objects[1:]:
        # Save the coordinates of the original object
        obj_matrix = obj.GetMg()

        # Create instance
        instance = c4d.BaseObject(c4d.Oinstance)
        instance[c4d.INSTANCEOBJECT_LINK] = reference_object
        instance[c4d.INSTANCEOBJECT_RENDERINSTANCE_MODE] = 1  # Render Instance mode
        instance.SetName(obj.GetName())  # Set instance name to original object name

        # Insert the instance at the same hierarchy level and position as the original object
        doc.InsertObject(instance, parent=obj.GetUp(), pred=obj.GetPred(), checknames=True)

        # Set the instance's coordinates to the original object's coordinates
        instance.SetMg(obj_matrix)

        # Add undo steps
        doc.AddUndo(c4d.UNDOTYPE_NEW, instance)
        doc.AddUndo(c4d.UNDOTYPE_DELETE, obj)

        # Remove original object from the scene
        obj.Remove()

        instances.append(instance)

    # Select all created instances
    for instance in instances:
        doc.SetActiveObject(instance, c4d.SELECTION_ADD)

    # End undo recording
    doc.EndUndo()

    # Update the scene
    c4d.EventAdd()

# Execute main()
if __name__ == '__main__':
    main()
