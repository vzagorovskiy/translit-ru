class Telegram(object):
    """Russian telegraph's rules
    Транслитерация по "Инструкции о порядке обработки международных телеграмм в организациях связи", 2001 год 
    см. /docs/Instrukcia mezhdunarodnye telegrammy.pdf 
    Русские буквы "ь", "ъ" (мягкий знак и твердый знак) при транслитерации не применют. 
    Букву "ё" пишут и передают как букву "е".
    Букву "й" пишут и передают как букву "и" (i)

    """

    _TRANSLIT_TABLE = {
        u'\u0410': 'A', u'\u0430': 'a',  # Аа
        u'\u0411': 'B', u'\u0431': 'b',  # Бб
        u'\u0412': 'V', u'\u0432': 'v',  # Вв
        u'\u0413': 'G', u'\u0433': 'g',  # Гг
        u'\u0414': 'D', u'\u0434': 'd',  # Дд
        u'\u0415': 'E', u'\u0435': 'e',  # Ее
        u'\u0401': 'Е', u'\u0451': 'е',  # Ёё
        u'\u0416': 'J', u'\u0436': 'j',  # Жж
        u'\u0417': 'Z', u'\u0437': 'z',  # Зз
        u'\u0418': 'I', u'\u0438': 'i',  # Ии
        u'\u0419': 'I', u'\u0439': 'i',  # Йй
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
        u'\u0427': 'Ch', u'\u0447': 'ch',  # Чч
        u'\u0428': 'Sh', u'\u0448': 'sh',  # Шш
        u'\u0429': 'Sc', u'\u0449': 'sc',  # Щщ
        u'\u042a': '', u'\u044a': '',  # Ъъ
        u'\u042b': 'Y', u'\u044b': 'y',  # Ыы
        u'\u042c': '', u'\u044c': '',  # Ьь
        u'\u042d': 'E', u'\u044d': 'e',  # Ээ
        u'\u042e': 'Iu', u'\u044e': 'iu',  # Юю
        u'\u042f': 'Ia', u'\u044f': 'ia'  # Яя
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
