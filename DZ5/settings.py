#BOT_NAME = 'scrapy_spider'

#SPIDER_MODULES = ['scrapy_spider.spiders']
#NEWSPIDER_MODULE = 'scrapy_spider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrapy_spider (+http://www.yourdomain.com)'

# Obey robots.txt rules
#ROBOTSTXT_OBEY = True


#ITEM_PIPELINES = {
#    'scrapy_spider.pipelines.ScrapySpiderPipeline': 300,
#}
#============================================================================================

BOT_NAME = 'all_pages'

SPIDER_MODULES = ['all_pages.spiders']
NEWSPIDER_MODULE = 'all_pages.spiders'

DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'all_pages.pipelines.CSVPipeline': 300,
}

# Настройки для экспорта данных в формат CSV
FEED_FORMAT = 'csv'
FEED_URI = 'output.csv'

# Тоже можно использовать настройки для CSV
# FEED_EXPORT_ENCODING = 'utf-8'  # кодировка для CSV, по умолчанию utf-8
FEED_EXPORT_FIELDS = ['title', 'review']  # список полей для экспорта в CSV

# Настройки для обхода политики robots.txt (можно отключить)
# ROBOTSTXT_OBEY = False

# Настройки для логирования (по умолчанию записывается только в консоль)
LOG_FILE = 'scrapy.log'  # указание файла для логирования

# Другие настройки, такие как задержки, юзер-агенты и прокси, могут быть указаны здесь
# DOWNLOAD_DELAY = 3  # задержка между запросами

# Убедитесь, что имена пауков и путь к пайплайну соответствуют вашей структуре проекта scrapy