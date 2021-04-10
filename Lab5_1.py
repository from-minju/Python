import random #난수를 생성하기 위해 random모듈 추가

print("학번: 201904001  이름: 강민주")
num_stu = int(input("몇명의 학생 데이터를 입력받겠습니까? ")) #데이터를 받을 학생 수

if num_stu == 0: #사용자가 0을 입력한 경우
    print("0을 입력하셨습니다.")
    print("프로그램을 종료합니다.")
    exit() #프로그램 종료

records = {} # 학생데이터를 저장할 빈 딕셔너리
for i in range(1, num_stu+1): #학생 수만큼 반복
    print(i, "번째 학생 성적")
    name = input("이름: ") #입력받은 학생이름
    score = int(input("점수: ")) #입력받은 학생점수

    def No_duplicate_name(name): #중복없는 이름을 반환하는 함수
        while name in records.keys(): #중복된 이름이 있는경우
            n = str(random.randrange(1, 100)) #0~99 난수 생성
            name += n #사용자가 원래 입력한 이름에 난수를 붙여준다.
            No_duplicate_name(name) #같은 이름에 같은 난수가 붙어 또 중복될 수 있으므로 재귀함수를 통해 중복을 완전히 없애준다.
        return name #중복없는 이름을 반환해준다.

    records[No_duplicate_name(name)] = score #딕셔너리에 값 추가
    print("입력완료\n")

score_list = records.values() #딕셔너리의 값들을 리스트로 바꿔 score_list에 대입
sum = sum(score_list) #학생들의 점수 리스트에 sum함수를 적용해 합계를 구한다.
print("합계점: ", sum) #총 합을 출력
avg = sum / len(score_list) #평균을 구한다.
print("평균점: ", avg)

print("|이름    | 점수 | 차이")
for name, score in records.items():
    print("|{0:<5}|{1:>5}|{2:5}".format(name, score, score - avg)) #결과를 출력
