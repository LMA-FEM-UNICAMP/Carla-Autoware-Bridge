import carla
import math

client = carla.Client('localhost', 1403)

world = client.get_world()
spawn_points = world.get_map().get_spawn_points()

actor_list = world.get_actors()

vehicle = actor_list.filter('*volkswagen*')

vehicle = actor_list.find(47)


def calculate_sides(hypotenuse, angle):


  # Convert the angle to radians
  angle_radians = math.radians(angle)

  # Calculate the opposite side using the sine function
  opposite_side = hypotenuse * math.sin(angle_radians)

  # Calculate the adjacent side using the cosine function
  adjacent_side = hypotenuse * math.cos(angle_radians)

  return opposite_side, adjacent_side
  
metres_distance = 5

while(1):

  vehicle_transform = vehicle.get_transform()

  spectator = world.get_spectator()
  spectator_pos = carla.Transform(vehicle_transform.location + carla.Location(x=20,y=10,z=4),
                                  carla.Rotation(yaw = vehicle_transform.rotation.yaw -155))
  #spectator.set_transform(spectator_pos)

  vehicle_transform = vehicle.get_transform()
  y,x = calculate_sides(metres_distance, vehicle_transform.rotation.yaw )

  spectator_pos = carla.Transform(vehicle_transform.location + carla.Location(x=-x,y=-y,z=5 ),
                                          carla.Rotation( yaw = vehicle_transform.rotation.yaw,pitch = -25))
  spectator.set_transform(spectator_pos)  