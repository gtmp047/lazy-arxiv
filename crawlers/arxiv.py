
try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urlparse
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


class ArxivCrawler:
    def __init__(self):
        self.main_url = 'http://export.arxiv.org/api/query'

        pass


if __name__ == '__main__':

    import xmltodict

    url = '?search_query=all:segmentation&start=0&max_results=10'
    data = urlopen(url).read()
    a = xmltodict.parse(data)
    print(data)
