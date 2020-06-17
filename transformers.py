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

    def flipVertical(self):
        """
        self.matrix = self.transformToSquare()
        newMatrix = copy.deepcopy(self.matrix)  

        n = len(self.matrix[0])-1      
        for row in newMatrix: 
            for i in range( n//2):   
                self.matrix[i] = newMatrix[n-1-i]
                self.matrix[n-1-i] = newMatrix[i] 
        """
        self.matrix = self.matrix[::-1, :, :]

        img = Image.fromarray(self.matrix)
        img.show()

    def flipHorizontal(self):
        """
        for row in self.matrix: 
            for i in range((len(row) + 1) // 2):   
                temp = copy.deepcopy(row[i])
                row[i] = row[len(row)-1-i]
                row[len(row)-1-i] = temp
        """
        self.matrix = self.matrix[:, ::-1, :]

        img = Image.fromarray(self.matrix)
        img.show()

    def turnBlackWhite(self):
        
        for row in self.matrix: 
            for i in range((len(row))): 
                R = row[i][0]
                G = row[i][1]
                B = row[i][2]
                row[i] = 0.2989*R + 0.5870*G + 0.1140*B 
        
        img = Image.fromarray(self.matrix)
        #img = Image.fromarray(self.matrix).convert('LA')
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
    #bumblebee.rotate()
    #bumblebee.flipVertical()
    #bumblebee.flipHorizontal()
    bumblebee.turnBlackWhite()


if __name__ == '__main__':
    main()