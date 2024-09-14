import sys

from View.app import Ui_App
from View.whiteCow import Ui_Whitecow
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stack = QStackedWidget(self)
        self.whitecow_page = Ui_Whitecow()
        self.app_page = Ui_App()

        self.stack.addWidget(self.app_page)
        self.stack.addWidget(self.whitecow_page)

        self.setCentralWidget(self.stack)

        
        # ปุ่มสลับหน้า (อยู่ในหน้าหลัก)
        self.app_page.switch_button.clicked.connect(self.switch_to_whitecow) 
        self.whitecow_page.switch_button.clicked.connect(self.switch_to_app)
        
        # กำหนดหน้าแรก
        self.stack.setCurrentWidget(self.app_page)  
    
    def switch_to_app(self):
        self.stack.setCurrentIndex(0)

    def switch_to_whitecow(self):
        self.stack.setCurrentIndex(1)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()