import c4d

def main():
    # Get the active Cinema 4D document
    doc = c4d.documents.GetActiveDocument()
    
    # Get the selected objects
    selected_objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    
    if selected_objects:
        for obj in selected_objects:
            # Check if the object has a parent
            parent = obj.GetUp()
            if parent:
                # Get the name of the parent
                parent_name = parent.GetName()
                
                # Set the child object's name to the parent's name
                obj.SetName(parent_name)
                
        # Update the Cinema 4D UI to reflect changes
        c4d.EventAdd()
    else:
        print("No objects selected.")

if __name__=='__main__':
    main()
