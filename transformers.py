from tkinter import *
from tkinter import filedialog, ttk
from PIL import Image, ImageDraw, ImageTk
import numpy as np
import copy


IMAGE = 'image/logo.png'
IMAGE = 'image/house.png'
IMAGE = 'image/donic.png'

class transformers:
    global ulx, uly, lrx, lry, cbox

    def __init__(self, image, master):
        self.path = IMAGE
        self.image = image
        self.width, self.height = image.size
        self.matrix = np.asarray(image)
        self.matrix.setflags(write=True)
        self.master = master

    def initializeGUI(self):
        global ulx, uly, lrx, lry, cbox

        img = Image.fromarray(self.matrix)
        img = Image.open(IMAGE)
        img1 = ImageTk.PhotoImage(img.resize((600, 600)))
        Label(self.master, image = img1).grid(row = 1, column = 0, 
            columnspan = 18, rowspan = 18, padx = 5, pady = 5) 
        


        ulx = Entry(self.master, width = 5)
        ulx.insert(0, "0")
        uly = Entry(self.master, width = 5)
        uly.insert(0, "0")
        lrx = Entry(self.master, width = 5)
        lrx.insert(0, "0")
        lry = Entry(self.master, width = 5)
        lry.insert(0, "0")

        cbox = ttk.Combobox(self.master, values=["R", "G", "B"], width = 5)

        actionRotate = Button(self.master, text = "Rotate", command=self.rotate) 
        actionVertical = Button(self.master, text = "Flip Vertical", command=self.flipVertical) 
        actionHorizontal = Button(self.master, text = "Flip Horizontal", command=self.flipHorizontal) 
        actionGrayscale = Button(self.master, text = "Grayscale", command=self.turnBlackWhite)
        actionDraw = Button(self.master, text = "Draw", command = self.drawBox)
        actionReset = Button(self.master, text = "Reset", command = self.resetGUI)
        actionSave = Button(self.master, text = "Save", command = self.saveImage)
        actionChoseFile = Button(self.master, text = "Chose File", command=self.choseImage)
        
        actionRotate.grid(row = 0, column = 0, sticky = E) 
        actionVertical.grid(row = 0, column = 1, sticky = E) 
        actionHorizontal.grid(row = 0, column = 2, sticky = E) 
        actionGrayscale.grid(row = 0, column = 3, sticky = E) 
        cbox.grid(row = 0, column = 4, sticky = E) 
        actionReset.grid(row = 0, column = 5, sticky = E) 
        actionSave.grid(row = 0, column = 6, sticky = E) 
        actionDraw.grid(row = 2, column = 19, sticky = E, columnspan = 2) 
        actionChoseFile.grid(row = 20, column = 0, sticky = W)  

        cbox.bind("<<ComboboxSelected>>", self.choseFilter)

        ulx.grid(row = 0, column = 20, sticky = W)
        uly.grid(row = 0, column = 21, sticky = W)
        lrx.grid(row = 1, column = 20, sticky = W)
        lry.grid(row = 1, column = 21, sticky = W)


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

        self.showImage()

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

        self.showImage()

    def flipHorizontal(self):
        """
        for row in self.matrix: 
            for i in range((len(row) + 1) // 2):   
                temp = copy.deepcopy(row[i])
                row[i] = row[len(row)-1-i]
                row[len(row)-1-i] = temp
        """
        self.matrix = self.matrix[:, ::-1, :]

        self.showImage()

    def turnBlackWhite(self):
        
        for row in self.matrix: 
            row.setflags(write=True)
            for i in range((len(row))): 
                R = row[i][0]
                G = row[i][1]
                B = row[i][2]
                row[i] = 0.2989*R + 0.5870*G + 0.1140*B 
        
        img = Image.fromarray(self.matrix)
        #img = Image.fromarray(self.matrix).convert('LA')
        self.showImage()

    def drawBox(self):
        global ulx, uly, lrx, lry, cbox
        ulxN = ulx.get()
        ulyN = uly.get()
        lrxN = lrx.get()
        lryN = lry.get()

        draw = ImageDraw.Draw(self.image)
        draw.rectangle((int(ulxN), int(ulyN), int(lrxN), int(lryN)), fill=(135,206,235), outline=(0,0,139))
        self.matrix = np.asarray(self.image)
        self.showImage()

    def saveImage(self):
        img = Image.fromarray(self.matrix).convert("RGB")
        img.save("image/output.jpg", "JPEG")

    def choseFilter(self, event):
        global cbox
        choice = cbox.get()
        if(choice=="R"):
            g=0
            b=0
            for row in self.matrix: 
                row.setflags(write=True)
                for i in range((len(row))): 
                    row[i][1] = g
                    row[i][2] = b
        if(choice=="G"):
            r=0
            b=0
            for row in self.matrix: 
                row.setflags(write=True)
                for i in range((len(row))): 
                    row[i][0] = r
                    row[i][2] = b
        if(choice=="B"):
            g=0
            r=0
            for row in self.matrix:
                row.setflags(write=True) 
                for i in range((len(row))): 
                    row[i][0] = r
                    row[i][1] = g        

        self.showImage()

    def showImage(self):
        self.image = Image.fromarray(self.matrix)
        img1 = ImageTk.PhotoImage(self.image.resize((600, 600)))
        imagePreview = Label(self.master, image = img1)
        imagePreview.grid(row = 1, column = 0, 
            columnspan = 18, rowspan = 18, padx = 5, pady = 5)  
        img.show() 
        #neznam zakaj, ali dok img.show() ,koji baca errore, ostane napisan prikazuje se slika, a ako maknem ne. Curious

    def printWH(self):
        print(self.width)
        print(self.height)
    
    def printMatrixShape(self):
        print(type(self.matrix))
        print(self.matrix.shape)
    
    def printMatrix(self):
        print(self.matrix)

    def choseImage(self):
        self.path=filedialog.askopenfilename(filetypes=[("Image File",'.jpg, .png')])
        self.image = Image.open(self.path)
        self.matrix = np.asarray(self.image)
        self.showImage()

    def resetGUI(self):
        self.image = Image.open(self.path)
        self.matrix = np.asarray(self.image)
        self.showImage()


    


def main():  
    img =Image.open(IMAGE)
    master = Tk()
    bumblebee = transformers(img, master)
    bumblebee.initializeGUI()
    #bumblebee.printWH()
    #bumblebee.showImage()
    #bumblebee.rotate()
    #bumblebee.flipVertical()
    #bumblebee.flipHorizontal()
    #bumblebee.turnBlackWhite()
    #bumblebee.drawBox(400, 800, 500, 400)
    #bumblebee.choseFilter("B")    

    mainloop()

if __name__ == '__main__':
    main()