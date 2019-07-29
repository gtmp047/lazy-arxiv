import xmltodict
from typing import List

try:
    from urllib.parse import urljoin, urlencode
except ImportError:
    from urlparse import urlparse
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen


def get_first(val: list):
    if val and isinstance(val, list):
        return val[0]
    return val


class ArxivCrawler:
    def __init__(self, search_query: str):
        query = self.build_query_string(search_query)
        self.query_url = f'http://export.arxiv.org/api/query?{query}'
        self.raw_data = xmltodict.parse(urlopen(self.query_url).read())
        self.parsed_data = ArxivCrawler.get_entry_infos(self.raw_data)

    @staticmethod
    def get_entry_infos(entry_list: List):
        res = []
        for item in entry_list:
            item['author'] = [i.get('name') for i in item['author']]
            item['pdf_link'] = get_first([i.get('@href') for i in item['link'] if i.get('@type') == 'application/pdf'])
            item['category'] = [i.get('@term') for i in item['category']]
            res.append(item)
        return res

    def build_query_string(self, search_query: str, start: int = 0, max_results: int = 50,
                           sortBy: str = 'submittedDate', sortOrder: str = 'descending'):
        data = {
            'search_query': search_query,
            'start': start,
            'max_results': max_results,
            'sortBy': sortBy,
            'sortOrder': sortOrder,
        }
        return urlencode(data)
