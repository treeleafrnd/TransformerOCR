from PIL import Image
from trocr.src.main import TrocrPredictor
import os
import matplotlib.pyplot as plt
import cv2

# load images
path = "test_images"
images_arr = []
images_a = []
for img in os.listdir(path):
    image_path = path + '/' + img
    curImg = cv2.imread(image_path)
    images_arr.append(image_path)
    images_a.append(curImg)

print(f'Path of images: {images_arr}')

# plotting the images    
plt.figure(figsize=(10, 10))  # specifying the overall grid size

for i in range(len(images_arr)):
    plt.subplot(3, 3, i + 1)  # the number of images in the grid is 5*5 (25)
    plt.imshow(images_a[i])

plt.show()

images = [Image.open(img_name) for img_name in images_arr]

# directly predict on Pillow Images or on file name
model = TrocrPredictor()
predictions = list(model.predict_images(images))

# print results  
for i, file_name in enumerate(images_arr):
    print(f'Prediction for {file_name}: {predictions[i]}')


