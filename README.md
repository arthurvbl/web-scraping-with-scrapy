# 📦 Web scraping with scrapy
Este é um repositório criado para explorar as utilidades e aplicações do framework Scrapy para o web scraping.

## 🎯 Objetivos
* Entender a estrutura e os componentes de um projeto Scrapy.
* Praticar extração de informações em páginas estáticas
* Explorar boas práticas de raspagem de dados, como:
  * Pausas entre requisições.
  * Tratamento de erros.
  * Armazenamento incremental dos dados (“saving as you go”).
 
## 🛠️ Tecnologias
* **Python 3.12.3**
* **Scrapy**
* **MongoDB**

## 📂 Estrutura do projeto
```bash
scrapy-study/
│── scrapy.cfg                # Configuração principal do Scrapy
│── requirements.txt          # Dependências do projeto
│
├── myspider/                 # Módulo principal do Scrapy
│   ├── __init__.py
│   ├── items.py              # Estrutura dos dados coletados
│   ├── middlewares.py        # Middlewares (tratamento de requests/responses)
│   ├── pipelines.py          # Definição do pipeline de dados
│   ├── settings.py           # Configurações do projeto
│   └── spiders/              # Onde ficam os spiders
│       └── exemplo_spider.py
│
└── README.md                 # Este arquivo
```

## 🚀 Como executar
1. Clone o repositório
```bash
git clone https://github.com/arthurvbl/web-scraping-with-scrapy.git
cd web-scraping-with-scrapy
```
2. Crie um ambiente virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```
3. Instale as dependências
```bash
pip install -r requirements.txt
```
4. Execute um spide de exemplo
```bash
scrapy crawl exemplo_spider -o resultados.json
```

## 📊 Armazenamento dos dados
Os dados raspados podem ser armazenados em:
* JSON/CSV (export direto via Scrapy).
* MongoDB (pipeline configurado no `pipelines.py`   

Exemplo de exportação para MongoDB (ajustar credenciais no settings.py):
```bash
ITEM_PIPELINES = {
   "myspider.pipelines.MongoPipeline": 300,
}
```

---

📌 Nota: O scraping deve sempre respeitar os termos de uso do site, o `robots.txt` e questões legais de uso dos dados.

---
