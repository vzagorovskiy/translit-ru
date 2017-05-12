""" Define rules for transliteration

"""


class GOST_A(object):
    """Транслитерация по ГОСТ 7.79—2000 (ISO 9:1995)
    Система A


    """
    _TRANSLIT_TABLE = {
        u'\u0410': 'A', u'\u0430': 'a',  # Аа
        u'\u0411': 'B', u'\u0431': 'b',  # Бб
        u'\u0412': 'V', u'\u0432': 'v',  # Вв
        u'\u0413': 'G', u'\u0433': 'g',  # Гг
        u'\u0414': 'D', u'\u0434': 'd',  # Дд
        u'\u0415': 'E', u'\u0435': 'e',  # Ее
        u'\u0401': u'\u00CB', u'\u0451': u'\u00EB',  # Ёё    Ëë
        u'\u0416': u'\u017D', u'\u0436': u'\u017E',  # Жж    Žž
        u'\u0417': 'Z', u'\u0437': 'z',  # Зз
        u'\u0418': 'I', u'\u0438': 'i',  # Ии
        u'\u0419': 'J', u'\u0439': 'j',  # Йй
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
        u'\u0425': 'H', u'\u0445': 'h',  # Хх
        u'\u0426': 'C', u'\u0446': 'c',  # Цц
        u'\u0427': u'\u010C', u'\u0447': u'\u010D',  # Чч    Čč
        u'\u0428': u'\u0160', u'\u0448': u'\u0161',  # Шш    Šš
        u'\u0429': u'\u015C', u'\u0449': u'\u015D',  # Щщ    Ŝŝ
        u'\u042a': u'\u02BA', u'\u044a': u'\u02BA',  # Ъ     ʺ
        u'\u042b': 'Y', u'\u044b': 'y',  # Ыы
        u'\u042c': u'\u02B9', u'\u044c': u'\u02B9',  # ь     ʹ
        u'\u042d': u'\u00C8', u'\u044d': u'\u00E8',  # Ээ   Èè
        u'\u042e': u'\u00DB', u'\u044e': u'\u00FB',  # Юю  Ûû
        u'\u042f': u'\u00C2', u'\u044f': u'\u00E2'  # Яя   Ââ
    }

    def transliterate(self, text):
        """Transliterate text

        :param text: text to be transliterated
        :return: transliterated text
        """
        transliterated = ''
        for index, char in enumerate(text):
            if char in self._TRANSLIT_TABLE:
                transchar = self._TRANSLIT_TABLE[char]
            else:
                transchar = char
            transliterated += transchar
        return transliterated


class GOST_B(object):
    """Транслитерация по ГОСТ 7.79—2000 (ISO 9:1995)
    Система Б

    """
    _TRANSLIT_TABLE = {
        u'\u0410': 'A', u'\u0430': 'a',  # Аа
        u'\u0411': 'B', u'\u0431': 'b',  # Бб
        u'\u0412': 'V', u'\u0432': 'v',  # Вв
        u'\u0413': 'G', u'\u0433': 'g',  # Гг
        u'\u0414': 'D', u'\u0434': 'd',  # Дд
        u'\u0415': 'E', u'\u0435': 'e',  # Ее
        u'\u0401': 'Yo', u'\u0451': 'yo',  # Ёё    yo
        u'\u0416': 'Zh', u'\u0436': 'zh',  # Жж    zh
        u'\u0417': 'Z', u'\u0437': 'z',  # Зз
        u'\u0418': 'I', u'\u0438': 'i',  # Ии
        u'\u0419': 'J', u'\u0439': 'j',  # Йй
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
        u'\u0425': 'X', u'\u0445': 'x',  # Хх
        u'\u0426': 'Cz', u'\u0446': 'cz',
        # Цц #рекомендуется использовать С перед буквами I, Е, Y, J; в остальных случаях CZ
        u'\u0427': 'Ch', u'\u0447': 'ch',  # Чч
        u'\u0428': 'Sh', u'\u0448': 'sh',  # Шш
        u'\u0429': 'Shh', u'\u0449': 'shh',  # Щщ
        u'\u042a': '``', u'\u044a': '``',  # Ъ
        u'\u042b': 'Y`', u'\u044b': 'y`',  # Ыы
        u'\u042c': '`', u'\u044c': '`',  # ь
        u'\u042d': 'E`', u'\u044d': 'e`',  # Ээ
        u'\u042e': 'Yu', u'\u044e': 'yu',  # Юю
        u'\u042f': 'Ya', u'\u044f': 'ya'  # Яя
    }

    def transliterate(self, text):
        """Transliterate text

        :param text: text to be transliterated
        :return: transliterated text
        """
        transliterated = ''
        for index, char in enumerate(text):
            if char in self._TRANSLIT_TABLE:
                transchar = self._TRANSLIT_TABLE[char]
            else:
                transchar = char
            transliterated += transchar
        return transliterated


class GOST(GOST_A):
    pass
