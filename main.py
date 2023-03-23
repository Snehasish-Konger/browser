import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtMultimediaWidgets import QVideoWidget



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle('PyBro')
        # set a custom icon for the window
        self.setWindowIcon(QIcon('icon.png'))

        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.setCentralWidget(self.tabs)

        self.add_tab()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        
        back_btn = QAction('⮜', self)
        back_btn.triggered.connect(lambda: self.current_browser().back())
        navbar.addAction(back_btn)

        forward_btn = QAction('⮞', self)
        forward_btn.triggered.connect(lambda: self.current_browser().forward())
        navbar.addAction(forward_btn)

        reload_btn = QAction('⟳', self)
        reload_btn.triggered.connect(lambda: self.current_browser().reload())
        navbar.addAction(reload_btn)

        # Home Button
        home_btn = QAction('⌂', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # Add a new tab button
        add_tab_btn = QAction('+', self)
        add_tab_btn.triggered.connect(self.add_tab)
        navbar.addAction(add_tab_btn)

        # Add a url bar
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.url_bar.setStyleSheet('width: 50%;')
        self.current_browser().urlChanged.connect(self.update_url)
        

    def add_tab(self):
        browser = QWebEngineView()
        browser.setUrl(QUrl('https://google.com'))
        self.tabs.addTab(browser, 'New Tab')
        self.tabs.setCurrentWidget(browser)
        self.tabs.setTabText(self.tabs.currentIndex(), 'Loading...')
        browser.titleChanged.connect(
            lambda title, browser=browser: self.tabs.setTabText(self.tabs.indexOf(browser), title))
        browser.urlChanged.connect(
            lambda url, browser=browser: self.update_url(url) if self.tabs.currentWidget() == browser else None)
        

    
    def close_tab(self, index):
        # Get the browser widget at the specified index
        browser_widget = self.tabs.widget(index)
    
        # Stop the video (if it is a video)
        if browser_widget.url().host() == "www.youtube.com":
            browser_widget.page().runJavaScript("document.getElementsByTagName('video')[0].pause();")
        
        # Remove the tab
        if self.tabs.count() < 2:
            # If this is the last tab, close the whole window
            self.close()
        else:
            # Remove the tab and delete the associated browser widget
            self.tabs.removeTab(index)
            browser_widget.deleteLater()


    def current_browser(self):
        return self.tabs.currentWidget()

    def navigate_home(self):
        self.current_browser().setUrl(QUrl('https://www.google.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        if 'http' not in url:
            url = 'https://' + url
        self.current_browser().setUrl(QUrl(url))
    
    def update_url(self, q):
        if self.sender() == self.current_browser():
            self.url_bar.setText(q.toString())
            self.url_bar.setCursorPosition(0)

    def closeEvent(self, event):
        for i in range(self.tabs.count()):
            # get the browser widget in the current tab
            browser = self.tabs.widget(i)
            # get the video widget, if it exists
            video_widget = browser.findChild(QVideoWidget)
            if video_widget:
                # stop the video
                video_widget.player().stop()
        event.accept()


app = QApplication(sys.argv)
app.setApplicationName('PyBro')
app.setApplicationDisplayName('PyBro')
app.setOrganizationName('PyBro')
window = MainWindow()
window.showMaximized()
app.exec_()
