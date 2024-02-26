import csv
with open('vacancy.csv', encoding='utf-8') as f: #
    a = csv.reader(f, delimiter=';')
    roles = {}
    company_size = {}
    salaries = {}
    companies = []
    c = 0
    for line in a:
        if c:
            try:
                if company_size[line[-1]] < int(line[2]):
                    company_size[line[-1]] = int(line[2])
                    roles[line[-1]] = line[-2]
                    salaries[line[-1]] = line[0]
            except:
                company_size[line[-1]] = int(line[2])
                roles[line[-1]] = line[-2]
                salaries[line[-1]] = line[0]
                if line[-1] not in companies:
                    companies.append(line[-1])
        c = 1
    min1 = float('inf')
    com = ''
    for company in companies:
        if roles[company] == 'классный руководитель':
            if min1 > company_size[company]:
                min1 = company_size[company]
                com = company
    print(f'В компании {com} есть заданная профессия: {roles[com]}, з/п в такой компании составит: {salaries[com]}')