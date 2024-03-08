# Take screenshot. Run through model. Get summary. Store in .txt file. Context used for chatbox
import pyscreenshot as ImageGrab
from PIL import Image
import os
import output_to_file

def save_img(): # save screenshot of image
    temp = ImageGrab.grab()
    temp.save('recentCache.png')

# get summary of screenshot

def remove_file():
    # remove recentCache.png after running summarizer
    if os.path.exists('recentCache.png'): # avoid error
        os.remove('recentCache.png')
    else: 
        print("something is messed up...")


