"""
Demonstrate using GOST 7.79—2000 (ISO 9:1995) System A
"""
from translitru import transliterate, rules
import pangrams

# demo system A
print('System A')
print()
for txt in pangrams.text:
    print(txt)
    print(transliterate(txt, rules.GOST_A), '\n')

# demo system B
print('System B')
print()
for txt in pangrams.text:
    print(txt)
    print(transliterate(txt, rules.GOST_B), '\n')
