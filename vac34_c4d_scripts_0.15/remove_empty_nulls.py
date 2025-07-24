import c4d

def remove_empty_nulls(doc):
    def is_empty_null(obj):
        return obj.GetType() == c4d.Onull and not obj.GetDown()

    def clean_hierarchy(obj):
        while obj:
            next_obj = obj.GetNext()
            if obj.GetDown():
                clean_hierarchy(obj.GetDown())  # Recursively clean children first
            if is_empty_null(obj):
                obj.Remove()  # Remove the null if it's empty
            obj = next_obj

    def iterate_objects(op):
        while op:
            next_obj = op.GetNext()
            clean_hierarchy(op)
            op = next_obj

    # Start by iterating over all objects in the document
    iterate_objects(doc.GetFirstObject())
    
    # Update Cinema 4D to reflect the changes
    c4d.EventAdd()

if __name__ == '__main__':
    doc = c4d.documents.GetActiveDocument()  # Get the active document
    remove_empty_nulls(doc)  # Remove empty nulls
