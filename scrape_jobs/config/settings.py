import os

from pathlib import Path
from dotenv import load_dotenv

from typing import Optional
from dataclasses import dataclass
from enum import Enum

# Load environment variables from .env file
load_dotenv()

# Project paths
PROJECT_ROOT: Path = Path(__file__).parent.parent.parent
DATA_DIR: Path = PROJECT_ROOT / "data"
LOGS_DIR: Path = PROJECT_ROOT / "logs"

# Create directories if they don't exist
DATA_DIR.mkdir(exist_ok=True)
LOGS_DIR.mkdir(exist_ok=True)

# Selenium settings
@dataclass
class SeleniumSettings:
    headless: bool = False
    implicit_wait: int = 10
    window_size: str = "600, 900"
    agent: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    
    use_chromium: bool = True
    chromium_path: str = "E:\\Utility\\Chromedriver\\chrome_win\\chrome.exe"
    chromedriver_path: str = "E:\\Utility\\Chromedriver\\chromedriver_win32\\chromedriver.exe"

# Wait Time settings
class WaitTime(int, Enum):
    DELAY = 1
    SHORT = 5
    MEDIUM = 15
    LONG = 30


# Logging settings
class LogLevel(str, Enum):
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"

@dataclass
class LogConfig:
    file_path: Path
    level: LogLevel = LogLevel.INFO
    max_file_size: int = 10_000_000
    backup_count: int = 3
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"



# Output settings
OUTPUT_FORMAT = os.getenv("OUTPUT_FORMAT", "json") 
OUTPUT_FILE_PREFIX = os.getenv("OUTPUT_FILE_PREFIX", "jobs")

