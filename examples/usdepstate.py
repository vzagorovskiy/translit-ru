"""
Demonstrate using U.S. State Department's rules
"""
from examples import pangrams
from translitru import transliterate, rules

# demo system A
print("U.S. State Department's rules")
print()
for txt in pangrams.text:
    print(txt)
    print(transliterate(txt, rules.USA), '\n')
