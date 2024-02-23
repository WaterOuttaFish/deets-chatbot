# import the packages made
import ocr
import summarizer
import output_to_file as output
from PIL import Image
import time # track execution time
from numba import jit


# filepath to slide, to be replaced with a live feed later

# the test file
# path = '/Users/name/Documents/Screenshots/Screenshot 2023-12-18 at 12.45.38 PM.png'

# take input from user for the file location
# path = input('Path to your image:\n')
#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR"

#@jit # run analyse_and_output on gpu
def analyse_and_output(path):
    # analyse image for text
    original_text = ocr.img2txt(path)
    print ('Original text is: ' + original_text)

    # summarize the text
    summarized_text = summarizer.summarize(original_text)
    print('Summarized text is: ' + summarized_text)

    output.write_output('Original text:\n\n' + original_text + '\n\n\n\nBREAK\n\n\n\n' + 'Summarized text:\n\n' + summarized_text)

path = r"C:\Users\Pranav\Downloads\testing_ocr_big.png"
# track time
t0 = time.perf_counter() # start time
analyse_and_output(path)
t1 = time.perf_counter() # end time
print("Execution time: ", t1-t0)
