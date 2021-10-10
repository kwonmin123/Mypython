print("a"+"b")
print("a","b")

#방법 1
print("나는 %d살 입니다" %20)
print("나는 %s 입니다" %"소방관")
print("나는 알파벳 %c가 좋습니다 " %"A")
print("나는 %s 또는 %s도 좋습니다 " %("자바" ,"파이썬"))

#방법 2

print("나는 {}살 입니다".format(20))
print("나는 {}또는 {}입니다".format("경찰관","소방관"))
print("나는 {0}또는 {1}입니다".format("경찰관","소방관"))
print("나는 {1}또는 {0}입니다".format("경찰관","소방관"))
print("나는 {1}또는 {1}입니다".format("경찰관","소방관"))

#방법 3
print("나는 {age}살 {job} 입니다".format(age=20,job="히어로"))
print("나는 {str1}또는 {str2}입니다".format(str1 ="경찰관",str2="소방관"))


#방법 4
age=30
job="hero"
print(f"안녕하세요 저는 {age}살 {job}입니다")