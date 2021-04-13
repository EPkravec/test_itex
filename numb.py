class Num:
    """
    Класс Num применяется для выявления является ли число number степенью числа 2
    :param: number: - десятичное число
    """

    def __init__(self, number):
        self.number = number

    def check_number(self):
        """
        Проверка на входимость в степень числа 2 self.number
        :return: True: -  если входит
        :return: False: - если не входит
        """
        result = (False if self.number.count('1') - 1 else True)
        return result
