from PIL import Image
import os
import time
import warnings

new_width1 = 128 # Adjust the Width of the picture here. Remember this will stretch the picture!
new_height1 = 128 # Adjust the Height of the picture here. Remember this will stretch the picture!
num_colors1 = 16 # Adjust the colors the picture will have here. Its not like 16 bits or anything, it just uses the most common colors from the picture.

# The rest of the code is the program itself, you dont need to mess with anything. You might do something that will make the code unusable!

# If you find any errors reach out to me on discord: rubenazaheker

# This is my first public project, so i hope that you like it or something!

# Made by RubenAzaHeker aka RubenGT

# If you want to support me, check out my website at http://www.rubengt.site , you'll find my ko-fi donation page there!

print("Convert Pictures to lower resolutions1 Version 1.0o") # Read about this in readme.md at line 26, line 27, line 28.
print("Made By RubenAzaHeker aka RubenGT")
print(" ")
time.sleep(2)
print("You must read the readme.md file to understand the usage of the program and how to edit the values!")
print(" ")
time.sleep(2)
print(f"Resolution set to w={new_width1} and h={new_height1}, Color(s): {num_colors1}. To edit read readme.md")
print(" ")
time.sleep(2)

def recreate_image(input_path, output_path, new_width=new_width1, new_height=new_height1, num_colors=num_colors1):
    print(f"Checking if the input file exists: {input_path}")
    if not os.path.isfile(input_path):
        print(f"Error: The file {input_path} not found.")
        return

    try:
        print("Opening image")
        original_image = Image.open(input_path)
    except Exception as e:
        print(f"An error occurred while opening the image: {e}")
        return

    print("Editing image size")
    resized_image = original_image.resize((new_width, new_height))
    
    time.sleep(2)

    print("doing some shit")
    quantized_image = resized_image.quantize(colors=num_colors)
    
    time.sleep(1)

    # damn

    try:
        print(f"Creating image and saving it to: {output_path}")
        time.sleep(1)
        quantized_image.save(output_path)
        print(f"Image saved successfully to: {output_path}")
    except Exception as e:
        print(f"An error occurred while saving the image: {e}")

input_path = input("Enter the name of the input file with a name (and path to the directory if necessarily) >>> ").strip()
output_path = input("Enter the name of the output file with a name (and path to the directory if necessarily) >>> ").strip()

print(f"Input Path: {input_path}")
print(f"Output Path: {output_path}")

recreate_image(input_path, output_path)

warnings.filterwarnings("ignore", category=SyntaxWarning)

# If you decide to edit the code thats okay until you dont make it public, if you want to publish this code contact me please. Even if the changes are minor changes!

# Credit to RubenAzaHeker aka RubenGT (the creator of this code, me)