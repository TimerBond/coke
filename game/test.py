import pymorphy2
morph = pymorphy2.MorphAnalyzer()
word = morph.parse('единица')[0]
print(word.make_agree_with_number(1).word)