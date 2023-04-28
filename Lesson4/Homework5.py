# Створіть англо-німецький словник, який називається e2g, і виведіть його на екран.
# Слова для словника: stork / storch, hawk / falke, woodpecker / specht і owl / eule.
# Виведіть німецький варіант слова owl.
# Додайте у словник, на ваш вибір, ще два слова та їхній переклад.
# Виведіть окремо: словник; ключі і значення словника у вигляді списків.


e2g = {'stork': 'storch', 'hawk': 'falke', 'woodpecker': 'specht', 'owl': 'eule'}

print(f'The German translation "owl" is "{e2g["owl"]}"')

e2g['table'] = 'tisch'
e2g['pen'] = 'stift'

print(e2g)

print(f'My e2g keys are {list(e2g.keys())}')
print(f'My e2g values are {list(e2g.values())}')
