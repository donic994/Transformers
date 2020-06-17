from PIL import Image
import numpy as np

IMAGE = 'image/logo.png'
IMAGE = 'image/house.png'
#IMAGE = 'image/donic.png'

class transformers:
    def __init__(self, image):
            self.image = image
            self.width, self.height = image.size
            self.matrix = np.asarray(image)
            self.matrix.setflags(write=True)

    def showImage(self):
        img = self.image
        img.show()

    def printWH(self):
        print(self.width)
        print(self.height)
    
    def printMatrixShape(self):
        print(type(self.matrix))
        print(self.matrix.shape)
    
    def printMatrix(self):
        print(self.matrix)



def main():    
    img = Image.open(IMAGE)
    bumblebee = transformers(img)
    bumblebee.printWH()
    bumblebee.showImage()


if __name__ == '__main__':
    main()