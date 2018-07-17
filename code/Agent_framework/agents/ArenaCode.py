import cozmo
import Agent
import time
import asyncio

global robot
global homeBase
global enemyBase
global assignedNumber
global enemyNumber

homeBase = 99
enemyBase = 98
assignedNumber = 1
enemyNumber = 2
robot = cozmo.robot.Robot

'''''
robot: cozmo.robot.Robot
self, evt, **kwargs
'''''

class ArenaCode(self, evt, **kwargs):
    gameInProgress =  True

    while gameInProgress == True:

        cozmo.connect(self.run_cozmo)

        def on_new_camera_image(self, event, *, image: cozmo.world.CameraImage, **kw):
            raw_image = image.raw_image
            self.img2 = cv2.cvtColor(np.array(raw_image), cv2.COLOR_RGB2BGR)
            self.check_image()

        async def set_up_cozmo(self, coz_conn):
            self._robot = await coz_conn.wait_for_robot()
            self._robot.camera.image_stream_enabled = True
            self._robot.add_event_handler(cozmo.world.EvtNewCameraImage, self.on_new_camera_image)
            self._robot.set_head_angle(cozmo.util.Angle(degrees=0))
            return 1

        async def run_cozmo(self, coz_conn):
            await self.set_up_cozmo(coz_conn)
            while True:
                await asyncio.sleep(0)

        look_around = robot.start_behavior(cozmo.behavior.BehaviorTypes.LookAroundInPlace)

        # try to find a block
        cube = None

        try:
            cube = robot.world.wait_for_observed_light_cube(timeout=30)
            print("Found cube", cube)

        except asyncio.TimeoutError:
            print("Didn't find a cube :-(")

        finally:
            # whether we find it or not, we want to stop the behavior
            look_around.stop()

        if cube is None:
            robot.play_anim_trigger(cozmo.anim.Triggers.MajorFail)



        if cube is not None:
            robot.pickup_object(self, )

        print("Yay, found cube")

        robot.turn_in_place(degrees(90)).wait_for_completed()

        action = robot.place_object_on_ground_here(cube)
        print("got action", action)
        result = action.wait_for_completed(timeout=30)
        print("got action result", result)



    robot.drive_wheels(50)



cozmo.run_program(ArenaCode)


