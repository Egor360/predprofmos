import csv # используем встроенную библиотеку csv
with open('vacancy.csv', encoding='utf-8') as f: # считываем файл
    a = csv.reader(f, delimiter=';')
    roles = {} # создаем словарь с профессиями по мин. кол-ву сотрудников, где ключом будут названия компаний
    company_size = {} # создаем словарь с мин. кол-вом сотрудников, где ключом будут названия компаний
    salaries = {} # создаем словарь с зарплатами по мин. кол-ву сотрудников в каждой компании, где ключом будут названия компаний
    companies = [] # создаем список компаний
    c = 0 # флаг, чтобы пропустить первую строчку
    for line in a:
        if c:
            try: # проверяем если есть в словарях название компании
                if company_size[line[-1]] < int(line[2]):
                    company_size[line[-1]] = int(line[2])
                    roles[line[-1]] = line[-2]
                    salaries[line[-1]] = line[0]
            except: # иначе добавляем
                company_size[line[-1]] = int(line[2])
                roles[line[-1]] = line[-2]
                salaries[line[-1]] = line[0]
                if line[-1] not in companies:
                    companies.append(line[-1])
        c = 1
    min1 = float('inf') # создадим переменную с макс. значением, в которую позже запишем мин. требуемое значение
    com = '' # сюда запишем компанию соответствующую значению переменной выше
    for company in companies: # ищем по компаниям
        if roles[company] == 'классный руководитель':
            if min1 > company_size[company]:
                min1 = company_size[company]
                com = company
    print(f'В компании {com} есть заданная профессия: {roles[com]}, з/п в такой компании составит: {salaries[com]}') # выводим
