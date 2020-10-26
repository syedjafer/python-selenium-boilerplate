from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from utils.utils import get_browser
import time

class PackageSearcher:
    def __init__(self):
        self.browser = get_browser()

    def run(self):
        url = "https://pypi.org/"
        self.browser.get(url)
        search_element = self.browser.find_element_by_id("search")
        search_element.send_keys("selenium"+Keys.ENTER)
        time.sleep(10)
        uls = self.browser.find_element_by_class_name("unstyled")
        items = uls.find_elements_by_tag_name("li")
        items[0].click()
        release_element = self.browser.find_element_by_class_name("package-header__date")
        print(release_element.text)



if __name__ == "__main__":
    ps = PackageSearcher()
    ps.run()