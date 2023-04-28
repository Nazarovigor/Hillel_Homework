# Створіть багаторівневий словник subjects навчальних предметів.
# Використайте наступні рядки для ключів верхнього рівня:
# 'science', 'humanities' і 'public'.
# Зробіть так, щоб ключ 'science' був ім’ям іншого словника, який має ключі
# 'physics', 'computer science' і 'biology'.
# Зробіть так, щоб ключ 'physics' посилався на список рядків зі значеннями
# 'nuclear physics', 'optics' і 'thermodynamics'.
# Решта ключів повинні посилатися на порожні словники.
# Виведіть на екран ключі subjects['science'] і значення subjects['science']['physics'].

subjects = {
    'science': {'physics': ['nuclear physics', 'optics', 'thermodynamics'], 'computer science': {}, 'biology': {}},
    'humanities': {},
    'public': {}}

print(*list(subjects['science'].keys()), sep = '\n')
print()
print(*list(subjects['science']['physics']), sep = '\n')