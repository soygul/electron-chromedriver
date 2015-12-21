# Electron ChromeDriver
Starter kit for testing Electron apps using Selenium ChromeDriver with Python bindings.

## Documentation
* Selenium ChromeDriver: [sites.google.com/a/chromium.org/chromedriver](https://sites.google.com/a/chromium.org/chromedriver/)
* Selenium Python Bindings: [selenium-python.readthedocs.org](https://selenium-python.readthedocs.org)

## Getting Started
Simply replace following variables in the code and restructure the testing code according to your app:

```python
chromedriver_path = "./chromedriver"
electron_path = "/Applications/MyApp.app/Contents/MacOS/Electron"
```

You also need to download [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) binary and extract it to the repo root, and install `selenium` package:

```python
pip3 install selenium
```

## Page Object Pattern
This project utilizes page object pattern for modelling the UI components into reusable classes (page objects). These page objects encapsulate relevant UI interactions and elements in one place so when your UI changes, you'll only have to change one file. See the [Selenium Docs - PageObjects](https://github.com/SeleniumHQ/selenium/wiki/PageObjects) wiki for detailed explanation. Wiki entry is for Java but it gives you the general idea.

## Reusing ChromeDriver Service
If you want to bind to an existing ChromeDriver rather than starting and stopping it for every test, see [issue #3](https://github.com/soygul/electron-chromedriver/issues/3).
