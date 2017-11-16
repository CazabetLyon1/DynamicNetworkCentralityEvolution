from PyQt5 import QtWidgets , QtCore, QtGui
from PyQt5.QtWidgets import QGraphicsScene, QApplication, QFileDialog, QMainWindow,QLCDNumber, QSlider,QVBoxLayout, QPushButton,QLabel,QAction, QLineEdit, QMessageBox, QInputDialog, QComboBox, QSpinBox
from PyQt5.QtGui import QPixmap

class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10,10,556,392))
        self.graphicsView.setObjectName("graphicsView")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,673,125))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionOpen.triggered.connect(self.showDialog)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionExit.triggered.connect(QApplication.quit)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
      
        """
        self.label = QLabel()
        self.image = QPixmap("images/game.jpg")
        self.label.setPixmap(self.image)"""
        
                
        # Create textbox
        self.textbox = QLineEdit(MainWindow)
        self.textbox.move(580, 80)
        self.textbox.resize(280,40)
 
        # Create a button in the window
        self.button = QPushButton('Ok', MainWindow)
        self.button.move(580,120)
 
        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        
        #Getchoice
        self.cb = QComboBox(MainWindow)
        self.cb.move(580,50)
        self.cb.addItem("C")
        self.cb.addItem("C++")
        self.cb.addItems(["Java", "C#", "Python"])
        self.cb.currentIndexChanged.connect(self.selectionchange)
        
        #object presents the user with a integer
        self.l1 = QLabel("current value:")
        self.l1.move(650,50)
        self.sp = QSpinBox(MainWindow)
        self.sp.move(700,50)
        self.sp.valueChanged.connect(self.valuechange)
        
        
    def showDialog(self):
        fileName = QFileDialog.getOpenFileName(MainWindow, 'Open file')[0]
        print(fileName)
        self.scene = QGraphicsScene()
        self.scene.addPixmap(QPixmap(fileName))
        self.graphicsView.setScene(self.scene)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Mainwindow"))
        self.menuFile.setTitle(_translate("MainWindow","F&ile"))
        self.actionOpen.setText(_translate("MainWindow","Open"))
        self.actionExit.setText(_translate("MainWindow","Exit"))
        
        
    def on_click(self):
        textboxValue = self.textbox.text()
        QMessageBox.question(MainWindow, 'ton texte', "You typed: " + textboxValue, QMessageBox.Ok, QMessageBox.Ok)
        self.textbox.setText("")
        
        
    def selectionchange(self,i):
        print ("Items in the list are :")
        for count in range(self.cb.count()):
            print (self.cb.itemText(count))
        print ("Current index",i,"selection changed ",self.cb.currentText())
        
        
    def valuechange(self):
      self.l1.setText("current value:"+str(self.sp.value()))
      print(self.sp.value())
        
        
if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    
    MainWindow.showMaximized()
    sys.exit(app.exec_())
