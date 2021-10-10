str1 = "My life is Beautiful, Python"
print(str1)
print(str1.lower())
print(str1.upper())
print(str1[0].isupper())
print(len(str1))
print(str1.replace("Python", "Java"))
print(str1.replace(" ", ""))
print(str1.replace("", ""))
index =str1.index("i")
print(index)
index =str1.index("i",index+1)# 그 다음 i의 위치 출력함
print(index)
print(str1.index("Python"))
print(str1.find("i"))
print(str1.find("java"))
# print(str1.index("java")) 오류내고 프로그램 종료 자바가 없기때문
print(str1.count("i"))