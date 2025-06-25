import logging

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .settings import SeleniumSettings

logger: logging.Logger = logging.getLogger(f"ScrapeJob.{__name__}")

class SeleniumDriver:
    def __init__(self, setting=SeleniumSettings()) -> None:
        self.headless: bool= setting.headless
        self.agent: str = setting.agent
        self.implicit_wait: int = setting.implicit_wait
        self.window_size: str = setting.window_size
        self.use_chromium: bool = setting.use_chromium
        self.chromium_path: str = setting.chromium_path
        self.chromedriver_path: str = setting.chromedriver_path
        
        self.driver: webdriver.Chrome | None = None
    
    def init_selenium(self) -> webdriver.Chrome | None:
        logger.info("Initializing Selenium WebDriver...")
        
        try:
            options = Options()
            
            if self.headless:
                options.add_argument("--headless")
            
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--disable-gpu")
            options.add_argument("--disable-extensions")
            options.add_argument("--disable-blink-features=AutomationControlled")
            options.add_argument(f"--window-size={self.window_size}")
            options.add_argument(f"--user-agent={self.agent}")
            
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)
            
            if self.use_chromium:
                driver: WebDriver | None = self.run_by_chromium(options)
                return driver

            # Default to chrome
            driver = webdriver.Chrome(options=options)
            driver.implicitly_wait(self.implicit_wait)
            self.driver = driver
            return driver
        
        except Exception as e:
            raise Exception(f"Failed to create Chrome driver: {e}")
    
    def run_by_chromium(self, options) -> webdriver.Chrome | None:
        try:
            if not Path(self.chromium_path).exists():
                raise FileNotFoundError(f"Chromium executable not found at {self.chromium_path}")
            if not Path(self.chromedriver_path).exists():
                raise FileNotFoundError(f"Chromedriver executable not found at {self.chromedriver_path}")
            
            options.binary_location = self.chromium_path
            service = Service(self.chromedriver_path)
            driver = webdriver.Chrome(service=service, options=options)
            driver.implicitly_wait(self.implicit_wait)
            self.driver = driver
            return driver
        
        except Exception as e:
            logger.error(f"Error initializing Selenium with Chromium: {e}")
            logger.info("Falling back to default Chrome driver initialization.")
                
    
    def quit_driver(self) -> None:
        if self.driver:
            self.driver.quit()
            self.driver = None
            logger.info("Selenium WebDriver quit successfully.")


def get_webdriver_wait(driver: webdriver.Chrome, timeout: int = 10) -> WebDriverWait:
    return WebDriverWait(driver, timeout)