

def perform(obj):

    if obj and obj.img:
        obj.img.delete()
        obj.img = None
        obj.save()

    return obj
