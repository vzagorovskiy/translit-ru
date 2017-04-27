"""
Demonstrate using default transliteartion rule
"""
from translitru import transliterate
from examples import pangrams

print("Default transliteration")
print()
for txt in pangrams.text:
    print(txt)
    print(transliterate(txt), '\n')
