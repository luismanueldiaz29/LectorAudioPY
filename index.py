from PySide2.QtWidgets import QApplication
from controllers.indexController import indexController
if __name__ == "__main__":
    app = QApplication()
    window = indexController()
    window.show()
    app.exec_()