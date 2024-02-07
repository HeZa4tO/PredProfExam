file_open_students = open('students.csv')

for line in file_open_students.readlines():
    data = line.split(',')
    if data[4] == 'None\n':
        data[4] = 0
    print(data)
    if 'Хадаров Владимир' in data[1]:
        ocenka = int(data[4])
        id_work = data[2]
        1
