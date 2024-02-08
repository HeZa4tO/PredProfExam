from random import randint, shuffle

file_open_students = open('students.csv')
file_redact_students = open('students_new.csv', 'w')

print(file_open_students.readline())

def create_login(user: str) -> str:
    data_user = user.split(' ')
    return f'{data_user[0]}_{data_user[1][0]}{data_user[2][0]}'


def create_password() -> str:
    n_num = randint(1, 3)
    n_abc = randint(1, 2)
    n_ABC = randint(1, 3)
    n_char = 8 - n_abc - n_ABC - n_num
    num = [chr(randint(48, 57)) for _ in range(n_num)]
    abc = [chr(randint(97, 122)) for _ in range(n_abc)]
    ABC = [chr(randint(65, 90)) for _ in range(n_ABC)]
    chars = [chr(randint(33, 47)) for _ in range(n_char)]
    s = num + abc + ABC + chars
    shuffle(s)
    return ''.join(s)


def main():
    login1 = create_login('Соколов Иван Иванович')
    pass1 = create_password()

    print(login1)
    print(pass1)

    login2 = create_login('Сербин Геннадий Михаилович')
    pass2 = create_password()

    print(login2)
    print(pass2)


if __name__ == '__main__':
    main()
