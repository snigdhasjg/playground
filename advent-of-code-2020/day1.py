with open('input/day1.txt') as file:
    report = [int(line) for line in file]

for i, each_expense_i in enumerate(report):
    for j, each_expense_j in enumerate(report):
        for k, each_expense_k in enumerate(report):
            if i != j != k and each_expense_i + each_expense_j + each_expense_k == 2020:
                print('yay', each_expense_i, each_expense_j, each_expense_k, each_expense_i * each_expense_j * each_expense_k)

if __name__ == '__main__':
    pass
