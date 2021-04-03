#Lab4_2

print("학번: 201904001  이름: 강민주")
num = int(input("정수를 입력하세요: ")) #사용자로부터 정수를 입력받아서 num에 저장

result = [] #3의 배수를 저장할 리스트
for i in range(1, num+1): #1~num까지
    if i%3 == 0:
        result.append(i) #3으로 나누어 떨어지면 그 값을 리스트에 추가
print("1부터 {0}까지 3의 배수는 {1}이고, 3의 배수의 합은 {2}입니다." .format(num, result, sum(result))) #최종결과 출력
