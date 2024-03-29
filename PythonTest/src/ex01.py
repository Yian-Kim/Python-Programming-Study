'''
Created on 2019. 8. 5.

@author: sist00

D:\class\python 폴더 생성

개발 도구
1. 이클립스(플러그인 - PyDev)
2. Visual Studio Code
3. PyCharm(JetBrains) - 학교 이메일 계정(*.ac.kr)
4. 파이썬 설치 > IDLE + CMD //기본 도구

1. Python
2. Node.js



커맨드 환경 > REPL 환경(Read, Eval, Print, Loop)



자료형
1. 숫자형
    - int
    - float
2. 문자형
    - str
    - 'str' , 홑따옴표 3개짜리 - 불변
    - "str", 쌍따옴표 3개짜리 - 가변
3. 논리형
    - bool(True, False)
3. 리스트.. 복합형

'''
# 주석입니다.
print(10 + 20)


# 공백문자에 대해서
for n in [1,2,3]:
    print(n)
    print(n*n)






# 파이썬 함수
# 자바스크립트
'''
function test() {
    실행문;
}
'''
def test(): #header
    print('함수입니다.')
    
test()


def sum(a, b):
    print('a : ' + str(a))
    print('b : ' + str(b))
    return a + b

result = sum(10, 20)

print('result : ' + str(result))




# 가변 인자 리스트 지원(자바에도 있음)
# - 매개변수의 갯수가 일정하지 않을 때 사용

# public void test(int... args) {}
# args : 배열 
# test(10) > args[1]
# test(10,20) > args[2]
# test(10,20,30...50) > args[5]
 
def sum_many(*args): 
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(sum_many(10))
print(sum_many(10,20,30))
print(sum_many(10,20,30,40,50,60,70,80,90,100))



# 함수 > 영역 발생 > 지역 변수 or 전역 변수
num = 10
check = "체크 완료"

if num > 0: # 제어문이 변수의 영역 역할을 하는지?
    print('양수')
    print(check)
    name = "홍길동"
else:
    print('음수')

print(name)


def hello():
    print("안녕")
    nick = "바보" # 지역 변수
    
hello()
# print(nick)











