import c4d

def main():
    # Get the active document
    doc = c4d.documents.GetActiveDocument()
    
    # Ensure the document is active and available
    if not doc:
        return
    
    # Get the current selection
    selection = doc.GetSelection()
    
    for obj in selection:
        # Check if the selected object is a tag and specifically a Polygon Selection Tag
        if isinstance(obj, c4d.BaseTag) and obj.GetType() == c4d.Tpolygonselection:
            print("Polygon Selection Tag is selected, updating...")
            
            # Execute the Update action for the Polygon Selection Tag
            c4d.CallButton(obj, c4d.POLYGONSELECTIONTAG_UPDATE)
            
            # It's often necessary to update the scene after making changes
            c4d.EventAdd()
            
            break  # Assuming you only want to execute once for the first found selection

# Execute main function
if __name__=='__main__':
    main()
