import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class MiniBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle('Claude Mini Browser')
        self.setFixedSize(500, 600)  # Adjust the size as needed
        self.setWindowFlag(Qt.WindowStaysOnTopHint)  # Keeps the window on top

        # Create a web engine view
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.claude.ai/"))  # URL to load Claude's website

        # Set a custom user-agent
        self.browser.page().profile().setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Set layout and add browser to it
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        central_widget.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create and display the mini browser window
    window = MiniBrowser()
    window.show()

    # Execute the application
    sys.exit(app.exec_())

