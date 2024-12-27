# function imports
import ocr
import caching
import summarizer
import output_to_file as output
# module imports
from PIL import Image
import time # track execution time
import tiktoken

"""
BRANCH NOTES:

"""

# take screenshot and summarize output
caching.save_img()
file_path = 'recentCache.png' #default file name of 

# wrapper function
def analyse_and_output(file_path):
    # run OCR on image
    original_text = ocr.img2txt(file_path)
    # summarize the text
    summarized_text = summarizer.big_input_summarize(original_text, 800, tiktoken.get_encoding("cl100k_base"))
    return summarized_text

# track time
t0 = time.perf_counter() # start time
output_summary = analyse_and_output(file_path)
input = ''.join(output_summary)
output.cached_output(input)
print(output_summary)
time.sleep(10)
output.cached_output(input)
t1 = time.perf_counter() # end time
print("--------------------------------------------------------")
print("Execution time: ", t1-t0)
