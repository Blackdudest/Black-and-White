
name = input("What is your name? ")
if 3 < len(name) < 11:
  print("Welcome " + name)

  from PIL import Image
  file = r"C:\Users\adeoy\OneDrive\Desktop\pexels-cindy-gustafson-675313.jpg"
  img = Image.open(file)
  img = img.convert("L")
  img.show()

else:
    print(name + " is invalid! Try characters from 3-11 letters")

