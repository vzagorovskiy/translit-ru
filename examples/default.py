"""
Demonstrate using default transliteartion rule
"""
from examples import pangrams
from translitru import transliterate

print("Default transliteration")
print()
for txt in pangrams.text:
    print(txt)
    print(transliterate(txt), '\n')
