from crawlers.arxiv import ArxivCrawler
from publishers.telegram import TelegramPublisher
from utils.logging import set_handler_logger, setup_logging
from utils.interactions import CONFIG, DATA_DIR_PATH
from os.path import join
import sqlite3

setup_logging()
logger = set_handler_logger(__name__)

def create_db(conn):
    conn.execute('''CREATE TABLE DOCUMENTS
             (ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             ULR            TEXT     NOT NULL);''')

def get_unique_uid_list():
    raise NotImplementedError()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='tags.txt')
    args = parser.parse_args()
    arxiv_results = []
    tag_list = []
    telega = TelegramPublisher(CONFIG.telegram.chanel_name)
    with sqlite3.connect(CONFIG.data.sqllite) as conn:
        create_db(conn)
        with open(join(DATA_DIR_PATH, args.input)) as fh:
            tag_list = [i.strip() for i in fh.readlines()]
        logger.info(f'Started crawl {len(tag_list)} tags')
        for tag in tag_list:
            logger.info(f'Crawl tag - {tag}')
            arxiv_res = ArxivCrawler(tag)

            arxiv_results.append(arxiv_res.parsed_data)

        logger.info(f'Push to telegram tag - {tag}')
        telega.send_texts(arxiv_res.parsed_data)
