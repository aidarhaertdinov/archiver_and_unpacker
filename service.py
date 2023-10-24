class Archiver:
    """Класс архивации и разархивации строки"""
    @staticmethod
    def archiver(text: str) -> str:
        """
        Функция архиватор, которая принимает на вход строку произвольной длины,
        а возвращает другую строку меньшей длины.

        Args:
            text (str): Передается строка произвольной длины

        Raises:
            TypeError: Если переданный агрумент в функцию не строковый тип данных

        Returns:
            str: Возвращает cтроку меньшей длины

        """
        if type(text) is not str:
            raise TypeError("Text must be a string")
        archived_text = ""
        counter = 1
        # проходимся циклом по длине переданной строки не включая последний элемент
        for element in range(len(text) - 1):
            # если текущий элемент и следующий равны
            if text[element] == text[element + 1]:
                # то счетчик прибавляем на единицу
                counter += 1
            else:
                # в нашу строку прибавляем сумму счетчика(преобразовываем в строку) и текущего элемента
                archived_text += str(counter) + text[element]
                counter = 1
        # добавляем в конечную строку счетчик последнего элемента и сам элемент
        archived_text += str(counter) + text[-1]
        # если переданная строка в функцию короче получившейся
        if len(text) < len(archived_text):
            return text

        return archived_text

    @staticmethod
    def unpacker(text: str) -> str:
        """
        Функция разархивирования, которая принимает на вход "сжатую" строку,
        а на выходе возвращает исходную строку без потерь.

        Args:
            text (str): Передается "сжатая" строка

        Raises:
            TypeError: Если переданный агрумент в функцию не строковый тип данных

        Returns:
            str: Возвращает исходную строку, после разархивирования

        """
        if type(text) is not str:
            raise TypeError("Text must be a string")
        unpacked_text = ""
        counter_digit = ""
        # проходимся циклом по переданной строке
        for element in text:
            # если элемент является цифрой
            if element.isdigit():
                # к счетчику прибавляем этот элемент
                counter_digit += element
            else:
                # в нашу строку прибавляем произведение счетчика на текущий элемент
                unpacked_text += int(counter_digit) * element
                counter_digit = ""

        return unpacked_text
