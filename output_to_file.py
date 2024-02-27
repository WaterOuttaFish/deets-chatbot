import time

def write_output(text):
    # define the file and open it
    file = open("test_file.txt", 'w')

    file.write(text)
    file.close()

def cached_output(text):
    currentTime = time.localtime() # get struct_time
    time_string = time.strftime("%H-%M-%S", currentTime)
    # define the file and open it
    name = "cache" + str(time_string) +".txt"
    file = open(name, 'w')
    file.write(text)
    file.close()
