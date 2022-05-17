
import user

if user.belhard_student:
    status = 'I am Bellhard student'
else:
    status = 'I am not Bellhard student'

print( f'My name is {user.name}{user.surname}\n'
       f'I am {user.age} years old\n'
       f'{status}')
