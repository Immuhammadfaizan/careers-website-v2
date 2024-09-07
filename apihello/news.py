from flask import Flask, request, render_template
from newsapi import NewsApiClient

app = Flask(__name__)
newsapi = NewsApiClient(api_key='4d58af8d3ff147e591b8955a1715948f')

def get_domains_and_sources(limit = 5):
    all_sources = newsapi.get_sources()['sources']
    domains = []
    sources = []

    for e in all_sources[:limit]:
        id = e['id']
        domain = e['url'].replace('http://', '')
        domain = domain.replace('https://', '')
        domain = domain.replace('www.', '')
        slash = domain.find('/')

        if slash != -1:
            domain = domain[:slash]
        sources.append(id)
        domains.append(domain)

    sources = ", ".join(sources)
    domains = ", ".join(domains)
    return sources, domains

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        sources, domains = get_domains_and_sources(limit = 5)
        keyword = request.form['keyword']
        related_news = newsapi.get_everything(q = keyword,
                                        sources = sources,
                                        domains = domains,
                                        language = 'en',
                                        sort_by = 'relevancy')

        no_of_articles = related_news['totalResults']
        if no_of_articles > 100:
            no_of_articles = 100
        all_articles = newsapi.get_everything(q = keyword,
                                        sources = sources,
                                        domains = domains,
                                        language = 'en',
                                        sort_by = 'relevancy',
                                        page_size = no_of_articles)['articles']

        return render_template('news.html', all_articles = all_articles,
                                            keyword = keyword)
    else:
        top_headlines = newsapi.get_top_headlines(country = 'pk', language = 'en')

        total_results = top_headlines['totalResults']
        if total_results > 100:
            total_results = 100
        all_headlines = newsapi.get_top_headlines(country = "pk",
                                                     language = "en",
                                                     page_size = total_results)['articles']

        return render_template('news.html', all_headlines = all_headlines)
    return render_template('news.html')

if __name__ == '__main__':
    app.run(debug = True)
