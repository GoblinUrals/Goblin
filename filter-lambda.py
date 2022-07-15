a = filter(lambda x:x%2==0, (1,2,3,4,5,6,7,33))
print(list(a))

a = [4,5,lambda:print('work'),7,8]
print(a[2]())

b = [5,3,0,-6,8,10,1]
r = filter(lambda x: x>0 and x%2==0, b)
print(list(r))