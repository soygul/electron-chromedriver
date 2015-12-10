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

## Reusing ChromeDriver Service
If you want to bind to an existing ChromeDriver rather than starting and stopping it for every test, see [issue #3](https://github.com/soygul/electron-chromedriver/issues/3).
