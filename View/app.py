
from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QInputDialog, QLineEdit, QFormLayout, QVBoxLayout, QMessageBox

from Controller.CowIdChecker import CheckCowId
from Controller.CowIdChecker import checkCowData

class Ui_App(QWidget):
     
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Cow Strike Checker")
        self.setGeometry(100, 100, 800, 600)
         
        #กำหนดประเภทของ Layout
        self.outerLayout = QVBoxLayout()
        self.layout = QFormLayout()
         
        #ชื่อโปรแกรม Cow Strike Checker 
        self.title = QLabel("Cow Strike Checker")
        self.title.setStyleSheet("font-weight: semi-Bold; font-size: 40px; font-family: Inter; ")
         
        #รับค่าจากผู้ใช้
        self.cowIdLabel = QLabel("Enter Cow Id:")
        self.cowIdLabel.setStyleSheet("font-weight: semi-Bold; font-size: 20px; font-family: Inter;")
        self.cowIdInput = QLineEdit()
        self.cowIdInput.setMaximumWidth(150)
        
         
        #ปุ่ม enter
        self.enterButton = QPushButton("Enter")
        self.enterButton.clicked.connect(self.enterButtonClicked)
        self.enterButton.setFixedSize(80,30)
        self.enterButton.setStyleSheet("QPushButton {background-color: blue; color: white; font-weight: bold; font-size: 14px; font-family: Inter; }"
                                 "QPushButton:hover {background-color: lightblue;}")
        
        self.switch_button = QPushButton("Switch to Whitecow")
        
        
        self.layout.addRow(self.title) 
        self.layout.addRow(self.cowIdLabel, self.cowIdInput)  
        self.layout.addRow(self.enterButton)
        self.layout.addWidget(self.switch_button)
        
        
        self.outerLayout.addLayout(self.layout)
        self.outerLayout.addStretch()
        self.setLayout(self.outerLayout)
        
        
    def enterButtonClicked(self):
        cowId = self.cowIdInput.text()
        
        # ถ้าผิดให้แสดงข้อความว่าใส่ผิด
        isCowIdvalid = CheckCowId(cowId)
        if not isCowIdvalid:
            QMessageBox.about(self, "Invalid Input", "Please enter a valid Cow ID with 8 digit and not start with 0.")
        
        # เช็คว่ามีวัวตัวนั้นไหม
        isCowIdvalid = checkCowData(cowId)
        if isCowIdvalid:
            self.switch_button = QPushButton("Switch to Whitecow")
            self.layout.addWidget(self.switch_button)
            
    
        
         
         
         

     