import bpy
from utils.blend import viewport, user
from utils import string_ops


def get_constraint_dict():
    """target: [current name, empty reference, constraint type, constraint strength]"""
    constrained_bones = {
        # JAW
        "jaw_master": ["jaw", "FaceEmpty_152", 23,              user.get_user().jaw_master_influence],
        "jaw.L.001": ["jaw.L.001", "FaceEmpty_435", 3,          user.get_user().jaw_sides_influence],
        "jaw.R.001": ["jaw.R.001", "FaceEmpty_215", 3,          user.get_user().jaw_sides_influence],

        # CHIN
        "chin": ["chin", "FaceEmpty_152", 3,                    user.get_user().chin_master_influence],
        "chin.R": ["chin.R", "FaceEmpty_32", 3,                 user.get_user().chin_sides_influence],
        "chin.L": ["chin.L", "FaceEmpty_262", 3,                user.get_user().chin_sides_influence],

        # LIPS
        "lips.R": ["lips.R", "FaceEmpty_61", 3,                 user.get_user().lips_influence],
        "lips.L": ["lips.L", "FaceEmpty_291", 3,                user.get_user().lips_influence],
        "lips.T": ["lips.T", "FaceEmpty_0", 3,                  user.get_user().lips_influence],

        # NOSE
        "nose.L": ["nose.L", "FaceEmpty_437", 3,                user.get_user().nose_influence],
        "nose.L.001": ["nose.L.001", "FaceEmpty_358", 3,        user.get_user().nose_influence],
        "nose.R": ["nose.R", "FaceEmpty_217", 3,                user.get_user().nose_influence],
        "nose.R.001": ["nose.R.001", "FaceEmpty_129", 3,        user.get_user().nose_influence],

        # BROW
        "brow.T.R": ["brow.T.R", "FaceEmpty_143", 3,            user.get_user().brow_sides_influence],
        "brow.T.R.001": ["brow.T.R.001", "FaceEmpty_70", 3,     user.get_user().brow_sides_influence],
        "brow.T.R.003": ["brow.T.R.003", "FaceEmpty_107", 3,    user.get_user().brow_master_influence],
        "brow.B.R": ["brow.B.R", "FaceEmpty_247", 3,            user.get_user().brow_master_influence],
        "brow.B.R.001": ["brow.B.R.001", "FaceEmpty_30", 3,     user.get_user().brow_master_influence],
        "brow.B.R.002": ["brow.B.R.002", "FaceEmpty_27", 3,     user.get_user().brow_master_influence],
        "brow.B.R.003": ["brow.B.R.003", "FaceEmpty_56", 3,     user.get_user().brow_master_influence],

        "brow.T.L": ["brow.T.L", "FaceEmpty_372", 3,            user.get_user().brow_sides_influence],
        "brow.T.L.001": ["brow.T.L.001", "FaceEmpty_300", 3,    user.get_user().brow_sides_influence],
        "brow.T.L.003": ["brow.T.L.003", "FaceEmpty_336", 3,    user.get_user().brow_master_influence],
        "brow.B.L": ["brow.B.L", "FaceEmpty_467", 3,            user.get_user().brow_master_influence],
        "brow.B.L.001": ["brow.B.L.001", "FaceEmpty_260", 3,    user.get_user().brow_master_influence],
        "brow.B.L.002": ["brow.B.L.002", "FaceEmpty_257", 3,    user.get_user().brow_master_influence],
        "brow.B.L.003": ["brow.B.L.003", "FaceEmpty_286", 3,    user.get_user().brow_master_influence],

        # EYES
        "lid.T.R": ["lid.T.R", "FaceEmpty_33", 3,               user.get_user().lid_influence],
        "lid.T.R.001": ["lid.T.R.001", "FaceEmpty_161", 3,      user.get_user().lid_influence],
        "lid.T.R.002": ["lid.T.R.002", "FaceEmpty_159", 3,      user.get_user().lid_influence],
        "lid.T.R.003": ["lid.T.R.003", "FaceEmpty_157", 3,      user.get_user().lid_influence],
        "lid.B.R": ["lid.B.R", "FaceEmpty_133", 3,              user.get_user().lid_influence],
        "lid.B.R.001": ["lid.B.R.001", "FaceEmpty_154", 3,      user.get_user().lid_influence],
        "lid.B.R.002": ["lid.B.R.002", "FaceEmpty_145", 3,      user.get_user().lid_influence],
        "lid.B.R.003": ["lid.B.R.003", "FaceEmpty_163", 3,      user.get_user().lid_influence],

        "lid.B.L": ["lid.B.L", "FaceEmpty_362", 3,              user.get_user().lid_influence],
        "lid.B.L.001": ["lid.B.L.001", "FaceEmpty_381", 3,      user.get_user().lid_influence],
        "lid.B.L.002": ["lid.B.L.002", "FaceEmpty_374", 3,      user.get_user().lid_influence],
        "lid.B.L.003": ["lid.B.L.003", "FaceEmpty_390", 3,      user.get_user().lid_influence],
        "lid.T.L": ["lid.T.L", "FaceEmpty_263", 3,              user.get_user().lid_influence],
        "lid.T.L.001": ["lid.T.L.001", "FaceEmpty_388", 3,      user.get_user().lid_influence],
        "lid.T.L.002": ["lid.T.L.002", "FaceEmpty_386", 3,      user.get_user().lid_influence],
        "lid.T.L.003": ["lid.T.L.003", "FaceEmpty_384", 3,      user.get_user().lid_influence]}

    return constrained_bones


