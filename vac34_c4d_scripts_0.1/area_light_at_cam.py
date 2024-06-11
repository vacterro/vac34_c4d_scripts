import c4d
from c4d import gui

def main():
    doc = c4d.documents.GetActiveDocument()
    doc.StartUndo()

    # Save the current state of the document's objects to find the new object later
    objects_before = [obj for obj in doc.GetObjects()]

    # Assuming 1038672 is the command ID for creating a Redshift Area Light
    c4d.CallCommand(1038672)  # This command creates the Redshift Area Light
    
    # Find the new object by comparing the state before and after the command
    objects_after = [obj for obj in doc.GetObjects()]
    new_objects = [obj for obj in objects_after if obj not in objects_before]

    if new_objects:
        newLight = new_objects[-1]  # Assuming the last object in the list is the newly created light
        
        # Determine the new name based on existing lights
        highest_num = 0
        for obj in doc.GetObjects():
            if obj.GetName().startswith("area_light_"):
                try:
                    num = int(obj.GetName().split("_")[-1])
                    if num > highest_num:
                        highest_num = num
                except ValueError:
                    pass  # In case the split result can't be converted to int

        new_light_name = f"area_light_{highest_num + 1}"
        newLight.SetName(new_light_name)
        
        # Get the current active camera
        bd = doc.GetActiveBaseDraw()
        activeCamera = bd.GetSceneCamera(doc) if bd.GetSceneCamera(doc) else bd.GetEditorCamera()
        
        if not activeCamera:
            gui.MessageDialog('No active camera found!')
            return
        
        # Set the light's position and rotation to match the camera's
        newLight.SetMg(activeCamera.GetMg())
        
        doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, newLight)
    else:
        gui.MessageDialog('Redshift Area Light was not created. Please check the command ID.')

    doc.EndUndo()
    # Update the scene
    c4d.EventAdd()

if __name__=='__main__':
    main()
