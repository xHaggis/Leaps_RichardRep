import cozmo
import Agent
import time

global robot
robot = cozmo.robot.Robot

def ArenaCode(evt, **kwargs):
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
        return

    if cube is not None:
        robot.pickup_object(self,)

    print("Yay, found cube")

    cube.set_lights(cozmo.lights.green_light.flash())

    anim = robot.play_anim_trigger(cozmo.anim.Triggers.BlockReact)
    anim.wait_for_completed()

    action = robot.pickup_object(cube)
    print("got action", action)
    result = action.wait_for_completed(timeout=30)
    print("got action result", result)

    robot.turn_in_place(degrees(90)).wait_for_completed()

    action = robot.place_object_on_ground_here(cube)
    print("got action", action)
    result = action.wait_for_completed(timeout=30)
    print("got action result", result)

    anim = robot.play_anim_trigger(cozmo.anim.Triggers.MajorWin)
    cube.set_light_corners(None, None, None, None)
    anim.wait_for_completed()


cozmo.run_program(ArenaCode)
