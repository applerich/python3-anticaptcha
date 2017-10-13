import requests

# from .errors import RuCaptchaError
from config import get_balance_url, incorrect_captcha_url

from config import TEST_KEY


class AntiCaptchaControl:
    def __init__(self, anticaptcha_key):
        self.ANTICAPTCHA_KEY = anticaptcha_key

    def get_balance(self):
        '''
        Получение баланса аккаунта
        :return: Возвращает актуальный баланс
        '''
        answer = requests.post(get_balance_url, json = {'clientKey': self.ANTICAPTCHA_KEY})

        if answer.json()['errorId'] == 0:
            return answer.json()['balance']
        else:
            return answer.json()

    def complaint_on_result(self, reported_id):
        '''
        Позволяет отправить жалобуна неправильно решённую капчу.
        :param reported_id: Отправляете ID капчи на которую нужно пожаловаться
        :return: Возвращает True/False, в зависимости от результата
        '''
        payload = {'clientKey': self.ANTICAPTCHA_KEY,
                   'taskId': reported_id,
                   }

        answer = requests.post(incorrect_captcha_url, json = payload)

        if answer.json()['errorId'] == 0:
            return True
        else:
            return False


print(AntiCaptchaControl(anticaptcha_key = TEST_KEY).complaint_on_result(reported_id = -5))
print(AntiCaptchaControl(anticaptcha_key = TEST_KEY).get_balance())