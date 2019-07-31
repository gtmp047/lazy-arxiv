import telepot
from utils.interactions import CONFIG
from urllib3.contrib.socks import SOCKSProxyManager
from telepot.api import _default_pool_params, _onetime_pool_params
from crawlers.arxiv import  ArxivCrawler
import logging


# todo make mongo saver

def set_telepot_socks_proxy(url, username=None, password=None):
    # from https://github.com/nickoala/telepot/pull/386
    telepot.api._onetime_pool_spec = (
    SOCKSProxyManager, dict(proxy_url=url, username=username, password=password, **_onetime_pool_params))
    telepot.api._pools['default'] = SOCKSProxyManager(url, username=username, password=password, **_default_pool_params)


class TelegramPublisher():
    def __init__(self, t_channel=None, config=CONFIG):
        self.config = config
        set_telepot_socks_proxy(f"socks5://orbtl.s5.opennetwork.cc:999", '448215182', 'UaP96Qhk')
        self.telepot_bot = telepot.Bot(self.config.telegram.token)
        self.t_channel = t_channel


    def send_document(self, data):
        self.telepot_bot.sendDocument(self.t_channel, data.get('pdf_file_b'),
                                      data.get('text'))

    def send_documents(self, data_list):
        for item in data_list:
            self.telepot_bot.sendDocument(self.t_channel, item.get('pdf_file_b'),
                                          item.get('text'))

    def send_texts(self, data_list):
        for item in data_list:
            self.telepot_bot.sendMessage(self.t_channel, item.get('text'))

if __name__ == '__main__':
    TelegramPublisher(CONFIG.telegram.chanel_name)
