d={
    'admin':'admin',
    'user':'login1',
    'charlie11':'zupa',
    'joker':'haslohaslo',
    '55jr':'kotkipieski123',
    'oo22':'oo22haslo'
}
login=input('podaj login:')
haslo=input('wprowadź haslo:')

if login in d and d[login]==haslo:
    if login=='admin':
        print('Witaj w panelu admina!')
    else:
        print('Witaj na stronie!')
else:
    print('Login lub hasło nieprawidłowe.')
