"""
Demonstrate using Russian telegraph transliteration system
"""
from examples import pangrams
from translitru import transliterate, rules

# demo system A
print('System A')
print()
for txt in pangrams.text:
    print(txt)
    print(transliterate(txt, rules.Telegram), '\n')
