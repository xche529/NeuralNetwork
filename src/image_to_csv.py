import csv
from PIL import Image
import matplotlib.pyplot as plt
import os

csv_file = 'train_data.csv'
pic_folder = input("Enter the path to the folder containing the images: ")

for filename in os.listdir(pic_folder):
    if filename.endswith('.png'):
        #get the number the image is of
        number = filename[0]
        image = Image.open(os.path.join(pic_folder, filename))
        image = image.convert('L')
        pixels = image.getdata()
        image.close()
        image_data = [number]
        for pixel in pixels:
            image_data.append(pixel)
        with open(csv_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(image_data)
file.close()
print("Done!")