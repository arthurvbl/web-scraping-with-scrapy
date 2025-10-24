# Estudo sobre Scrapy

É um framework para extrair dados estruturados da `web`, muito usado para a mineração de dados, processamento de informações, dentre outros.  
Neste estudo, estarei trabalhando, como um exemplo, no scraping de notícias do portal `metropoles.com`.

---

# Como iniciar um projeto com Scrapy?
* Rode no seu terminal:
```bash
scrapy startproject scraper
```
* Isso vai criar:
```bash
├── scraper
│   ├── scraper
│   │   ├── __init__.py
│   │   ├── items.py
│   │   ├── middlewares.py
│   │   ├── pipelines.py
│   │   ├── settings.py
│   │   └── spiders
│   └── scrapy.cfg
```

# Como criar uma spider?
* Crie um arquivo na pasta criada (neste caso o arquivo se chama metropoles.py):
```bash
import scrapy


class metropoles_spider (scrapy.Spider):
    name = "metropoles"

    def start(self):
        url = "https://www.metropoles.com/ultimas-noticias"
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        pass
```

* Primeiro, para conseguirmos analisar a estrutura da spider para o projeto, devemos analisar como é feito o items.py
* O intuito dele é servir de "molde" para todas as spiders que serão adicionadas ao projeto
```bash
from scrapy.item import Item, Field


class Item(Item):
    title = Field()
    date = Field()
    category = Field()
    text = Field()
    author = Field()
```

* Em seguida, olhamos para pipelines.py, que diz como armazenar os dados coletados.

* Devemos tambem configurar o settings.py