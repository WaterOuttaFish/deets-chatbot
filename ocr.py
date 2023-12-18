def img2txt(path_to_img):
    # import packages - pytesseract for ocr and pillow for importing images
    import pytesseract
    from PIL import Image

    # define path
    path = path_to_img
    # open image
    image = Image.open(path)
    # analyse image using pytesseract
    txt_from_image = pytesseract.image_to_string(image)

    # return the text from the image
    return txt_from_image

