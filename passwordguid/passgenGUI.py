# imports
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QCheckBox, QButtonGroup, QMessageBox
from passgen import genPassword
import sys


#subclass object for QMainWindow to allow further customization
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setStyleSheet("background-color: lightgray;") #set background color to light gray
        self.initUI()
        
    # output generated password if the genButton widget is clicked
    def genButton_clicked(self):
        self.generatedpassword.setText(genPassword(self.selectedcharlength.currentText(), self.selectedmode()))
        self.update()
    # copy to clipboard
    def copyButton_clicked(self):
        #clipboard.copy(str(self.charlenfield.text()))
        self.generatedpassword.selectAll()
        self.generatedpassword.copy()

    # get mode selected
    def selectedmode(self):
        if self.securitymodegroup.checkedId() == -4:
            mode = 'advanced'
            self.selectedcharlength.clear()
            self.selectedcharlength.addItems([str(x+1) for x in range(15, 24)]) # 24 <= minimum length >= 16
        elif self.securitymodegroup.checkedId() == -3:
            mode = 'standard'
            self.selectedcharlength.clear()
            self.selectedcharlength.addItems([str(x+1) for x in range(7, 24)]) # 24 <= minimum length >= 8
        elif self.securitymodegroup.checkedId() == -2:
            mode = 'minimum'
            self.selectedcharlength.clear()
            self.selectedcharlength.addItems([str(x+1) for x in range(24)]) # in case 'advanced' or 'standard' was selected, updates dropdown items again to include 1->24
        return mode # pass the security mode to the function calling
    # info dialog window
    def modeinfo(self, s):
        self.infowindow = QMessageBox(self)
        self.infowindow.setWindowTitle("Mode Info")
        self.infowindow.setText("Minimal: any character length, UPPER/lower only.\nStandard: minimum of 8 characters, UPPER/lower, numbers, special characters\nAdvanced: minimum of 16 characters, UPPER/lower, numbers, special characters")
        self.donebutton = self.infowindow.exec()

    # UI object
    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("Password Generator")
        self.setFixedWidth(450)
        self.setFixedHeight(250)

        # genpwbutton - when pressed, calls to genButtonClicked
        self.genpwbutton = QtWidgets.QPushButton(self)
        self.genpwbutton.setText ("Generate")
        self.genpwbutton.move(85, 150)
        self.genpwbutton.setStyleSheet("background:white;")
        self.genpwbutton.clicked.connect(self.genButton_clicked)

        # copybutton - when pressed, copies password to clipboard
        self.copybutton = QtWidgets.QPushButton(self)
        self.copybutton.setText("Copy")
        self.copybutton.move(255,150)
        self.copybutton.setStyleSheet("background:white;")
        self.copybutton.clicked.connect(self.copyButton_clicked)
        
        
        # Asking to select a password length
        self.passwordlengthrequest = QtWidgets.QLabel("Password Length: ", self)
        self.passwordlengthrequest.move(5, 5)
        
        # dropdown to select character length (goes up to 16)
        self.selectedcharlength = QComboBox(self)
        self.selectedcharlength.addItems([str(x+1) for x in range(24)])
        self.selectedcharlength.setStyleSheet("background: white;")
        self.selectedcharlength.move(105, 5)



        # checkbox for bare minimum password security
        self.minimalsecurity = QCheckBox("Minimal", self)
        self.minimalsecurity.move(75, 60)
        # checkbox for standard password security
        self.standardsecurity = QCheckBox("Standard", self)
        self.standardsecurity.move(175, 60)
        # checkbox for advanced password security
        self.advancedsecurity = QCheckBox("Advanced", self)
        self.advancedsecurity.move(275, 60)
        
        # label above the password security options
        self.selectsecuritylabel = QtWidgets.QLabel("Security Mode", self)
        self.selectsecuritylabel.move(170, 40)

        # group security mode checkboxes
        self.securitymodegroup = QButtonGroup(self)
        self.securitymodegroup.addButton(self.minimalsecurity)
        self.securitymodegroup.addButton(self.standardsecurity)
        self.securitymodegroup.addButton(self.advancedsecurity)
        self.securitymodegroup.buttonToggled.connect(self.selectedmode)
        

        # field to show the generated password
        self.generatedpassword = QtWidgets.QLineEdit(self)
        self.generatedpassword.setStyleSheet("background: white;") # set line edit background to white
        self.generatedpassword.move(170,105)

        # info button
        self.infobutton = QPushButton('Mode Info', self)
        self.infobutton.setStyleSheet("background: white;")
        self.infobutton.move(5, 215)
        self.infobutton.clicked.connect(self.modeinfo)



def Window():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec())

Window()
