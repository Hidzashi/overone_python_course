#task_1
# countries = {
#     'Belarus': ['Minsk', 'Brest', 'Gomel', 'Mir'],
#     'Ukrane': ['Kyiv', 'Lviv', 'Luhansk','Chernigiv'],
#     'Spain': ['Madrid', 'Barselona', 'Tenerife']
# }
# city = input('city - ').title()
# c = 0
# for key, val in countries.items():
#     if city in val:
#         print(f'city - {city} in {key}')
#         c = 1
# if c == 0:
#     print('no city')

#task_2

users = {
    123: {
        'name': 'Vasya',
        'last_name': 'Vasyin',
        'phone': '375293456789',
        'email': 'qwerty@gmail.com'
    },
    234: {
        'name': 'Tanya',
        'last_name': 'Vasyina',
        'phone': '375293456099',
        'email': ''
    },
    345: {
        'name': 'Kate',
        'last_name': 'Mishina',
        'phone': '375293456649',
    }
}
res = ''
for val in users.values():
    if val.get('email') == None or val['email'] == '':
        res += val['name'] + ' '
print(res)
