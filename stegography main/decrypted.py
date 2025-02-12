import cv2
import os
import string
with open("password.txt", "r") as file:
    password = file.read()
img = cv2.imread("encryptedImage.png")
c = {i: chr(i) for i in range(255)}
os.system("start encryptedImage.png")
message = ""
n = 0
m = 0
z = 0
pas = input("Enter Passcode for Decryption:")
for _ in range (1000): 
        message = message + c[img[n, m, z]]
        if message.endswith("#####"):
             break
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
if password == pas:
    print("Decryption Successful!")
    print("Decrypted Message:",message[:-5])
else:
  print("Unauthorised Access")

# The code is designed to decrypt the image and extract the message and password from it.