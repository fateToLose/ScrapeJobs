import logging
from datetime import datetime

from selenium.webdriver.chrome.webdriver import WebDriver

from scrape_jobs.utils.logging import setup_logging
from scrape_jobs.config.selenium_config import SeleniumDriver
from scrape_jobs.config.settings import LogConfig, WaitTime, LOGS_DIR

setup_logging(LogConfig(file_path=LOGS_DIR), logger_name="ScrapeJob")
logger: logging.Logger = logging.getLogger(f"ScrapeJob.{__name__}")

url = "https://www.mycareersfuture.gov.sg/"

def main():
    logger.info("Starting ScrapeJob application...")
    driver: WebDriver | None = SeleniumDriver().init_selenium()
    
    if driver:
        driver.get(url)
    
    logger.info("Ended Session")

if __name__ == "__main__":
    main()