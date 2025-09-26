# Estudo sobre Scrapy

É um framework para extrair dados estruturados da `web`, muito usado para a mineração de dados, processamento de informações, dentre outros.

---

# Como criar uma spider?

Para entendermos como funciona o framework, precisamos primeiramente entender como as `spiders` funcionam nele. Aqui está um exemplo de spider que minera frases do website [quotes to scrape](https://quotes.toscrape.com/):

```bash
import scrapy                           # Importa o framework


class QuotesSpider(scrapy.Spider):      # "QuoutesSpider" herda a classe Spider
    name = "quotes"                     # nome da spider
    start_urls = [
        "https://quotes.toscrape.com/tag/humor/",
    ]

    def parse(self, response):          # método que é chamada 
                                        # automaticamente quando chega a 
                                        # resposta da requisição
        for quote in response.css("div.quote"):
                                        # Procura todos os elementos <div> 
                                        # com a classe quote usando seletor 
                                        # CSS.
            yield {                     # Extrai os dados de autor e a quote
                "author": quote.xpath("span/small/text()").get(),
                "text": quote.css("span.text::text").get(),
            }

        next_page = response.css('li.next a::attr("href")').get()
                                        # Procura a próxima página de citações
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```

Adicione esse código em um arquivo `quotes_spider.py`, rodando com o comando:

```bash
scrapy runspider quotes_spider.py -o quotes.jsonl 
```

Isso adiciona um arquivo `quotes.jsonl` com uma lista de quoutes em JSON Lines, como mostra a seguir:

```bash
{"author": "Jane Austen", "text": "\u201cThe person, be it gentleman or lady, who has not pleasure in a good novel, must be intolerably stupid.\u201d"}
{"author": "Steve Martin", "text": "\u201cA day without sunshine is like, you know, night.\u201d"}
{"author": "Garrison Keillor", "text": "\u201cAnyone who thinks sitting in church can make you a Christian must also think that sitting in a garage can make you a car.\u201d"}
...
```

A forma que esse processo acontece é a seguinte: 
* Rodando a linha acima no seu terminal, o Scrapy procura por uma spider no arquivo. 
