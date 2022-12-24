# 첫 번째 문제
# split ('sep', 'maxsplit')의 형식으로 구성됨
# 아무것도 지정하지 않는다면 최대한 자른 리스트를 구성
# Split 또한 ()을 붙여주어야 한다는 점

# map (function,  iterable1,iterable2 ...) 다른 말로 (적용시킬 함수, 적용할 값들)
# 반복적으로 바꾸거나 적용시키는 것을 단축시키는 데에 사용가능함

# A, B = input().split()
# print (int(A)+int(B))

# 두 번째 문제
# %와 /는 엄연히 다른 존재라는 것을 인지할 필요성이 있음
# 파이썬의 경우에는 각 개별 print문 마다 자동으로 줄 바꿈이 진행된다는 점

# A, B, C = map(int, input().split())
# print((A+B)%C)
# print(((A%C) + (B%C))%C)
# print((A*B)%C)
# print(((A%C) * (B%C))%C)

# 세 번째 문제
# 현재로써는 리스트로 세자리 수를 입력받아서 계산을 진행하는 방식으로 풀이할까 고민됨
# 내가 이해하기로는 .split() 함수의 경우에는 자동으로 리스트로 받는 걸로 아는데 왜 map 안쓰면 안돌아가
# 변수가 두개면 그냥 받아지기 때문에 그렇다고 하네요

# a = int input()
# b = int input()
# print(a*(b%10))
# print(a*((b%100)//10))
# print(a*(b//100))
# print(a*b)

# 아니 고양이 문제 시발 저거 화나게 하는거 아니냐 그냥 한번만 하면 되지 저딴걸 넣네

# a,b = map(int, input().split())
# if a > b :
#   print(">")
# elif a < b :
#   print("<")
# else:
#   print("==")

# 20단위가 아니라 10단위라는 점 그리고 한가지 조건으로 사용하는 것도 가능함
# a = int(input())
# if 90 <= a <=100:
#   print("A")
# elif 80 <= a <=89:
#   print("B")
# elif 60 <= a <=69:
#   print("C")
# elif 40 <= a <=59:
#   print("D")
# else:
#   print("F")


# 나도코딩의 예제

# import random as r
# count = 0
# for i in range (1,51):
#     time = int(r.randrange(5,51))# 항상 하는 실수로 50미만이니까 51까지 해야지
#     if 5 <= time <=  15:
#         print ("[0] {0}번째 손님 (소요시간 : {1})" .format(i,time))
#         count= count +1
#     else :
#         print ("[ ] {0}번째 손님 (소요시간 : {1})" .format(i,time))
#     i = i+1
# print("총 탑승 승객 : {}분".format(count))

# 함수를 만들어봅시다 
# def open_a():
#     print("새로운 계좌 생성 완료")
# def deposit(balance , money):
#     print("입금 완료 잔액은 {0}원입니다.".format(balance+money))
#     return balance+money

# 위의 형식으로 함수를 설정하는 것이 가능함
# 괄호 안에는 입력 받아야 하는 인자, return에서는 되돌려줄 값읆 정하는 방식이어야 함

# 백준 문제
# and or 를 잘 구분 할줄 알아야한다는 점이 중요함
# & |의 경우에는 집합의 연산에서만 사용가능하다는 점 인지해야

# a = int(input())
# if (a%4 == 0 and ((a%100) != 0 or a%400 == 0 )):
#   print("1")
# else:
#   print("0")

# 백준 문제 2트
# 더 간결하게 할 필요 없는건지 이해가 안되네\

# x = int(input())
# y = int(input())

# if 0 < x and 0 < y:
#   print("1")
# elif x<0 and 0<y:
#   print("2")
# elif x<0 and y<0:
#   print("3")
# else:
#   print("4")

# 기본값 
# def profile(name, age=17, main ="파이썬"):
#     print("dddd")
# 이처럼 입력하는 값에 기본값을 설정하는 것이 가능하다는 점
# 매개변수의 값을 키워드를 이용해서 집어넣게되면 순서가 뒤바뀌어도 상관없이 들어감

