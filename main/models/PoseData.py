from main.helper import KeyframeAssistent, JsonDecoder
import importlib
importlib.reload(KeyframeAssistent)
importlib.reload(JsonDecoder)


class PoseData:
    def __init__(self, px, py, pz, rx, ry, rz, frame):
        # assign pos
        self.px = px
        self.py = py
        self.pz = pz
        # assign rotation_euler
        self.rx = rx
        self.ry = ry
        self.rz = rz
        # assign frame
        self.frame = frame

    def init_frame(self, scene):
        KeyframeAssistent.init_keyframe(self.frame, scene)

    def key_pos(self, obj):
        KeyframeAssistent.set_pos_keyframe(self.px, self.py, self.pz, obj)

    def key_rot(self, obj):
        KeyframeAssistent.set_rot_keyframe(self.rx, self.ry, self.rz, obj)

    def print_content(self):
        print('px', self.px, 'py', self.py, 'pz', self.pz, 'rx', self.rx, 'ry', self.ry, 'rz', self.rz, 'f', self.frame)


def init_pose_model(json_data):
    # array to store pose data
    pose_model = []
    # decoding json
    for data in json_data['poseList']:
        px, py, pz = JsonDecoder.split_pos_data(data)
        rx, ry, rz = JsonDecoder.split_rot_data(data)
        frame = (data['frame'])
        # append data to list
        tmp = PoseData(px, py, pz, rx, ry, rz, frame)
        pose_model.append(tmp)
    return pose_model
