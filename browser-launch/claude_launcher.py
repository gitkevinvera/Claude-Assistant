import sys
from PyQt5.QtCore import Qt, QUrl, QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEnginePage


class MiniBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set window properties
        self.setWindowTitle('Claude Mini Browser')
        self.setFixedSize(500, 600)  # Adjust the size as needed
        self.setWindowFlag(Qt.WindowStaysOnTopHint)  # Keeps the window on top
        self.setWindowFlags(self.windowFlags() | Qt.FramelessWindowHint)  # Remove the title bar

        # Create a web engine view
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.claude.ai/"))  # URL to load Claude's website

        # Set a custom user-agent
        self.browser.page().profile().setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")

        # Enable JavaScript and Pop-ups
        profile = self.browser.page().profile()
        profile.settings().setAttribute(profile.settings().JavascriptEnabled, True)
        profile.settings().setAttribute(profile.settings().JavascriptCanOpenWindows, True)

        # Handle new window requests
        self.browser.page().setFeaturePermission(QUrl("https://www.claude.ai/"), QWebEnginePage.Feature.PermissionGrantedByUser)

        self.browser.page().profile().setRequestInterceptor(self.CustomRequestInterceptor())

        # Create a central widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Set layout and add browser to it
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        central_widget.setLayout(layout)

        # Variables for dragging
        self._is_dragging = False
        self._start_position = QPoint()

    # Override mouse events to make window draggable
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = True
            self._start_position = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if self._is_dragging:
            self.move(event.globalPos() - self._start_position)
            event.accept()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._is_dragging = False
            event.accept()

    # Custom request interceptor to allow Google OAuth pop-ups
    class CustomRequestInterceptor(QWebEnginePage):
        def createWindow(self, _type):
            new_browser = QWebEngineView()
            new_browser.setWindowFlag(Qt.WindowStaysOnTopHint)
            new_browser.setWindowFlags(Qt.Window)
            new_browser.show()
            return new_browser


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Create and display the mini browser window
    window = MiniBrowser()
    window.show()

    # Execute the application
    sys.exit(app.exec_())