# 가변인자를 이용한 프로필
# 사소한 팁으로 end = ""을 이용하면 줄 바꿈이 자동으로 이루어지지 않음

# def profile(name, age=17, lang1, lang2):
# def profile(name, age=17, *lang ):
# 위에서처럼 가변 인자를 활용해서 개수를 지정하지 않고도 동일한 함수를 이용하는 것이 가능
# 한줄 for문의 경우에는 한번에 지정하는 것이 가능

# 지역 변수와 전역변수
# 지역변수의 경우에는 함수의 정의 안에 초기화 되지 않는다면 사용불가능
# global이라는 말을 스고 변수를 사용하면 바로 사용하는 것이 가능함
#   함수에서 외부의 변수를 가져온다고 하더라도 함수내에서 변경된 값은 외부에 적용되는 것이 아님
#   그래서 리턴을 이용해서 값을 되돌려 주는것이 필요함

# 정확하게 잘했다라는 느낌이 든다
# def normal_weights(height, gender):
#    height_C =height/100
#    if gender == "man":
#      print("키 {0}cm 남자의 표준 체중은 {1} 입니다.".format(height , height_C*height_C*22))
#    else:
#      print("키 {0}cm 여자의 표준 체중은 {1} 입니다.".format(height , height_C*height_C*21))

# height = int(input("키를 입력하세요.(cm) : "))
# gender = str(input("생물학적 성별을 입력하세요. : ")) 
# normal_weights(height, gender)


# print 문 안에 .ljust(6) 하면 왼쪽에 6칸 확보 후에 정렬한다는 의미
# .item를 이용해서 튜플안에 있는 키와 벨류값을 모두 불러오는것이 가능하다
# z.fill(3) 값이 없는 빈공간을 0으로 채운다는 의미

# 빈 자리는 빈공간으로 두고 오른쪽 정렬을 하되 총 10자리 정렬을 확보
# print("{0: >10}".format(5000))
# # 양수일때는 플러스 음수일때는 마이너스로 표시
# print("{0: >+10}".format(-5000))
# # 왼쪽 정렬하고 빈칸으로 0을 채움
# print("{0:0 <10}".format(5000))
# # 3자리마다 콤마 찍어주기(플러스 부호까지 입력드가자)
# print("{0:+,}".format(5000))
# print("{0:2f}".format(5000))
# # 위의 경우에는 소수점 둘째자리에서 반올림

# score_file = open("score.txt", "w",encoding="utf8")
# # w는 쓰기의 의미를 가지고 있고. a는 더하기의 의미를 가짐 r은 읽기의 의미
# print(score_file.readline(), end= "") # 의 형식으로 줄별로 읽는 것이 가능
# #몇 줄인지 모를때에는
# while True:
#     line =score_file.readline()
#     if not line:
#         break
# #위의 다른 방법으로는 리스트 형식으로 저장함으로서 다르게 하는 방법이 있음
# print(score_file.readlines(), end="") 
# print("수학 80 ", file=score_file)
# score_file.close

# # pickle을 이용하면 파일을 여는 형식(이미 bineary)을 지정하지 않고도 열고 불러오는 것이 가능
# import pickle
# profile_file = open("profile.pickle","wb")
# profile = {"이름 ": "박명수", "나이": 30}
# print(profile)
# pickle.dump(profile,profile_file)

#with를 사용하면 close문을 사용할 필요가 없다는 점이 장점

# 나도 코딩의 예제 

import pickle as p
for i in range(1,51):
    review_file = open("review_file.{0}", "w", encoding="utf8" .format(i))
    print ("-{0}주차 주간 보고-".format(i))
    print ("부서 : /t")
    print ("이름 : /t")
    print ("업무 요약 : /t")
    review_file.close()

# 나의 방식과는 다르게 with를 활용해서 실행을 함 또한 str을 활용하여 적절하게 진행한다는 점이 흥미로운 점
# 예시
 
for i in range (1,51):
    with open(str(i) + "-{0} 주차 주간보고 -".format(i))
    review_file.write("thasdfas")









