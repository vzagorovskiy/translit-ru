from . import rules

def transliterate(text,Rules=rules.USA):
    """Transliterate text by rules.

    Args:
        text: text.
        rules: datetime of when the message occurred.
            Defaults to USAEmbassyRules.
    """
    return Rules().transliterate(text)