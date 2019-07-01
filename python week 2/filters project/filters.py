from PIL import Image
import math
# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.
def load_img(file_name):
    image = None
    try:
        image = Image.open(file_name)
    except IOError:
        print("The file %s cannot be found, or the image cannot be opened and identified!" %(file_name))
    return image
# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(selected_image):
    selected_image.show()


# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(selected_image, file_name):
    try:
        selected_image.save(file_name)
    except IOError:
        print("Unable to write file %s!" %(file_name))
    except KeyError:
        print("Unable to determine the file format from the name!")


# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(image):
    new_image = Image.new(image.mode, image.size, color = 0)
    old_data = image.getdata()
    new_data = []
    dark_blue = (0, 51, 76)
    red = (217, 26, 33)
    light_blue = (112, 150, 150)
    yellow = (252, 227, 166)
    for pixel in old_data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if(intensity<182):
            new_data.append(dark_blue)
        elif(intensity<364):
            new_data.append(red)
        elif(intensity<546):
            new_data.append(light_blue)
        else:
            new_data.append(yellow)
    new_image.putdata(new_data)
    return new_image


def grayscale(image):
        new_image = Image.new(image.mode, image.size, color = 0)
        old_data = image.getdata()
        new_data = []
        for pixel in old_data:
            gray_value = (pixel[0]+pixel[1]+pixel[2])/3
            gray_value = round(gray_value)
            new_data.append((gray_value, gray_value, gray_value))
        new_image.putdata(new_data)
        return new_image

def grayscale2(image):
    new_image = Image.new(image.mode, image.size, color = 0)
    old_data = image.getdata()
    new_data = []
    dark_blue = (0, 51, 76)
    red = (217, 26, 33)
    light_blue = (112, 150, 150)
    yellow = (252, 227, 166)
    for pixel in old_data:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if(intensity<182):
            new_data.append(dark_blue)
        elif(intensity<364):
            new_data.append(red)
        elif(intensity<546):
            new_data.append(light_blue)
        else:
            new_data.append(yellow)
    new_image.putdata(new_data)
    return new_image
