import cv2
import os
import string 
img = cv2.imread("mypic.png") # Replace with the correct image path
msg = input("Enter secret message:")
password = input("Create a passcode:")
with open("password.txt", "w") as file:
        file.write(password)
d = {}
for i in range(255): 
        d[chr(i)] = i
m = 0
n = 0
z = 0
msg += "#####"
for i in msg:
     img[n, m, z] = d[i]
     n = n + 1
     m = m + 1
     z = (z + 1) % 3
cv2.imwrite("encryptedImage.png", img)
print("Successfully Encripted")
 