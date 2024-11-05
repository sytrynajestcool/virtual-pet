import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon #dodawanie ikon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ITost") #nazwa apki
        self.setGeometry(1300,1000,130,100) #ustawianie rozmiaru i gdzie ma sie respic okno
        self.setWindowIcon(QIcon("logo.png")) #ustawianie ikonki

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() #wyswietlanie okna
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()