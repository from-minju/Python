#while문

# energy = 3
# while energy > 0:
#     print("달려라 고고싱")
#     print("|energy=", energy)
#     energy -= 1 #에너지를 1만큼 소비
# else :
#     print("못달려잉")
#
# youngk = "강영현"
# wonpil = "김원필"
#
# while True:
#     pyeong = int(input("평수는?"))
#     m2 = pyeong *3.31
#     s = "{0}평은 {1}제곱미터입니다." .format(pyeong, m2)
#     print(s)
#     print("{0}이랑 {1}은 최고야" .format(youngk, wonpil))

# 파이썬 프로그램을 강제로 끝내는 방법 : Ctrl + C키 (무한루프에 들어와도 Ctrl + C키로 종료 가능

#무한루프에 주의! -> 사용자가 강제로 끝내지 않으려면 break문을 통해서 루프 탈출할 방법

#평수는?
# while True :
#     pyeong = input("평수는?")
#     if pyeong == "" or pyeong == "q":
#         break
#     m2 = int(pyeong) * 3.31
#     print("{0}평은 {1}제곱미터입니다.".format(pyeong, m2))

#범위 반복을 위한 for문
# for i in range(5):
#     print(i)
#
# v = 0
# for i in range(1, 11):
#     v = v + i
#     print(i, "을(를) 더하면", v)
# print("1에서 10까지 모두 더하면...", v)

#range()함수

#범위 반복을 위한 for문 예제3

#화면에 300개의 세로 선을 긋는다
# from tkinter import * #그래픽 라이브러리를 도입한다
# w = Canvas(Tk(), width=900, height=400) #화면 초기화
# w.pack()
#
# for i in range(300): #0~299
#     x = i * 3
#     w.create_line(x, 0, x, 400, fill = "#FF0000") #(x,0)에서 (x,400)까지 이어지는 선 생성, #FF0000 : R(FF) G(00) B(00)
#
# mainloop()


#범위 반복을 위한 for문 예제2
# from tkinter import * #그래픽 라이브러리를 도입
# w = Canvas(Tk(), width=90, height=400) #화면 초기화
# w.pack()
#
# for i in range(100):
#     x = i * 9
#     if i % 2 == 0:
#         c = "ff0000" #빨강색
#     else:
#         c = "#0000FF" #파랑색
#     w.create_line(x,0,x,400,fill=c)
#
# mainloop()

#반복을 중지하는 break와 continue
#FizzBuzz
# for i in range(1,21): #1~20
#     if i%15==0:
#         print("Fizz Buzz")
#         continue
#     if i%3==0:
#         print("Fizz")
#         continue
#     if i%5==0:
#         print("Buzz")
#         continue
#     print(i)


#반복문에서 else블록을 사용할 경우 예제1
# foodstuff = ["Banana", "Mango", "Fish", "Carrot", "cabbage"]
# #망고가 있는지 확인
# flag_found = False
# for food in foodstuff:
#     if food == "Mango"
#         flag_found=True
#         break
# if flag_found:
#     print("망고가 들어 있습니다.")
# else:
#     print("없습니다.")

#반복문에서 else블록을 사용할 경우 예제2
# foodstuff = ["Banana", "Mango", "Fish", "Carrot", "cabbage"]
# #망고가 들어 있는지 확인한다
# for food in foodstuff:
#     if food == "Mango":
#         print("망고가 들어 있습니다.")
#         break
# else: #if문이 수행되지 않았을 경우(=break문이 실행 안되었을 경우)
#     print("없습니다.")

#for와 조합해 리스트를 한번에 처리 방법
# points = [88, 76, 67, 43, 79, 80, 91]
# sum_v = 0
# for i in points:
#     sum_v+=i
#     print(i, "점을 더한 합계는 ", sum_v)
#
# ave = sum_v / len(points)
# print("평균점은 ", ave, "점")

#리스트 값의 합계를 한번에 계산하는 sum()함수
# points = [88, 76, 67, 43, 79, 80, 91]
# sum_v = sum(points)
# ave = sum_v / len(points)
# print("합계점은 ", sum_v, "점")
# print("평균점은 ", ave, "점")

#이름을 무작위로 표시하는 프로그램 예제
# import random
# name = ["박성진, 박제형, 강영현, 김원필, 윤도운"]
# i = random.randint(0, len(name)-1) #무작위로 수치를 하나 고른다.
# print(name[i])
#n부터 m까지의 수치 중에서 무작위로 선택된 값을 구할 수 있음

#for구문에서 인덱스 번호를 사용한 반복
# fruits = ["Apple", "Orange", "Banana"]
# for i,v in enumerate(fruits):
#     print(i, v)
# print(list(enumerate(fruits)))

# #리스트에 요소 추가 append()
# num = [1, 2, 3]
# num.append(4) #append()로 값 추가
# num.append(5)
# print(num)

#리스트에 요소 추가 : append() 예제
# #국어 시험 점수 목록
# points = [80, 40, 23, 14, 29, 58]
#
# #30점 이하의 데이터만을 선택해서 낮은 점수 리스트에 추가
# lowscore = [] #빈 리스트
# for p in points:
#     if p < 30:
#         lowscore.append(p)
# print(lowscore) #결과 : [23, 14, 29]

# #리스트 요소 슬라이스
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(b[2:8:2]) #인덱스 2~7까지 중에 2번째 값들
# #결과 : [3, 5, 7]
#
# print(b[::3])#처음~끝까지 3번째에 등장하는 데이터 값 출력
# #결과 : [1, 4, 7]

# #del키워드
# num = [0, 1, 2, 3, 4]
# del num[2]
# print(num) #결과 : [0, 1, 3, 4]
#
# num = [0, 1, 2, 3, 4]
# del num[2:4]
# print(num) #결과 : [0, 1, 4]

# #pop() 함수
# num = [0, 1, 2, 3, 4]
# num.pop(1) #인덱스1에 있는 요소를 삭제
# print(num) #결과 : [0, 2, 3, 4]
#
# num = [0, 2, 3, 4]
# num.pop() #아무것도 안쓰면 자동으로 마지막 요소가 삭제됨
# print(num) #결과 : [0, 2, 3]

# #remove
# num = [0, 1, 2, 3, 4, 2, 5]
# num.remove(2)
# print(num) #결과 : [0, 1, 3, 4, 2, 5]

# #clear
# num = [0, 1, 2, 3, 4, 2, 5]
# num.clear()
# print(num) #결과 : []