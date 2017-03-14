"""
Demonstrate using default transliteartion rule
"""
from translitru import transliterate
import pangrams

print("Default transliteration")
print()
for txt in pangrams.text:
    print(txt)
    print(transliterate(txt), '\n')
