#PyQt5 introduction
import  sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.setWindowTitle("My cool first GUI")
        #self.setGeometry(700,300, 500, 500) #(position at X-axis, position at y-axis, width, height)

        #label = QLabel("Hello", self)
        #label.setFont(QFont("Arial", 40))
        #label.setGeometry(0, 0, 500, 100)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
