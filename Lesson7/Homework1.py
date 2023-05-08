# Открыть файл test_file.csv,
# прочитать, распарсить зп сотрудников в долларах и перевести в гривны на текущую дату
# (курс задается отдельной переменной).
# Результат сохранить в новый файл salaries_uah.csv


import os

def change(dollar):
    koef = 2.5
    try:
        grivna = dollar / koef
        return grivna
    except ValueError:
        print('Wrong dollar value')

file = 'test_file.csv'

if os.path.exists(file):

    with open(file, 'r') as file_dollar:
        stroki = file_dollar.readlines()

        with open('salaries_uah.csv', 'a') as file_grivna:
            file_grivna.write(stroki[0])

            for i in range(1, len(stroki)):
                employee_salary = stroki[i].split(',')
                for j in range(1, len(employee_salary)):
                    try:
                        salary = int(employee_salary[j].strip())
                        salary_grn = str(change(salary))
                        employee_salary[j] = salary_grn

                    except ValueError:
                        print('Wrong salary data')

                employee_salary[-1] = employee_salary[-1] + '\n'
                employee_salary = ','.join(employee_salary)
                file_grivna.write(employee_salary)

else:
    print(f'There is no any {file}')



