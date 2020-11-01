from PIL import Image
from PIL import ImageEnhance
import pytesseract
import cv2
import matplotlib.pyplot as plt

def getText(path):
    #pytesseract path
    pytesseract.pytesseract.tesseract_cmd =r'C:/Program Files/Tesseract-OCR/tesseract'

    # assigning an image from the source path
    img = Image.open(path)

    # do some image processing before feed the image to the pytesseract
    # adding some sharpness and contrast to the image in order to be red well
    enhancer1 = ImageEnhance.Sharpness(img)
    enhancer2 = ImageEnhance.Contrast(img)
    processed_img = enhancer1.enhance(20.0)
    processed_img = enhancer2.enhance(1.5)
    # save the new image
    processed_img.save("power.png")
    # read the text from the image
    result = pytesseract.image_to_string(processed_img)

    return result


def write(result,filename):
    # save the text into a text file
    with open(filename, mode ="w") as file:
        file.write("This text is extracted from the Image :\n\n")
        file.write(result)
        print("your text image is in the text file. check it out !")

    return True

def read(filepath):
    # Load and read the file
    with open(filepath, mode ="r") as file:
        text= file.read()
    print(text)
    return True

def show(imagepath):
    # get the image and compare it to the returned text
    image = cv2.imread(imagepath,0)
    plt.imshow(image, cmap='gray')


## TESTING THE SCRIPT
if __name__ == "__main__":
    
    #get the text from the first image
    text=getText("./input_images/will_power.jpg")
    #write the text in a file
    write(text,"output_text/power.txt")
    #read the file again
    read("output_text/will_power.txt")
    
    #get the text from the second image
    text=getText("./input_images/bukowski_poem.jpg")
    #write the text in a file
    write(text,"output_text/bukowski_poem.txt")
    #read the file again
    read("output_text/bukowski_poem.txt")
