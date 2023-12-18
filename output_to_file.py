def write_output(text):
    # define the file and open it
    file = open("test_file.txt", 'w')

    file.write(text)
    file.close()
