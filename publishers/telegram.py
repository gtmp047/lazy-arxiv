import telepot
from utils.interactions import CONFIG


# todo make mongo saver

class TelegramPublisher():
    def __init__(self, t_channel=None, config=CONFIG):
        self.config = config
        self.telepot_bot = telepot.Bot(self.config['telegram']['token'])
        self.t_channel = t_channel

    def send_document(self, data):
        pass

if __name__ == '__main__':
    TelegramPublisher()