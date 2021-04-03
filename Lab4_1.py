#Lab4_1

print("학번: 201904001  이름: 강민주")
print("덧셈을 하고싶은 정수들을 입력하세요! 0을 입력시 종료됩니다.") #안내멘트 출력

sum = 0 #합을 저장할 변수를 0으로 초기화

while True:
    user = int(input()) #사용자로부터 정수를 입력받는다
    if user != 0: #0이 아니면
        sum += user #sum이랑 입력한 값을 더해서 다시 sum에 저장
    else:
        break #0을 입력하면 while문을 빠져나감

print("총 합은 ", sum, "입니다.") #총 합을 출력