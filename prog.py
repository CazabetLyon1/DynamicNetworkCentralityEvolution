import networkx as nx
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

"""
app = QApplication(sys.argv)

w = QWidget()

w.show()

sys.exit(app.exec_())"""

G=nx.read_graphml("data\GoT_S01E01_000.graphml")


class App(QWidget):
 
    def __init__(self):
        super().__init__()
        self.title = 'RC3'
        self.setWindowIcon(QIcon('data\game.png'))
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        
        button = QPushButton('PyQt5 button', self)
        button.setToolTip('This is an example button')
        button.move(150,400) 
        button.clicked.connect(self.on_click)
        
        button2 = QPushButton('PyQt5 button', self)
        button2.setToolTip('This is an example button')
        button2.move(250,400) 
        button2.clicked.connect(self.on_click)
        
        
        self.show()
        pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')   
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())