from unittest import TestCase
from service import Archiver


class UnpackerTest(TestCase):
    """ Класс для тестирования функции unpacker """

    def test_positive_one(self):
        """
        Первый положительный тест проверит функцию unpacker
        на равенство данных строк
        """
        self.assertEqual(Archiver.unpacker(text="6A2B4C4D2E"), "AAAAAABBCCCCDDDDEE")

    def test_positive_two(self):
        """
        Второй положительный тест проверит функцию unpacker
        на равенство данных строк
        """
        self.assertEqual(Archiver.unpacker(text="2j9k2w16m2q"), "jjkkkkkkkkkwwmmmmmmmmmmmmmmmmqq")

    def test_negative_one(self):
        """
        Первый негативный тест проверит функцию unpacker
        на неравенство данных строк
        """
        self.assertNotEqual(Archiver.unpacker(text="6A2B4C14D2E"), "AAAAAABBCCCCDDDDDDDDDDDDDDDEE")

    def test_negative_two(self):
        """
        Второй негативный тест проверит функцию unpacker
        на неравенство данных строк
        """
        self.assertNotEqual(Archiver.unpacker(text="2j9k2w16m2q"), "jjjjkkkkkkkkkwwmmmmmmmmmmmmmmmmqq")

    def test_type_one(self):
        """
        Первый тест проверит функцию unpacker,
        если будет передан первый аргумент не строка, а список
        """
        self.assertRaises(TypeError, Archiver.unpacker, text=['kkkaaawww'])

    def test_type_two(self):
        """
        Второй тест проверит функцию unpacker,
        если будет передан первый аргумент не строка, а кортеж
        """
        self.assertRaises(TypeError, Archiver.unpacker, text=('fffssseeeettttt',))
