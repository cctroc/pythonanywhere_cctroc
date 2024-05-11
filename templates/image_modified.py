from PIL import Image

img=Image.open(r".\static\assets\images\space.jpg", mode='r')
print(img.format)
# print(dir(img))
print(img.size)
space2 = img.resize((500,300))
space2.show()
space2.save(r'.\static\assets\images\space.png','png')
