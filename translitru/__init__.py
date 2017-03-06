from . import rules


def transliterate(text, rule=rules.USA):
    """Transliterate text by rules.

    Args:
        text: text for transliteration.
        rule: Transliteration rule.
            Defaults to rules.USA - U.S. Departament of State's rule.
    """
    return rule().transliterate(text)
