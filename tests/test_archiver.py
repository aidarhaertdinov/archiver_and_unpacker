from unittest import TestCase
from service import Archiver


class ArchiverTest(TestCase):
    """ Класс для тестирования функции archiver """

    def test_positive_one(self):
        """
        Первый положительный тест проверит функцию archiver
        на равенство данных строк
        """
        self.assertEqual(Archiver.archiver(text="AAAAAABBCCCCDDDDEE"), "6A2B4C4D2E")

    def test_positive_two(self):
        """
        Второй положительный тест проверит функцию archiver
        на равенство данных строк
        """
        self.assertEqual(Archiver.archiver(text="jjkkkkkkkkkwwmmmmmmmmmmmmmmmmqq"), "2j9k2w16m2q")

    def test_negative_one(self):
        """
        Первый негативный тест проверит функцию archiver
        на неравенство данных строк
        """
        self.assertNotEqual(Archiver.archiver(text="AAAAAABBCCCCDDDDEE"), "6A2B4C4D3E")

    def test_negative_two(self):
        """
        Второй негативный тест проверит функцию archiver
        на неравенство данных строк
        """
        self.assertNotEqual(Archiver.archiver(text="jjkkkkkkkkkwwmmmmmmmmmmmmmmmmqq"), "3j9k2w16m2q")

    def test_type_one(self):
        """
        Первый тест проверит функцию archiver,
        если будет передан первый аргумент не строка, а список
        """
        self.assertRaises(TypeError, Archiver.archiver, text=['kkkaaawww'])

    def test_type_two(self):
        """
        Второй тест проверит функцию archiver,
        если будет передан первый аргумент не строка, а кортеж
        """
        self.assertRaises(TypeError, Archiver.archiver, text=('fffssseeeettttt',))
