from sense_hat import SenseHat

def caesar_encryption(msg):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  private_key = 19
  encry_message = ""
  
  for c in msg:
    position = alphabet.find(c)
    new_position = (position + private_key) % len(alphabet)
    new_character = alphabet[new_position]
    encry_message += new_character
  return encry_message

def caesar_decryption(msg, public_key):
  alphabet = "abcdefghijklmnopqrstuvwxyz"
  private_key = 23
  decry_message = ""
  key = int(public_key / private_key)
  
  for c in msg:
    position = alphabet.find(c)
    new_position = (position - key) % len(alphabet)
    new_character = alphabet[new_position]
    decry_message += new_character
  return decry_message

while True:
      message = input("Please enter a message: ")
      public_key= int(input("please enter public key"))
      if message == "q": break
      encry_message = caesar_encryption(message)
      decry_message = caesar_decryption(encry_message,public_key)

      print("Encrypted message:" , encry_message)
      print("Decrypted message:" , decry_message)
