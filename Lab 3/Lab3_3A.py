from sense_hat import SenseHat

def caesar(msg, key):
  alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWSYZ'
  new_message = ""

  for c in msg:
      position = alphabet.find(c.upper())
      new_position = (position + key) % len(alphabet)
      new_character = alphabet[new_position]
      new_message += new_character
  return new_message
     
key = 3
while True:
      message = input("Please enter a message: ")
      if message == "q": break
      encry_message = caesar(message, key)

      print("Encrypted message:" , encry_message)