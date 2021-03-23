#3주차

print("김원필"*3)

str2= "강영현 사랑해"
print(str2[0:3])
print(str2[4:])
print(str2[:-1])
print(str2[1:3])

phone = '01012345678'
print(phone[0:3])

print(len(str2))
print(len("김원필 사랑해"))

#사용자 입력 함수
youngk = input("강영현의 생년월일을 입력하시오")
print(type(youngk))

#sum = youngk + 121 #에러뜸 youngk는 문자열이라서 숫자랑 못더함
#print(sum)

sum = int(youngk)+1219
print(sum)

wonpil = int(input("김원필의 생년월일을 입력하시오")) #이렇게하면 바로 int형으로 바뀜
print(wonpil)
sum = wonpil +121
print(sum)