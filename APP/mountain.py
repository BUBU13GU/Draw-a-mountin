import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

class mainWindow(qtw.QWidget):
    # Sprint-1 Step-1: Initializer function
    def __init__(self):
        super().__init__()
        
        # Sprint-1 Step-2: Variables
        self.n_rows     = []
        self.n_columns  = []
        self.grid_data  = []

        # Sprint-1 Step-3: Read input file
        file = open('Data/medium.txt','r')

        # Sprint-1 Step-4: Extract the values of line-1 into 
        # self.n_rows and self.n_columns
        line = file.readline().split()
        self.n_rows = int(line[1]) 
        self.n_columns = int(line[1])

        # Sprint-1 Step-5:
        # Extract the values of line-2 into a two-dimensional list 
        # called self.grid_data
        # Important! Make sure each value is stored as a valid 
        #            float with two decimals
        list1 = []
        list2 = []
        list1 = file.read().split()
        for elm in list1:
            list2.append(float(elm))
        for i in range(0, len(list2), self.n_columns):
            self.grid_data.append(list2[i:i+self.n_columns])
            
        # Sprint-1 Step-6: 
        # Set window title and icon
        # Create self.label1 to be used to display the canvas
        # Create self.canvas based on the size of self.n_columns and self.n_rows       
        # Set self.canvas as the image for label1
        # Create the layout and display the UI
        self.setWindowTitle("Mountain")
        self.setWindowIcon(qtg.QIcon("Images/adventure.png"))
        
        self.label = qtw.QLabel()
        canvas = qtg.QPixmap(self.n_rows, self.n_rows)
        self.label.setPixmap(qtg.QPixmap(canvas))
        
        hLayout = qtw.QHBoxLayout()
        vLayout = qtw.QVBoxLayout()

        hLayout.addWidget(self.label)
        self.setLayout(hLayout)

        self.draw_something()    
        self.show()
        

        # Sprint-1 Step-7: 
        # Link a painter to label1's image and plot the data_points in
        # self.grid_data (the items in the sub-lists) on the canvas. 
        # Use "#c2c2a3" as color
    def draw_something(self):
        painter = qtg.QPainter(self.label.pixmap())
        pen = qtg.QPen()
        pen.setColor(qtg.QColor("dark gray"))
        painter.setPen(pen)
        point1 = 0
        point2 = 0
        for x in range(0, self.n_rows):
            for y in range(0, self.n_columns):
                painter.drawPoint(point1, point2)
                point1 += 1
                if point1 == self.n_columns:
                    point2 += 1
                    point1 = 0
                
        painter.end()
        


# *****************************************
# This is the Main Code section of the app.
# *****************************************
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # Create a mainWindow object
    mw = mainWindow()
    sys.exit(app.exec())
