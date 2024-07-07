import c4d
from c4d import gui

class ColorPickerDialog(gui.GeDialog):
    def CreateLayout(self):
        self.SetTitle("Choose Icon Color")
        
        # Add a color picker field without initial color
        self.AddColorField(1000, c4d.BFH_CENTER, initw=100, inith=30, colorflags=c4d.DR_COLORFIELD_POPUP)
        
        # Set the default color to yellow (RGB: 1.0, 1.0, 0.0)
        initial_color = c4d.Vector(1.0, 1.0, 0.0)
        
        # Set the initial color programmatically
        self.SetColorField(1000, initial_color, 1, 1, c4d.DR_COLORFIELD_ENABLE_COLORWHEEL)
        
        # Add OK button and center it
        self.AddDlgGroup(c4d.DLG_OK)
        self.GroupEnd()
        
        return True

    def Command(self, paramid, msg):
        if paramid == c4d.DLG_OK:
            # Get selected color
            selected_color = self.GetColorField(1000)["color"]
            
            # Get the active document and selected objects
            doc = c4d.documents.GetActiveDocument()
            if doc is None:
                return True
            
            doc.StartUndo()  # Start recording undo
            
            selected_objects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
            
            if not selected_objects:
                gui.MessageDialog("No objects selected.")
                doc.EndUndo()  # End undo recording
                return True
            
            # Iterate over selected objects
            for obj in selected_objects:
                # Store the current state for undo
                doc.AddUndo(c4d.UNDOTYPE_CHANGE_SMALL, obj)
                
                # Set the Icon Color to "Custom"
                obj[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = c4d.ID_BASELIST_ICON_COLORIZE_MODE_CUSTOM
                # Apply the selected color to ID_BASELIST_ICON_COLOR
                obj[c4d.ID_BASELIST_ICON_COLOR] = selected_color
            
            # Update the Cinema 4D scene after processing all objects
            c4d.EventAdd()
            
            doc.EndUndo()  # End undo recording
            
            # Close the dialog window after OK is pressed
            self.Close()
        
        return True

def main():
    dlg = ColorPickerDialog()
    dlg.Open(c4d.DLG_TYPE_MODAL_RESIZEABLE, defaultw=60, defaulth=50)

if __name__=='__main__':
    main()