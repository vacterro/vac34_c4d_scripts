import c4d

def main():
    # Get the active object
    obj = doc.GetActiveObject()
    
    if obj is not None:
        # Create a new undo group
        doc.StartUndo()
        
        # Execute Axis Center command
        c4d.CallCommand(1011982) # This is the command ID for Axis Center
        
        # Add the object to the undo queue
        doc.AddUndo(c4d.UNDOTYPE_CHANGE, obj)
        
        # Update the scene
        c4d.EventAdd()
        
        # End the undo group
        doc.EndUndo()
    else:
        print("Please select an object.")

# Execute the main function
if __name__=='__main__':
    main()
