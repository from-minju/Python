#머신러닝 프로그래밍 5주차 실습

# ##### 리스트 --------------------
# a = [32, 42, 11, 10]
# print(a.index(42)) #42가 들어있는 인덱스 번호가 나옴. ->1
# print(2 in a) #2가 a에 있는지 없는지 True/False로
# if 4 in a :
#     print(a.index(32))
# else:
#     print("리스트에 요소가 없습니다.")

# #print(a.count())#에러, count안에 요소 넣어주어야 함
# print(a.count(42)) #42라는 요소가 몇개 있는지 확인
#
# a.sort() #오름차순 정렬
# print(a)
# # print(a.sort()) #결과:None/ sort메소드는 반환값이 없고 a자체가 변하는것이다.
# a.sort(reverse=True) #내림차순 정렬
# print(a)
# a.sort(reverse=False) #오름차순 정렬, 그냥 reverse생략해도 오름차순
#
# a = [32, 42, 11, 10, 11]
# b=["python", "hello", "programming"]
# b.sort()
# print(b)
#
# b.sort(key=len) #문자열 길이 작은것부터 출력(문자열 길이가 같으면 오름차순으로)
# print(b)
#
#
# c = b.copy() #얕은 복사, 값 자체만 복사하여 c에 대입되기 때문에 원본 b에 영향을 주지 않게 된다.
# print(c)
# A = b #b의 주소값 자체로 대입이 되기 때문에 원본 b에 영향을 주게 된다
# print(id(A))
# print(id(c))
# print(id(b))
# A.sort() #A정렬하면 원본b도 같이 정렬이 됨. b의 주소값을 대입했기 때문
# print(A)
# print(b)
# print(c)


# ##### 튜플 (tuple) --------------------
# a = (1,2,33)
# print(type(a)) #'tuple'
# print(a)
# print(a[2]) #인덱스로도 접근 가능
# print(a[1:]) #슬라이스도 가능
# print(a[:2]) #인덱스 1까지
# #튜플은 값을 변경할 수 없다. -> 값을 바꾸고 싶으면 리스트로 변환하는 방법을 써야 한다.
# #a[0] = 10 #error
#
# list(a)
# print(list(a))
# print(type(a)) #아직도 tuple임. 원본 값을 바꿔주지는 않으므로 직접 대입해야함
# a = list(a)
# print(type(a))#list
# a[0] = 10 #list로 바꿨으니까 값 변경이 가능하다.
# print(a)
# a = tuple(a) #리스트를 다시 튜플로 바꿔줌
# print(a)
#
# b = (2, 3, 10)
# print(a+b)#튜플끼리도 연결이 가능하다


# ##### 집합 --------------------
# #중복되는 값을 포함할 수 없다.
# a = {1,2, 3, 1} #집합
# b = [1,2,3,1] #리스트 - 중복 허용
# print(a) #중복되는 값 자동 제거
# print(b) #중복을 허용하므로 중복된 값이 나온다.
#
# a = {'banna', 'mango', 'apple'}
# print(a) #순서 매길 수 없음
# #교집합을 그럼 왜 사용? -> 교집합, 차집합...
#
# b = {'mango', 'melon'}
# print(a-b)#a기준, 차집합
#
# c = set({'banana', 'apple'}) #집합 선언하는 또다른 방법
# b = set() #빈 집합
# print(c)
# print(type(b))
# #b = { } #그냥 중괄호로 쓰면
# #print(type(b)) #type은 'dict'이 됨.
#
# b.add('mango') # 집합에 값을 추가할 수도 있음
# b.add('melon')
# print(b)
# b.remove('mango') #값을 지울 수도 있음
# print(b)
#
# a = {'banna', 'mango', 'apple'}
# b = {'mango', 'melon'}
# print(a&b) #교집합
# print(a.intersection(b)) #위의 교집합이랑 같은 기능
# print(a|b) #집합을 합칠 때, 공통되는 값은 하나만
# print('banana' in a) #True - list랑 비슷한 기능
# print('banana' in b) #False

##### 딕셔너리 (dictionary) --------------------
a = { '키':100, '강영현': 100}
print(type(a)) #dict
print(a)
#인덱스로 접근하는 것이 아니라 키값으로 접근한다.
print(a['키']) #키에 해당하는 값이 나옴
#print(a[0])# ERROR - 딕셔너리는 인덱스로 접근하는거 아님

a['강영현'] = 93
print(a)

print('강영현' in a) #True
#print(100 in a) #틀림. 요소값으로 찾는거 아님. '키'값으로 찾는거임.
print('키' in a)

print(a.keys()) #키의 목록들을 가져올 수 있음 # dict_keys(['키', '강영현'])
print(type(a.keys())) # 'dict_keys'
print(list(a.keys())) #키 목록을 리스트로 바꿔줌
print(a.items()) #리스트 안에 튜플형태로 # dict_items([('키', 100), ('강영현', 93)])
print(a.values()) #키에 대한 값들만 가져옴 (<-> a.keys()는 키를 가져옴)

#sorted : 키 목록을 정렬된 리스트로 얻고자 할 때
fruits = {'banana' : 300, 'apple' : 200, 'mango' : 400}
print(sorted(fruits)) # 키값이 정렬되어 나옴(= sorted(fruits.keys()) #['apple', 'banana', 'mango']
print(sorted(fruits.values())) # 키에 대한 값들을 정렬 #[200, 300, 400]
print(sorted(fruits.items())) # 키에 대해 오름차순으로 정렬함. #[('apple', 200), ('banana', 300), ('mango', 400)]

for name in fruits:
    print(name) #자동으로 키값만 나옴

for name in fruits.items():
    print(name)  # 튜플형태로 나옴

for name, value in fruits.items(): #1번째 방법 - 튜플 벗겨내서 출력하는
    print(name, value)  # 튜플을 벗겨내고 싶으면

for name in fruits.keys(): #2번째 방법 - 튜플 벗겨내서 출력하는
    value = fruits[name]
    print(name, value)


score = { '강영현':100, '김원필':80, '박성진':90 }
for name, value in score.items():
    print("이름:{0:<5}, 점수: {1:>5}" .format(name, value)) # {0:<5} 오른쪽정렬 간격5

