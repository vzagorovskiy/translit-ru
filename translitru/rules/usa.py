

class USA(object):
    """U.S. State Department's rules
    Транслитерация по правилам госдепартамента США
    http://www.ustraveldocs.com/ru_ru/Transliteration_Rus.pdf
    1 - Русская буква е транслитерируется как ye в случае, если открытого слога, после гласных,
        а также после твердого и мягкого знаков; во всех остальных случаях её необходимо транслитерировать как e.
    2 - Буква ë транслитерируется по тем же правилам, что и e.
    3 - Буквы й и ы транслитерируются как y.

    """

    _TRANSLIT_TABLE = {
        u'\u0410': 'A', u'\u0430': 'a',  # Аа
        u'\u0411': 'B', u'\u0431': 'b',  # Бб
        u'\u0412': 'V', u'\u0432': 'v',  # Вв
        u'\u0413': 'G', u'\u0433': 'g',  # Гг
        u'\u0414': 'D', u'\u0434': 'd',  # Дд
        u'\u0415': 'E', u'\u0435': 'e',  # Ее
        u'\u0401': 'Е', u'\u0451': 'е',  # Ёё
        u'\u0416': 'Zh', u'\u0436': 'zh',  # Жж
        u'\u0417': 'Z', u'\u0437': 'z',  # Зз
        u'\u0418': 'I', u'\u0438': 'i',  # Ии
        u'\u0419': 'Y', u'\u0439': 'y',  # Йй
        u'\u041a': 'K', u'\u043a': 'k',  # Кк
        u'\u041b': 'L', u'\u043b': 'l',  # Лл
        u'\u041c': 'M', u'\u043c': 'm',  # Мм
        u'\u041d': 'N', u'\u043d': 'n',  # Нн
        u'\u041e': 'O', u'\u043e': 'o',  # Оо
        u'\u041f': 'P', u'\u043f': 'p',  # Пп
        u'\u0420': 'R', u'\u0440': 'r',  # Рр
        u'\u0421': 'S', u'\u0441': 's',  # Сс
        u'\u0422': 'T', u'\u0442': 't',  # Тт
        u'\u0423': 'U', u'\u0443': 'u',  # Уу
        u'\u0424': 'F', u'\u0444': 'f',  # Фф
        u'\u0425': 'Kh', u'\u0445': 'kh',  # Хх
        u'\u0426': 'Ts', u'\u0446': 'ts',  # Цц
        u'\u0427': 'Ch', u'\u0447': 'ch',  # Чч
        u'\u0428': 'Sh', u'\u0448': 'sh',  # Шш
        u'\u0429': 'Shch', u'\u0449': 'shch',  # Щщ
        u'\u042a': '', u'\u044a': '',  # Ъ
        u'\u042b': 'Y', u'\u044b': 'y',  # Ыы
        u'\u042c': '', u'\u044c': '',  # ь
        u'\u042d': 'E', u'\u044d': 'e',  # Ээ
        u'\u042e': 'Yu', u'\u044e': 'yu',  # Юю
        u'\u042f': 'Ya', u'\u044f': 'ya'  # Яя
    }

    # исключения
    _TRANSLIT_TABLE_EXCEPTIONS = {
        u'\u0415': 'Ye', u'\u0435': 'ye',  # Ее ye
        u'\u0401': 'Ye', u'\u0451': 'yе',  # Ёё ye
    }
    # гласные
    _VOWELS = [
        u'\u0410', u'\u0430',  # Аа
        u'\u0415', u'\u0435',  # Ее ye
        u'\u0401', u'\u0451',  # Ёё ye
        u'\u0418', u'\u0438',  # Ии
        u'\u041e', u'\u043e',  # Оо
        u'\u0423', u'\u0443',  # Уу
        u'\u042b', u'\u044b',  # Ыы
        u'\u042d', u'\u044d',  # Ээ
        u'\u042e', u'\u044e',  # Юю
        u'\u042f', u'\u044f',  # Яя
    ]
    # твердый и мягкий знак
    _SIGNS = [
        u'\u042a', u'\u044a',  # Ъ
        u'\u042c', u'\u044c',  # ь
    ]

    def transliterate(self, text):
        """Transliterate text

        :param text: text to be transliterated
        :return: transliterated text
        """
        transliterated = ''
        for index, char in enumerate(text):
            if char in self._TRANSLIT_TABLE_EXCEPTIONS and (
                            index == 0 or text[index - 1] in self._VOWELS + self._SIGNS):
                transchar = self._TRANSLIT_TABLE_EXCEPTIONS[char]
            else:
                if char in self._TRANSLIT_TABLE:
                    transchar = self._TRANSLIT_TABLE[char]
                else:
                    transchar = char
            transliterated += transchar
        return transliterated
