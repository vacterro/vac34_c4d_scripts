import c4d
from c4d import gui

def update_polygon_selection_tags(doc):
    """
    Updates all selected polygon selection tags in the document.
    
    Args:
        doc (c4d.documents.BaseDocument): The active Cinema 4D document
    """
    if not doc:
        raise ValueError("No active document available")

    updated_count = 0
    selection = doc.GetSelection()
    
    for obj in selection:
        if not obj:
            continue
            
        # Check for polygon selection tag
        if isinstance(obj, c4d.BaseTag) and obj.GetType() == c4d.Tpolygonselection:
            try:
                # Update the polygon selection tag
                c4d.CallButton(obj, c4d.POLYGONSELECTIONTAG_UPDATE)
                updated_count += 1
                print(f"Updated Polygon Selection Tag: {obj.GetName()}")
                
            except Exception as e:
                print(f"Failed to update tag {obj.GetName()}: {str(e)}")
    
    return updated_count

def main():
    doc = c4d.documents.GetActiveDocument()
    if not doc:
        gui.MessageDialog("No active document found")
        return
    
    try:
        doc.StartUndo()
        
        updated_tags = update_polygon_selection_tags(doc)
        
        if updated_tags == 0:
            gui.MessageDialog("No polygon selection tags found in selection")
        else:
            c4d.EventAdd()
            
    except Exception as e:
        gui.MessageDialog(f"Error: {str(e)}")
    finally:
        doc.EndUndo()

if __name__ == '__main__':
    main()