import xmltodict
try:
    from urllib.parse import urljoin, urlencode
except ImportError:
    from urlparse import urlparse
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


class ArxivCrawler:
    def __init__(self):
        self.main_url = f'http://export.arxiv.org/api/query?search_query=all:image+segmentation&start=0&max_results=10'
        data = urlopen(self.main_url).read()
        a = xmltodict.parse(data)
        print(data)


if __name__ == '__main__':
    a = ArxivCrawler()


    url = '?search_query=all:segmentation&start=0&max_results=10'
    data = urlopen(url).read()
    a = xmltodict.parse(data)
    print(data)
