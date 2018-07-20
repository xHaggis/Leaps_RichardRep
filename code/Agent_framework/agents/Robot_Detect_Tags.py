import asyncio
import cozmo
import cv2
import numpy as np
import time

from cozmo.util import degrees, distance_mm, speed_mmps



class RobotDetectsTags:
    def __init__(self):
        super(RobotDetectsTags, self).__init__()
        self._robot = None
        self._tk_root = 0
        self._tk_label_input = 0
        self.is_moving = False
        self.img1 = None  # trainImage
        self.sift = cv2.xfeatures2d.SIFT_create()
        self.index_params = dict(algorithm=0, trees=5)
        self.search_params = dict(checks=50)
        self.flann = cv2.FlannBasedMatcher(self.index_params, self.search_params)
        self.img2 = None
        self.match_found = False
        self.image = ''
        self.own_objects = 2
        self.home_base = '6'
        self.opponent_home_base = '7'
        self.south_wall = '3'
        self.north_wall = '1'
        self.east_wall = '4'
        self.west_wall = '2'
        self.inner_box_wall_north = '12'
        self.inner_box_wall_west = '9'
        self.inner_box_wall_south = '10'
        self.outer_box_wall_north = '13'
        self.outer_box_wall_west = '8'
        self.outer_box_wall_south = '11'
        self.special_zone = '5'

        cozmo.connect(self.run_cozmo)

    def on_new_camera_image(self, event, *, image: cozmo.world.CameraImage, **kw):
        time.sleep(2)
        raw_image = image.raw_image
        self.img2 = cv2.cvtColor(np.array(raw_image), cv2.COLOR_RGB2BGR)
        self.check_image()

    async def set_up_cozmo(self, coz_conn):
        self._robot = await coz_conn.wait_for_robot()
        self._robot.camera.image_stream_enabled = True
        self._robot.add_event_handler(cozmo.world.EvtNewCameraImage, self.on_new_camera_image)
        self._robot.add_event_handler(cozmo.robot.objects.EvtObjectObserved,self.objectObserved)
        self._robot.set_head_angle(cozmo.util.Angle(degrees=0))
        return 1

    async def run_cozmo(self, coz_conn):
        await self.set_up_cozmo(coz_conn)
        while True:
            await asyncio.sleep(0)

    def return_home(self):
        self.check_image()

    def check_image(self):
        TurnedOnce = False
        image_list = list(range(1, 15))
        i = 0
        self.match_found = False
        while self.match_found is False and i < len(image_list):

            self.match(image_list[i])
            i += 1
        if self.match_found is True:
            a = str(image_list[i-1])
            print('Image is', image_list[i-1])
            if str(image_list[i-1]) == self.opponent_home_base:
                print('Opponent home base')
                self._robot.turn_in_place(degrees(180)).wait_for_completed()
                self._robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
            if str(image_list[i - 1]) == self.home_base:
                print('Home base')
                self._robot.turn_in_place(degrees(180)).wait_for_completed()
                self._robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
            if a == self.north_wall or a == self.south_wall or a == self.east_wall or a == self.west_wall:
                print('Wall')
                self._robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
                self._robot.turn_in_place(degrees(90)).wait_for_completed()
                # do stuff
            if a == self.inner_box_wall_north or a == self.inner_box_wall_south or a == self.inner_box_wall_west:
                print("I'm inside the box")
                if TurnedOnce == True:
                    self._robot.turn_in_place(degrees(325)).wait_for_completed()
                else:
                    self._robot.turn_in_place(degrees(325)).wait_for_completed()
                    TurnedOnce = True
            if a == self.outer_box_wall_north or a == self.outer_box_wall_south or a == self.outer_box_wall_west:
                print('I see the box')
                self._robot.turn_in_place(degrees(90)).wait_for_completed()
                self._robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
            if a == self.special_zone:
                print('Special zone')
                self._robot.turn_in_place(degrees(90)).wait_for_completed()
                self._robot.drive_straight(distance_mm(150), speed_mmps(50)).wait_for_completed()
        else:
            print('image not found')

    def match(self, image_number):
        self.img1 = cv2.imread('Selection/' + str(image_number) + '.png', 0)
        self.kp1, self.des1 = self.sift.detectAndCompute(self.img1, None)
        min_match_count = 10

        # Feature Recognition
        kp2, des2 = self.sift.detectAndCompute(self.img2, None)
        matches = self.flann.knnMatch(self.des1, des2, k=2)

        good = []
        for m, n in matches:
            if m.distance < 0.7*n.distance:
                good.append(m)
                if len(good) > min_match_count:
                    src_pts = np.float32([self.kp1[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
                    dst_pts = np.float32([kp2[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
                    m, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
                    h, w = self.img1.shape
                    pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
                    dst = cv2.perspectiveTransform(pts, m)
                    self.img2 = cv2.polylines(self.img2, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
                    self.match_found = True
        # print(str(image_number) + '  matches : ', len(good))

'''
    def objectObserved(self, event, **kwargs):
        cubePickedUp = False

        if event.obj.object_id == self.own_objects:
            self._robot.pickup_object(event.obj, num_retries=3).wait_for_completed()
            cubePickedUp = True

        while cubePickedUp == True:
            self.check_image()

            if self.match_found == True:
'''







if __name__ == '__main__':
    RobotDetectsTags()
