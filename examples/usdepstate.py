"""
Demonstrate using U.S. State Department's rules
"""
from translitru import transliterate, rules
from examples import pangrams

# demo system A
print("U.S. State Department's rules")
print()
for txt in pangrams.text:
    print(txt)
    print(transliterate(txt, rules.USA), '\n')
