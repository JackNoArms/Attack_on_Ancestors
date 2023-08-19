import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class App(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aplicativo Dash")
        self.setGeometry(100, 100, 800, 600)

        layout = QVBoxLayout()
        webview = QWebEngineView()
        webview.load(QUrl("home.py"))
        
        layout.addWidget(webview)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
