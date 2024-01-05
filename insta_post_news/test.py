from transliterate import translit

# Пример транслитерации
cyrillic_text = "Привет, мир! и слава".split(' ')[:2]
res = ' '.join(cyrillic_text)
latin_text = translit(res, 'ru', reversed=True)  # 'ru' указывает на русский язык

# print(latin_text)
# print(res)

