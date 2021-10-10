#or a b중 둘중하나면 됨
a= True
b= False
c= True
d= False
print(a or b)
print(a | c)
#and 둘다 참이여야 참
print(a and b)
print(a & c)

#nor  둘중하나만 참이여아함
print(a ^ b)
print(a ^ c)

# == 같음
print(a==b)
print(a==c)

#(^ 연산자는 ==의 반대라고 생각하면 편함)
#연산자 생각할때는 드모르간 법칙을 염두하면 편할때가 있음