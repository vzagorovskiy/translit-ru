import unittest
from translitru import transliterate, rules


class TestTranslit(unittest.TestCase):
    """Unit test for translit rules 
    
    """

    def test_usdepstate(self):
        txt = u"Завершён ежегодный съезд эрудированных школьников, мечтающих глубоко проникнуть в тайны физических явлений и химических реакций."
        txt_t = "Zavershеn ezhegodnyy syezd erudirovannykh shkolnikov, mechtayushchikh gluboko proniknut v tayny fizicheskikh yavleniy i khimicheskikh reaktsiy."
        self.assertEqual(transliterate(txt, rules.USA), txt_t)

    def test_gost_a(self):
        txt = u"Завершён ежегодный съезд эрудированных школьников, мечтающих глубоко проникнуть в тайны физических явлений и химических реакций."
        txt_t = u"Zaveršën ežegodnyj sʺezd èrudirovannyh školʹnikov, mečtaûŝih gluboko proniknutʹ v tajny fizičeskih âvlenij i himičeskih reakcij."
        self.assertEqual(transliterate(txt, rules.GOST_A), txt_t)

    def test_gost_b(self):
        txt = u"Завершён ежегодный съезд эрудированных школьников, мечтающих глубоко проникнуть в тайны физических явлений и химических реакций."
        txt_t = u"Zavershyon ezhegodny`j s``ezd e`rudirovanny`x shkol`nikov, mechtayushhix gluboko proniknut` v tajny` fizicheskix yavlenij i ximicheskix reakczij."
        self.assertEqual(transliterate(txt, rules.GOST_B), txt_t)


if __name__ == '__main__':
    unittest.main()
