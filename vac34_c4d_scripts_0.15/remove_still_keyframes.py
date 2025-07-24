import c4d
from c4d import gui

def has_unchanged_keyframes(track):
    """
    Checks if a track has keyframes with identical values.
    
    Args:
        track (c4d.CTrack): The track to check
        
    Returns:
        bool: True if all keyframes have the same value, False otherwise
    """
    if not track:
        return False

    curve = track.GetCurve()
    if not curve:
        return True  # No curve means no animation

    key_count = curve.GetKeyCount()
    if key_count <= 1:
        return True  # 0 or 1 keyframe means no variation

    first_value = curve.GetKey(0).GetValue()
    
    # Using any() for more efficient iteration
    return not any(
        curve.GetKey(i).GetValue() != first_value
        for i in range(1, key_count)
    )

def remove_unused_tracks(doc):
    """
    Removes animation tracks with no meaningful keyframe data.
    
    Args:
        doc (c4d.documents.BaseDocument): The active document
    """
    if not doc:
        raise ValueError("No active document")

    obj = doc.GetActiveObject()
    if not obj:
        gui.MessageDialog('No object selected.')
        return

    tracks = obj.GetCTracks()
    if not tracks:
        gui.MessageDialog('No animation tracks found.')
        return

    doc.StartUndo()
    try:
        removed_count = 0
        
        # Work with a list copy to avoid modification during iteration
        for track in list(tracks):
            if has_unchanged_keyframes(track):
                doc.AddUndo(c4d.UNDOTYPE_DELETE, track)
                track.Remove()
                removed_count += 1

        if removed_count == 0:
            gui.MessageDialog('No unchanged tracks found.')
        else:
            gui.MessageDialog(f'Removed {removed_count} unused tracks.')

    except Exception as e:
        gui.MessageDialog(f'Error: {str(e)}')
    finally:
        doc.EndUndo()
        c4d.EventAdd()

def main():
    doc = c4d.documents.GetActiveDocument()
    remove_unused_tracks(doc)

if __name__ == '__main__':
    main()