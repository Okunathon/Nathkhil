#cryptography

#barry steganography
    #take the lower bits of barry to get a new image

#take pixels in the image, un-crypto them to get the original image

#(255, 255, 255)

import cv2

#MSB Untouched Pixels Original Image Pixels -> Crypto Algorithm -> New Image Lower Part of Pixels

###### FILE PATHS ######
ORIGINAL_IMAGE = "imgs/dude.jpg"

#goal of this function is to take an original image, 
#add some stuff to the lower pixels
#encrypt the lower part of the bits
#and get a new image
def forward():
    orig_img = cv2.imread(ORIGINAL_IMAGE)
    
    print(orig_img[0][0])

if __name__ == "__main__":
    forward()