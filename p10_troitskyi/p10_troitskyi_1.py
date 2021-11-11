salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]

def Calc(salaries):
    return list(map(lambda i: round(i * 1.3, 2), salaries))

print('Salary table:',
'\n',salary_list,
'\n',Calc(salary_list))