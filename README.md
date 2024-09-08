##### Web Scraping with Scrapy Framework - Lab

> Developed with Python version 3.10.x

1. About Scrapy
- Had the same founder with Zyte(full framework for web scraping), Pablo Hoffman and Shane Evans, Scrapy is also a framework but build scrapers for scalablity, large HTML process, multiple file data format and storage location.
- Use ```scrapy shell``` to open and work with our project via Scrapy Shell
![Using Scrapy Shell to Fetch](/assets/fetch_sample1.png)
![Using Scrapy Shell to Extract Data from HTML component](/assets/fetch_sample2.png)
- Use XPath or CSS selectors to locate where in the page is the data.

2. Start a first spider with:
```sh
    cd automated_web_scraper
    scrapy genspider <name_of_spider> <website_url>
```
