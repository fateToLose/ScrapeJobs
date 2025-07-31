# Scrape Jobs

Job scraping application designed to collect job posting data from various job board platforms. Built with Python using a modular architecture for scalability and maintainability.

> **Note**: This is a personal project designed to expand knowledge with web scraping.  
> _Have fun and continue building._

## Features

-   **Modular Architecture**: Clean separation of concerns with dedicated modules for scrapers, models, configuration, and utilities
-   **Selenium-based Scraping**: Robust web scraping using Selenium WebDriver with configurable browser settings
-   **Data Models**: Standardized job data structure with comprehensive job attributes
-   **Flexible Configuration**: Environment-based configuration with support for headless/headed browser operation
-   **Data Export**: Export scraped data to JSON and CSV formats
-   **Comprehensive Logging**: Built-in logging system with configurable log levels and file output
-   **Error Handling**: Robust error handling and retry mechanisms

## Development Status

### ✅ Completed

-   Setup and basic configuration with selenium

### 🚧 Work in Progress

-   Build scrapper for "CareerFuture" and "JobStreet" webpages
-   Database integration
-   Create job pipeline for scheduler
-   Build analytic (EDA) on crawled job information

## Quick Start

### Prerequisites

-   Python >=3.12
-   Chrome or Chromium browser
-   ChromeDriver

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/fateToLose/ScrapeJobs.git
    cd scrap_jobs
    ```

2. Install dependencies using uv:

    ```bash
    uv sync
    ```

3. Configure environment variables:
    ```bash
    cp example.env .env
    # Edit .env with your ChromeDriver and browser paths
    ```

## Project Structure

```
scrape_jobs/
├── config/                # Configuration management
│   ├── selenium_config.py # WebDriver configuration and setup
│   └── settings.py       # Application settings and environment variables
├── scrapers/              # Platform-specific scrapers
├── models/                # Data models
└── utils/                 # Utility functions
    └── logging.py         # Logging configuration

data/                      # Exported job data (auto-created)
logs/                      # Application logs (auto-created)
tests/                     # Test files
```

## Configuration

The application uses environment variables for configuration. Copy `example.env` to `.env` and configure:

```env
chromium_path=/path/to/your/chrome
chromedriver_path=/path/to/your/chromedriver
```

### Available Settings

-   **Browser Configuration**: Headless/headed mode, window size, user agent
-   **Wait Times**: Configurable timeouts for element loading
-   **Logging**: Log levels, file paths, and rotation settings

## Contributing

This is a personal learning project, but suggestions and improvements are welcome!

## License

This project is for educational and personal use. Please respect the terms of service of the job boards you scrape.

---
