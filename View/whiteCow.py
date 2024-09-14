from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QPushButton

class Ui_Whitecow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.label = QLabel("Whitecow page")
        self.layout.addWidget(self.label)
        
        #เปลี่ยนหน้าต่าง
        self.switch_button = QPushButton("Switch to App")
        self.layout.addWidget(self.switch_button)
        
        self.setLayout(self.layout)