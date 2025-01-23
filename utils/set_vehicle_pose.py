import carla
import math

client = carla.Client('localhost', 1403)

world = client.get_world()
spawn_points = world.get_map().get_spawn_points()

actor_list = world.get_actors()

vehicle = actor_list.filter('*volkswagen.t2_2021*')

vehicle = vehicle[0]

vehicle.set_transform(carla.Transform(carla.Location(x=3.047784, y=130.209518, z=-0.000458), carla.Rotation(pitch=0.000676, yaw=-179.647827, roll=0.000146)))

