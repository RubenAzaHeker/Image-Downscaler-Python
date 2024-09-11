from PIL import Image
import os
import time

new_width1 = 128 # Adjust the Width of the picture here. Remember this will stretch the picture!
new_height1 = 128 # Adjust the Height of the picture here. Remember this will stretch the picture!
num_colors1 = 16 # Adjust the colors the picture will have here. It does not use a color palette, it just uses the most common colors from the picture.

# The rest of the code is the program itself, you dont need to mess with anything. You might do something that will make the code unusable!

# If you find any errors or you get stuck on an error reach out to me on discord: rubenazaheker

# This is my first public project, so I hope that you like it or something!

# Made by RubenAzaHeker aka RubenGT

# If you want to support me, check out my website at http://www.rubengt.site , you'll find my ko-fi donation page there!

# This is version 1.1o. Read the changelog in readme.md!

print("Convert pictures to lower resolutions Version 1.1o") # Read about this in readme.md from line 36 to line 38.
print("Made By RubenAzaHeker aka RubenGT")
print(" ")
time.sleep(2)
print("You must read the readme.md file to understand the usage of the program and how to edit the values!")
print(" ")
time.sleep(2)
print("Resolution set to:")
print(f"Width is {new_width1} Pixels")
time.sleep(0.1)
print(f"Height is {new_height1} Pixels")
time.sleep(0.1)
print(f"Amount of the colors that will be used is {num_colors1} Colors")
print(" ")
time.sleep(2)

# If you decided to look into the code more, this is where the code actually transforms the picture.

def outimage(input_p, output_p, height=new_height1, width=new_width1, ncolors=num_colors1):
    if not os.path.isfile(input_p):   # If the file isnt found ----> ----> ----> ---->    ↓↓↓
        print(f"Sadly, the code couldn't find the file:( Error: {input_p} not found.") # Print out the error then ↓↓↓
        return # break <---- <---- <---- <---- <---- <---- <---- <---- <---- <---- <---- <---- <---- <---- <---- <----
    try:
        print("Opening image now.")    
        original_image = Image.open(input_p) # This will open the image.
    except Exception as e:
        print(f"Couldn't open image, closing now. Error {e}") # If it couldnt open, it will print this error.
        return # break
    
    print("Resizing image:")
    print("0%")
    resized_image = original_image.resize((width, height))   # This will actually resize the image.
    time.sleep(0.5)
    print("100%")
    time.sleep(1)
    
    try:
        print("Adujusting the colors:")
        print("0%")
        quantized_image = resized_image.convert('P', palette=Image.ADAPTIVE, colors=ncolors)    # This was added in v1.1 read about it in changelog in readme.md
        time.sleep(0.2)
        print("100%")
        time.sleep(1)
    except Exception as e:
        print(f"Error during color adjustment: {e}")
        return
        
    try:
        print("Saving image.")
        quantized_image.save(output_p)
        time.sleep(1)
        print("Image Successfully Saved")
    except Exception as e:
        print(f"Couldn't save image. Closing Now. {e}")

    
input_p = input("Enter the name of the input file with a name (and path to the directory if necessarily) >>> ").strip()
output_p = input("Enter the name of the output file with a name (and path to the directory if necessarily) >>> ").strip()

outimage(input_p, output_p)

# if you decided to look over the code ur welcome.

# Made by RubenAzaHeker aka RubenGT

# This was Version 1.1o