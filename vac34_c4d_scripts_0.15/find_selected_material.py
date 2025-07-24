import c4d
from c4d import gui

# Function to get the full hierarchy path of an object
def get_full_hierarchy_path(obj):
    path = obj.GetName()
    parent = obj.GetUp()
    while parent:
        path = parent.GetName() + " -> " + path
        parent = parent.GetUp()
    return path

# Recursive function to iterate through all objects in the scene
def get_objects(obj, selected_material, assigned_objects_paths, objects_to_select):
    while obj:
        # Check if the object has any texture tags
        tags = obj.GetTags()
        for tag in tags:
            if isinstance(tag, c4d.TextureTag) and tag.GetMaterial() == selected_material:
                # Get the full hierarchy path of the object
                full_path = get_full_hierarchy_path(obj)
                assigned_objects_paths.append(full_path)
                # Add the object to the selection list
                objects_to_select.append(obj)

        # Recursively check children
        get_objects(obj.GetDown(), selected_material, assigned_objects_paths, objects_to_select)

        # Move to next object
        obj = obj.GetNext()

class MaterialDialog(gui.GeDialog):
    def __init__(self, title, message):
        self.message = message
        self.title = title

        # Dynamically calculate the dialog height based on the number of lines in the message
        line_count = self.message.count("\n") + 1
        base_height = 60  # Base height for the dialog (title + button space)
        line_height = 16   # Adjusted line height slightly to prevent cropping
        padding = 0      # Added padding to ensure no cropping at the bottom
        max_height = 700   # Maximum dialog height

        # Dynamically calculate the dialog width based on the longest line
        longest_line_length = max(len(line) for line in self.message.splitlines())
        char_width = 8     # Estimated character width in pixels
        base_width = 0   # Base width (for dialog padding)
        max_width = 1000   # Maximum dialog width

        # Dialog height will be at least enough for a few lines but no more than max_height
        self.dialog_height = min(max_height, base_height + line_count * line_height + padding)

        # Dialog width will be based on the longest line but no more than max_width
        self.dialog_width = min(max_width, base_width + longest_line_length * char_width)

    def CreateLayout(self):
        # Add a title for the dialog using the material name
        self.SetTitle(self.title)

        # Add a multi-line edit box without a scroll group, to avoid the empty space issue
        self.AddMultiLineEditText(1001, c4d.BFH_SCALEFIT | c4d.BFV_SCALEFIT, style=c4d.DR_MULTILINE_READONLY)
        self.SetString(1001, self.message)  # Set the message text

        # Add an "OK" button to close the dialog
        self.AddButton(1002, c4d.BFH_CENTER, 0, 0, "OK")

        return True

    def InitValues(self):
        return True

    def Command(self, id, msg):
        # Handle "OK" button press (closing the dialog)
        if id == 1002:  # ID for the OK button
            self.Close()  # Close the dialog
        return True

    def openCentered(self):
        # Get the screen dimensions, third argument is whole_screen (True means get the full screen dimensions)
        screen_dimensions = c4d.gui.GeGetScreenDimensions(0, 0, True)

        screen_width = screen_dimensions['sx2']
        screen_height = screen_dimensions['sy2']

        # Calculate center position
        xpos = (screen_width - self.dialog_width) // 2
        ypos = (screen_height - self.dialog_height) // 2

        # Open the dialog at the calculated position
        self.Open(c4d.DLG_TYPE_MODAL, xpos=xpos, ypos=ypos, defaultw=self.dialog_width, defaulth=self.dialog_height)

def main():
    # Get the active document
    doc = c4d.documents.GetActiveDocument()

    # Get the selected material in the Material Manager
    selection = doc.GetActiveMaterials()

    if not selection:
        gui.MessageDialog("No material selected.")
        return

    selected_material = selection[0]  # Taking the first selected material
    result_message = ""  # Remove the material name, leave just the object paths

    # Get all objects in the scene
    obj = doc.GetFirstObject()

    # List to store hierarchy paths of objects assigned with the selected material
    assigned_objects_paths = []
    objects_to_select = []

    # Start the recursive object search
    get_objects(obj, selected_material, assigned_objects_paths, objects_to_select)

    # Prepare the result message with full hierarchy paths
    if assigned_objects_paths:
        for i, path in enumerate(assigned_objects_paths, 1):  # Numbering the paths
            result_message += f"{i}. {path}\n"
    else:
        result_message += "No objects assigned to the selected material."

    # Check if Shift key is held
    bc = c4d.BaseContainer()
    is_shift_pressed = c4d.gui.GetInputState(c4d.BFM_INPUT_KEYBOARD, c4d.KEY_SHIFT, bc) and bc[c4d.BFM_INPUT_VALUE]

    if is_shift_pressed:
        # Select the objects in Object Manager
        doc.StartUndo()
        for obj in objects_to_select:
            doc.AddUndo(c4d.UNDOTYPE_BITS, obj)
            obj.SetBit(c4d.BIT_ACTIVE)  # Activate object
        doc.EndUndo()
        c4d.EventAdd()  # Update the scene

    # Show the result in a scrollable dialog with dynamic width and height
    dlg = MaterialDialog(selected_material.GetName(), result_message)
    
    # Ensure the window is centered
    dlg.openCentered()  # Open centered dialog

# Execute the script
if __name__ == '__main__':
    main()
