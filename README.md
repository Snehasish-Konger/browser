# PyBro

PyBro is a simple web browser built with Python and PyQt5. It allows you to open multiple tabs, navigate to different websites, and play videos.

Step-by-step guide available at https://scientyficworld.org/how-to-build-a-browser-using-python/

## Getting Started

To get started with PyBro, clone the repository and install the required dependencies using pip:

`pip install PyQt5 PyQtWebEngine`

## Usage

To run the browser, simply run the `main.py` file:

`$ python main.py`


### Features

- Multiple tabs: You can open multiple tabs and navigate to different websites in each tab.
- Video support: PyBro supports playing videos from YouTube and other websites.
- Navigation buttons: PyBro includes navigation buttons for going back, forward, and reloading the page.
- Home button: The home button takes you to the Google search page.
- URL bar: You can enter a URL in the URL bar to navigate to a specific website.

### Implementation

PyBro is built using PyQt5, which is a Python binding for the popular cross-platform GUI toolkit Qt. The main window of the browser contains a QTabWidget, which allows you to switch between multiple tabs. Each tab contains a QWebEngineView widget, which is used to display web pages.

When a new tab is added, a QWebEngineView widget is created and added to the QTabWidget. The QWebEngineView widget is then set to display the Google search page by default. As the user navigates to different pages, the URL bar and tab title are updated to reflect the current page.

When a tab is closed, PyBro first checks if the tab contains a video player. If it does, the video is stopped before the tab is closed. If the tab was the last tab open, the entire application is closed.

## Output
browser.webm

## About using the code:

The code for this project is open to all. Anyone can use this code and build their own browser and also if some wants to add features to this code/ our browser, they can do that freely.
