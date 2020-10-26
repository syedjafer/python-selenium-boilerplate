from selenium import webdriver

def get_browser():
    browser = webdriver.Firefox()
    return browser