# Работы с архивацией и разархивацией строк 
## Назначение проекта
В проекте представлены две функции.
* Первая функцию-архиватор, которая принимает на вход строку произвольной длинны, а на выход выдает другую строку меньшей длины.
* Вторая функцию-разархивирования, которая принимает на вход "сжатую" строку, а на выходе возвращает исходную строку без потерь.

Тестирование функций было использовано с помощью `unittest`


## Запустить проект

Клонировать проект выполнив команду
```Bash 
git clone https://github.com/aidarhaertdinov/function_archiver_and_unpacker.git
```

## Перейти в директорию с проектом
```Bash 
cd /PycharmProjects/function_archiver_and_unpacked
```

## Запустить все тесты

```Bash 
python -m unittest
```
### Запустить тесты test_archiver.py
```Bash 
python -m unittest tests/test_archiver.py
```
### Запустить тесты test_unpacker.py
```Bash
python -m unittest tests/test_unpacker.py
```

## Запустить интерактив с пользователем

```Bash
python main.py
```