def add_constraint(bone, data):
    constraints = {
        0: "CAMERA_SOLVER",
        1: "FOLLOW_TRACK",
        2: "OBJECT_SOLVER",
        3: "COPY_LOCATION",
        4: "COPY_ROTATION",
        5: "COPY_SCALE",
        6: "COPY_TRANSFORMS",
        7: "LIMIT_DISTANCE",
        8: "LIMIT_LOCATION",
        9: "LIMIT_ROTATION",
        10: "LIMIT_SCALE",
        11: "MAINTAIN_VOLUME",
        12: "TRANSFORM",
        13: "TRANSFORM_CACHE",
        14: "CLAMP_TO",
        15: "DAMPED_TRACK",
        16: "IK",
        17: "LOCKED_TRACK",
        18: "SPLINE_IK",
        19: "STRETCH_TO",
        20: "TRACK_TO",
        21: "ACTION",
        22: "ARMATURE",
        23: "CHILD_OF",
        24: "FLOOR",
        25: "FOLLOW_PATH",
        26: "PIVOT",
        27: "SHRINKWRAP"
    }

    constraint = bone.constraints.new(
        type=constraints[data[2]]
    )
    constraint.target = bpy.data.objects[data[1]]
    constraint.influence = data[3]


def update_constraint(bone, data):
    constraints = {
        0: "CAMERA_SOLVER",
        1: "FOLLOW_TRACK",
        2: "OBJECT_SOLVER",
        3: "COPY_LOCATION",
        4: "COPY_ROTATION",
        5: "COPY_SCALE",
        6: "COPY_TRANSFORMS",
        7: "LIMIT_DISTANCE",
        8: "LIMIT_LOCATION",
        9: "LIMIT_ROTATION",
        10: "LIMIT_SCALE",
        11: "MAINTAIN_VOLUME",
        12: "TRANSFORM",
        13: "TRANSFORM_CACHE",
        14: "CLAMP_TO",
        15: "DAMPED_TRACK",
        16: "IK",
        17: "LOCKED_TRACK",
        18: "SPLINE_IK",
        19: "STRETCH_TO",
        20: "TRACK_TO",
        21: "ACTION",
        22: "ARMATURE",
        23: "CHILD_OF",
        24: "FLOOR",
        25: "FOLLOW_PATH",
        26: "PIVOT",
        27: "SHRINKWRAP"
    }

    for constraint in bone.constraints:
        c_name = string_ops.set_lower_letter_only_string(constraint.name)
        lookup = string_ops.set_lower_letter_only_string(constraints[data[2]])

        # check constraint type
        if c_name == lookup:
            c_target_name = string_ops.set_lower_letter_only_string(constraint.target.name)
            # todo: faceempty str should be anywhere, not here..
            # check constraint target before resetting influence
            if c_target_name == "faceempty":
                constraint.influence = data[3]


def add(arm):
    bones = arm.pose.bones
    for bone in bones:
        try:
            data = get_constraint_dict()[bone.name]
            add_constraint(bone, data)

        except KeyError:
            pass


def update(arm):
    viewport.set_pose_mode()
    bones = arm.pose.bones
    for bone in bones:
        try:
            data = get_constraint_dict()[bone.name]
            update_constraint(bone, data)

        except KeyError:
            pass
    viewport.set_object_mode()
