#문자열 함수

str = "hello world!!!"
print(str.split()) #['hello', 'world!!!'] #원본파괴X
print(str.replace("!!!", "~~~")) #hello world~~~
print(str) #hello world!!! #자체가 변하지는 않음!! 반환값만 대치해서 주는거임

print(str.find("hello")) #0 #인덱스 값이 나옴.
print(str.find("world")) #6
print(str.find("world", 0, 6)) #-1 #0부터 6사이에 world가 있니?->없음(-1)
print(str.find("hello", 0 ,6)) #0

str = "Hello world!!!"
print(str.lower()) #소문자로 바꿔주는 함수
print(str.upper()) #대문자로
print(str) #lower, upper도 역시 원본파괴X

str1 = ","
list1 = ["hello", "hi"]
print(str1.join(list1)) #hello,hi #list1을 str1로 결합

str = "!!!Hello world!!!"
print(str.rstrip("!!!")) #!!!Hello world #왼쪽에 있는 !!!만 지워짐
print(str.lstrip("!!!")) #Hello world!!! #오른쪽에 있는 !!!만 지워짐
print(str.strip("!!!")) #Hello world #양쪽에 있는 !!! 지워짐
#공백을 제거하고싶으면 그냥 str.strip()
#strip도 원본파괴X

str = "Hello world"
print(str.startswith("Hello"))#True #Hello로 시작하니?
print(str.startswith("hello"))#False #hello로 시작하니?

print(str.isnumeric())#False # 문자열 전체가 숫자로 이루어져있니?->거짓
str2 = "123"
print(str2.isnumeric()) #True
print(str2.isalpha()) #알파벳이니? #isnumeric말고도 많이 있음


#함수
def sum(a, b):
    '''a와 b를 더해주는 함수'''
    print("hello", a)
    return a+b
print(sum(1, 2))

help(sum) #docstring 확인 가능
# Help on function sum in module __main__:
#
# sum(a, b)
#     a와 b를 더해주는 함수
help(print)

#재귀함수
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

print(fact(5)) #120

def sum(a, b=0):
    print("a={0} b={1}".format(a, b))
    return a+b
print(sum(1)) #b는 자동으로 0
print(sum(a=1))#키워드인수
#a랑 b둘다 기본값 지정 안한 상태에서 그냥 print(sum(1))하면 ERROR가 뜬다.

def sum(a=1, b=2):
    return a+b
print(sum(1))#3 #1은 a값이됨, b는 기본값으로
print(sum(b=2, a=4))#6 #키워드인수는 a와 b순서 상관없음

#가변개수인수
def sum(*a):
    print(a)
    print(type(a)) #<class 'tuple'>

sum(1,2,3,4,5,6)#(1, 2, 3, 4, 5, 6) #함수호출 #1,2,3,4,5,6이 "튜플"형태로 넘어간다

def sum(**a):
    print(a)
    print(type(a)) #<class 'dict'>
    for name, value in a.items():
        print(name, value)

#sum(1,2,3,4,5,6)#ERROR #딕셔너리 형태로 넘겨주려면 키와 값이 있어야 함
sum(홍길동='80', 이순신='90')