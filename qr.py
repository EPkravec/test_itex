from urllib.parse import urlparse

import qrcode


class Qr:
    """
    Класс Qr применяется для валидации полученного url, и на его основе создает QR-code
    :param: href - url сайта
    """

    def __init__(self, href):
        self.href = href

    def url_check(self):
        """
        Проверка url на валидность

        :return: True: если валидно
        :return: False: если не валидно
        """
        try:
            result = urlparse(self.href)
            return all([result.scheme, result.netloc, result.path])
        except ValueError:
            return False

    def creat_qc(self):
        """
        Создание преобразование url в QR-code и его запись в file
        """
        result = self.url_check()
        if result:
            file = 'qr-code.jpg'
            image = qrcode.make(self.href)
            image.save(file)
