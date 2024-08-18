import random
import time
from values import MAX_REST_SECONDS, JUMP_MAX_DISTANCE

class Hare:
    def __init__(self, _id):
        self.id = _id
        self.id_normalized = _id[:20] if len(_id) > 20 else _id.ljust(20)
        self.track_distance = 0
        self.jumps = 0

    def jump(self):
        distance = random.uniform(1, JUMP_MAX_DISTANCE)
        self.track_distance += distance
        self.jumps += 1
        return distance

    def rest(self):
        seconds = random.uniform(0, MAX_REST_SECONDS)
        time.sleep(seconds)
        return seconds


