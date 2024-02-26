import csv # используем встроенную библиотеку csv
with open('vacancy.csv', encoding='utf-8') as f: # считываем файл
    a = csv.reader(f, delimiter=';')
    salaries = {} # создаем словарь с макс. зарплатами в каждой компании, где ключом будут названия компаний
    roles = {} # создаем словарь с профессиями с макс зарплатой по компании, где ключом будут названия компаний
    companies = [] # создаем список компаний
    c = 0 # флаг, чтобы пропустить первую строчку
    for line in a:
        if c:
            try: # проверяем если есть в словарях название компании
                if salaries[line[-1]] < int(line[0]): # 
                    salaries[line[-1]] = int(line[0])
                    roles[line[-1]] = line[-2]
            except: # иначе добавляем
                salaries[line[-1]] = int(line[0])
                roles[line[-1]] = line[-2]
                if line[-1] not in companies:
                    companies.append(line[-1])
        c = 1
with open('vacancy_new.csv', mode='w', encoding='utf-8') as f: # считываем созданный файл
    a = csv.writer(f, delimiter=';', lineterminator='\n')
    a.writerow(['company', 'role', 'Salary']) # записываем названия столбцов
    for company in companies:
        a.writerow([company, roles[company], salaries[company]]) # зависываем строчки
with open('vacancy_new.csv', mode='r', encoding='utf-8') as f: # считываем созданный файл
    b = csv.reader(f, delimiter=';')
    top = [] # для удобства создадим список из файла
    c = 0 # флаг, чтобы пропустить первую строчку
    for line in b:
        if c:
            top.append([line[-1], line[0], line[1]]) # добавляем в список строки из файла в удобном для сортировки порядке
        c = 1
    for line in sorted(top, reverse=1)[:3]: # сортируем и выводим первые три строки
        print(line[1], line[2], line[0]) # выводим в нужном порядке
