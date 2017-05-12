"""Transliterate text by predefined rules

"""
__version__ = '1.0'

from .rules import *


def transliterate(text, rule=rules.GOST):
    """Transliterate text by rules.

    Args:
        text: text for transliteration.
        rule: Transliteration rule.
            Defaults to rules.USA - U.S. Departament of State's rule.
    """
    return rule().transliterate(text)
