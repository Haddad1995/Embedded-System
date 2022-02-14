from sense_hat import SenseHat

sense = SenseHat()

#10.1. Create a SenseHat object.
#10.2. Get orientation:
o = sense.get_orientation()
#10.3. Get acceleration:
acceleration = sense.get_accelerometer_raw()
#10.4. Extract components from orientation:
pitch = o["pitch"]
roll = o["roll"]
yaw = o["yaw"]
#10.5. Extract components from acceleration and round their values:
x = acceleration['x']
y = acceleration['y']
z = acceleration['z']
x = acceleration['x']
y = acceleration['y']
z = acceleration['z']
x=round(x, 0)
y=round(y, 0)
z=round(z, 0)

#10.6. Print out all values:
print("pitch: ", pitch, " roll: ", roll, " yaw: ", yaw)
print("x: ", x, " y: ", y, " z: ", z)
