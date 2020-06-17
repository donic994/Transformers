from PIL import Image
import numpy as np
import copy

IMAGE = 'image/logo.png'
IMAGE = 'image/house.png'
IMAGE = 'image/donic.png'

class transformers:
    def __init__(self, image):
            self.image = image
            self.width, self.height = image.size
            self.matrix = np.asarray(image)
            self.matrix.setflags(write=True)

    def transformToSquare(self):
        matrix = np.asarray(self.image)
        if(self.height>=self.width):
            n = (self.height - self.width)//2
            matrix = matrix[n:, :, :]
            matrix = matrix[:-(n+1), :, :]
        if(self.height<self.width):
            n = (self.width - self.height)//2
            matrix = matrix[:, n:, :]
            matrix = matrix[:, :-n, :]

        matrix.setflags(write=True)
        return matrix

    def rotate(self):
        n = len(self.matrix[0])
        m = len(self.matrix)
        """
        self.matrix = self.transformToSquare()
        n = len(self.matrix[0])-1
        for i in range(n//2):
            for j in range(i, n-i-1):
                temp = copy.deepcopy(self.matrix[i][j])
                self.matrix[i][j] = self.matrix[n-1-j][i]
                self.matrix[n-1-j][i] = self.matrix[n-1-i][n-1-j]
                self.matrix[n-1-i][n-1-j] = self.matrix[j][n-1-i]
                self.matrix[j][n-1-i] = temp
        """
        self.matrix = np.asarray([[self.matrix[j][i] for j in range(m)] for i in range(n)])[::-1,:,:]
        #self.matrix = (np.transpose(self.matrix, (1,0,2)))[::-1,:,:]

        img = Image.fromarray(self.matrix)
        img.show()

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
    #bumblebee.showImage()
    bumblebee.rotate()


if __name__ == '__main__':
    main()