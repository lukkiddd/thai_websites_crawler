# Crawler (Scrapy)

This folder contains all scrapy spiders which developed for a specific use case. The folder structures is followed by the standard scrapy project.

### How to use

#### Bilang Spider

1. Install dependencies
2. Prepare a file that contains both `th_url` and `en_url` as shown below.
3. Start the **splash server**
4. Run the scrapy

##### 1) Install dependencies

```bash
pip install -r requirements
```

##### 2) Prepare an input file


`urls.json`

```json
[
    {
        "th_url": "https://www.jobthai.com/th/job/720737", 
        "en_url": "https://www.jobthai.com/en/job/720737"
    }
] 
```

##### 3) Start the splash server

Using docker to start Splash Server with some configuration to prevent `timeout` issue

```bash
docker run --restart always -p 8050:8050 scrapinghub/splash --max-timeout 3600
```


##### 3) Start the scrapy server

Once you have this file and start splash server, you are able to run the following command to start the crawler.


```bash
scrapy crawl bilang -a file="./urls.json" -o output_file.csv
```

The scrapy will start scrape all the urls in the file called `urls.json` and save it as `csv` file named `output_file.csv`





## Additional materials

- [Scrapy Splash](https://github.com/scrapy-plugins/scrapy-splash)
- [Scrapy] (https://scrapy.org/)