import c4d
from c4d import gui

class ColorPickerDialog(gui.GeDialog):
    """Dialog for selecting icon color for Cinema 4D objects"""
    
    COLOR_FIELD_ID = 1000
    DEFAULT_COLOR = c4d.Vector(1.0, 1.0, 0.0)  # Default yellow color
    
    def CreateLayout(self):
        """Create dialog interface"""
        self.SetTitle("Choose Icon Color")
        
        # Add color picker field
        self.AddColorField(
            self.COLOR_FIELD_ID, 
            c4d.BFH_CENTER, 
            initw=100, 
            inith=30, 
            colorflags=c4d.DR_COLORFIELD_POPUP
        )
        
        # Set default color
        self.SetColorField(
            self.COLOR_FIELD_ID, 
            self.DEFAULT_COLOR, 
            1, 1, 
            c4d.DR_COLORFIELD_ENABLE_COLORWHEEL
        )
        
        # Add OK/Cancel buttons
        self.AddDlgGroup(c4d.DLG_OK | c4d.DLG_CANCEL)
        
        return True
    
    def Command(self, paramid, msg):
        """Handle dialog commands"""
        if paramid == c4d.DLG_OK:
            self._apply_color_to_objects()
            self.Close()
        elif paramid == c4d.DLG_CANCEL:
            self.Close()
        
        return True
    
    def _apply_color_to_objects(self):
        """Apply selected color to objects"""
        # Get active document
        doc = c4d.documents.GetActiveDocument()
        if not doc:
            gui.MessageDialog("Error: No active document.")
            return
        
        # Get selected objects
        selected_objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
        if not selected_objects:
            gui.MessageDialog("No objects selected.")
            return
        
        # Get selected color
        color_data = self.GetColorField(self.COLOR_FIELD_ID)
        if not color_data or "color" not in color_data:
            gui.MessageDialog("Error getting color.")
            return
        
        selected_color = color_data["color"]
        
        # Start undo recording
        doc.StartUndo()
        
        try:
            # Apply color to all selected objects
            for obj in selected_objects:
                if obj:  # Validate object
                    # Register object change for undo
                    doc.AddUndo(c4d.UNDOTYPE_CHANGE_SMALL, obj)
                    
                    # Set custom icon color mode
                    obj[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = c4d.ID_BASELIST_ICON_COLORIZE_MODE_CUSTOM
                    
                    # Apply selected color
                    obj[c4d.ID_BASELIST_ICON_COLOR] = selected_color
            
            # Update scene
            c4d.EventAdd()
            
        except Exception as e:
            gui.MessageDialog(f"Error applying color: {str(e)}")
        
        finally:
            # End undo recording
            doc.EndUndo()


def main():
    """Main function to launch dialog"""
    # Check for active document
    doc = c4d.documents.GetActiveDocument()
    if not doc:
        gui.MessageDialog("Error: No active document.")
        return
    
    # Create and open dialog
    dialog = ColorPickerDialog()
    dialog.Open(
        c4d.DLG_TYPE_MODAL_RESIZEABLE, 
        defaultw=250, 
        defaulth=120
    )


if __name__ == '__main__':
    main()