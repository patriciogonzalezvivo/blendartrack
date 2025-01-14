import rigify
from ....utils.blend import data, objects, scene


# Todo: generate at other rig pos!!!
def generate(metarig):
    objects.deselect_all()
    data.purge_orphan_data()

    context = scene.get_context()
    scene.set_cursor_location(metarig.location)

    if metarig is not None:
        metarig.select_set(True)
        rigify.generate.generate_rig(context, metarig)
