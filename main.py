from PIL import Image
name = input("What is your name? ")
if 3 < len(name) < 11:
  print("Welcome " + name)


  file = r"C:\Users\adeoy\Downloads\surface-T8YJX3lpiMQ-unsplash.jpg"
  img = Image.open(file)
  img = img.convert("L")
  img.show()

else:
    print(name + " is invalid! Try characters from 3-11 letters")

