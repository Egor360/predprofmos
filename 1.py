import csv
with open('vacancy.csv', encoding='utf-8') as f:
    a = csv.reader(f, delimiter=';')
    salaries = {}
    roles = {}
    companies = []
    c = 0
    for line in a:
        if c:
            try:
                if salaries[line[-1]] < int(line[0]):
                    salaries[line[-1]] = int(line[0])
                    roles[line[-1]] = line[-2]
            except:
                salaries[line[-1]] = int(line[0])
                roles[line[-1]] = line[-2]
                if line[-1] not in companies:
                    companies.append(line[-1])
        c = 1
with open('vacancy_new.csv', mode='w', encoding='utf-8') as f:
    a = csv.writer(f, delimiter=';', lineterminator='\n')
    a.writerow(['company', 'role', 'Salary'])
    for company in companies:
        a.writerow([company, roles[company], salaries[company]])
with open('vacancy_new.csv', mode='r', encoding='utf-8') as f:
    b = csv.reader(f, delimiter=';')
    top = []
    c = 0
    for line in b:
        if c:
            top.append([line[-1], line[0], line[1]])
        c = 1
    for line in sorted(top, reverse=1)[:3]:
        print(line[1], line[2], line[0])