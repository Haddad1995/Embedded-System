from sense_hat import SenseHat 
from time import sleep

sense = SenseHat()
while True:
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()
  message = "Temperature: " + str(t) + "C" + " Pressure: " + str(p)+ "hPa" + " Humidity: " + str(h)+ "%"
  print(message)
  sleep(1)
