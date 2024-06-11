import c4d
from c4d import gui

# Function to check if a track has keyframes with no changes
def has_unchanged_keyframes(track):
    if track is None:
        return False

    curve = track.GetCurve()
    if curve is None or curve.GetKeyCount() <= 1:
        return True  # Consider tracks with 0 or 1 keyframe as unchanged

    # Get the first key's value to compare with others
    first_key_value = curve.GetKey(0).GetValue()

    # Check if all keyframes have the same value
    for i in range(1, curve.GetKeyCount()):
        if curve.GetKey(i).GetValue() != first_key_value:
            return False

    return True

# Main function to remove unused tracks
def remove_unused_tracks():
    # Get the active object
    obj = doc.GetActiveObject()
    if obj is None:
        gui.MessageDialog('No object selected.')
        return

    # Start undo action
    doc.StartUndo()

    # Iterate through all tracks of the object
    tracks = obj.GetCTracks()
    for track in tracks:
        if has_unchanged_keyframes(track):
            # Add undo command for removing a track
            doc.AddUndo(c4d.UNDOTYPE_DELETE, track)
            # Proper method to remove a track from an object
            track.Remove()

    # End undo action
    doc.EndUndo()

    # Inform Cinema 4D of the changes
    c4d.EventAdd()

if __name__=='__main__':
    remove_unused_tracks()
