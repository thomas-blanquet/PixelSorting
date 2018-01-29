from PIL import Image, ImageFile
import sys
import numpy as np

originalPic = None
pixels = None
pixelsLuminanceImage = None
pixelsLuminance = None
luminanceThreshold = 127
size = (0, 0)

def errorQuit(message):
    print("Error: " + message, file=sys.stderr)
    sys.exit(1)

#Open the image
def loadImage(image):
    print("Loading image...")
    global originalPic
    originalPic = Image.open(image)
    print("Loaded !")

#Convert image to nparray of pixels (RGB)
def imageToList():
    print("Putting image to array of pixels...")
    global pixels
    global size
    pixels = np.array(originalPic.getdata()).reshape(originalPic.size[1], originalPic.size[0], 3)
    size = (originalPic.size[1], originalPic.size[0])
    print ("Done !")

#By using a formula, create a black and white image using white for pixels brighter than the threshold and black otherwise
def createLuminanceImage(name):
    print("Creating luminance filter...")
    global pixelsLuminanceImage
    global pixels
    pixelsLuminanceImage = np.copy(pixels)
    for array in pixelsLuminanceImage:
        for row in array:
            if (row[0] * 0.2126 + row[1] * 0.7152 + row[2] * 0.0722) < luminanceThreshold:
                row[0] = row[1] = row[2] = 0
            else:
                row[0] = row[1] = row[2] = 255
    print("Done !")
    print("Saving image...")
    image = Image.fromarray(pixelsLuminance.astype('uint8'))
    image.save(name, "JPEG", quality=80, optimize=True, progressive=True)
    print("Saved !")

#Create and fill an 2D array corresponding to pixels's luminance
def initLuminanceTab():
    global size
    global pixelsLuminance
    global pixels
    
if __name__ == '__main__':
    if len(sys.argv) < 2:
        errorQuit("Not enough parameters.")
    try:
        loadImage(sys.argv[1])
    except FileNotFoundError:
        errorQuit("'" + sys.argv[1] + "': Image not found.")
    except PermissionError:
        errorQuit("'" + sys.argv[1] + "': Image not found.")
    imageToList()
    createLuminanceImage("out.jpg")
    
