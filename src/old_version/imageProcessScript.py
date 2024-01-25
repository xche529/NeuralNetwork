from PIL import Image
import matplotlib.pyplot as plt
import os

row_folder = input("Enter the path to the folder containing the raw images: ")
target_number = input("Enter the number these images are of: ")
target_folder = input("Enter the path to the folder you want to save the processed images to: ")
next_suffix = 0

for filename in os.listdir(row_folder):
    # Check if the file is an image (JPEG, PNG, etc.)
    if filename.endswith('.png'):
        # Construct the complete file path
        file_path = os.path.join(row_folder, filename)
        # Open the image
        image = Image.open(file_path)
        resized_image = image.resize((28, 28))
        next_suffix += 1
        filename = f'{next_suffix}_processed_image_{target_number}.png'
        save_path = os.path.join(target_folder, filename)
        resized_image.save(save_path)
        image.close()
        resized_image.close()

print("Done!")
        

#plt.imshow(resized_image)
#plt.show()

