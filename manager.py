from service import Archiver


class Manager:
    """Класс для управления объектами класса Archiver """
    @classmethod
    def menu(cls):
        """
        Функция меню для интерактива с пользователем
        """
        print("\nЗдравствуй пользователь!")
        while True:
            choice = input("\nВыбери один из вариантов:\n"
                           "1: Заархивировать строку\n"
                           "2: Разархивировать строку\n"
                           "3: Выход\n-> ")
            if choice == "1":
                current_string = Manager._archiver()
                answer = input("Разархивировать данную строку?\nВведите: ДА или НЕТ\n-> ")
                if answer in ['ДА', 'Да', 'да', 'yes', 'Yes', 'YES']:
                    print(f"Ваш результат: {Archiver.unpacker(current_string)}")
                elif answer in ['НЕТ', 'Нет', 'нет', 'no', 'NO', 'No']:
                    continue
                else:
                    print("Вы ввели не корректный ответ")
                    break

            elif choice == "2":
                Manager._unpacker()

            elif choice == "3":
                break
            else:
                print("Вы ввели не правильный вариант! Попробуйте еще раз")
                continue

    @classmethod
    def _archiver(cls):
        """Обработка логики архивирования"""
        while True:
            string = input("Введите строку произвольной длинны: ")
            if not string.isalpha():
                print("Вы ввели не строку! Попробуйте еще раз")
                continue
            print(f"Ваш результат: {Archiver.archiver(string)}\n")
            return Archiver.archiver(string)

    @classmethod
    def _unpacker(cls):
        """Обработка логики разархивирования"""
        while True:
            archived_string = input(f"Введите введите получившуюся заархивированную строку: ")
            if not archived_string.isalnum():
                print("Вы ввели не заархивированную строку! Попробуйте еще раз")
                continue
            print(f"Ваш результат: {Archiver.unpacker(archived_string)}")
            break
