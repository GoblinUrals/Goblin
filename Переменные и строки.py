c=[]
for num in range(1,15):
    c.append(num*2)
print(c)
print(f"{'hello':*<20}")
print(f'{12458:*=10}')
print('Hello world'.count('wo'))
print('Hello world'.partition('l'))
print('Hello world'.rpartition('ol'))
print('Hello world'.rpartition('l'))
a='я так думаю'
print(f'f-строка {a} интересная тема')

w='Струков Владислав Владимирович'
print('sd_afx_xccs_jcoakc'.split('_'))
print('43,543,765,3,765,432'.split(','))
print(w.split('к'))
w='Струков Владислав Владимирович'
print(','.join(w.split()))
q=['Струков', 'Владислав', 'Владимирович']
print('='.join(q))
z=['12','49','78','879','7456']
#print(','.join(z.split()))
print(' '.join(z))
