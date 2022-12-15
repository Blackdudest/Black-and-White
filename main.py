
name = input("What is your name? ")
if 3 < len(name) < 11:
  print("Welcome " + name)

else:
    print(name + " is invalid! Try characters between 3 and 11")

from PIL import Image
file = r"C:\Users\adeoy\OneDrive\Desktop\pexels-cindy-gustafson-675313.jpg"
img = Image.open(file)
img = img.convert("L")
img.show()