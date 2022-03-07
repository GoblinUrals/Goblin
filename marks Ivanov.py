person={}
s='IVANOV IVAN Samara SGU 5 4 5 5 4 3 5'
s=s.split()   # нарезаем строку s
person['lastName']=s[0]
person['firstName']=s[1]
person['city']=s[2]
person['university']=s[3]
person['marks']=[] # пустой список ,который заполним оценками
for i in s[4:]:
    person['marks'].append(int(i)) # добавляем оценки с 4 индекса,i-строка>int
print(s)
print(person)
