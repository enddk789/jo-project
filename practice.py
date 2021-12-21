

# #t사전 만드는법
# cavinet = {3:"유재석", 100: "김태호"}
# print(cavinet[3])
# print(cavinet[100])
# print(cavinet.get(3))

# print(3 in cavinet )
# print( 5 in cavinet)

# #사전에 새로 추가하는법

# cavinet["c-20"] = "조세호" 

# #사전에 제와시키는법

# del cavinet["c-20"]  

# print(cavinet)

# # key들만 출력

# print(cavinet.keys())

# # value들만 출력

# print(cavinet.values())

# # key, value들만 출력

# print(cavinet.items())

# #완전히 지우기

# cavinet.clear()


# #  튜블-----------------------------------

# menu = ("돈까스", "치즈 까스")

# print(menu[0])
# print(menu[1])

# #튜플에 항목 추가하기가 안됨

# name = "김종국"
# age = 20
# hobby = "코딩"

# print(name, age, hobby) 

# # 튜플로 값 한번에 적용시키기

# (name, age, hobby) = ("김종국", 20, "코딩")


# #세트 (set) 내가 아는 수학에서의 집합임 교집합 합집합 등--------------------------------------- 
# #중복 안됨, 순서 없음

# my_et = {1,2,3,3,3} 

#  #임의의 집합 만들기

# java = {"유재석", "김태호", "양세형"}

# # 다른방법으로 집합 만들기

# pytho = set(["유재석", "박명수"])

# # 교집합 하는 방법

# print(java & pytho)

# # 교집합을 하는 다른 방법

# print(java.intersection(pytho))

# # 합집합 하는방법 

# print(java | pytho)

# # 합집합의 다른 방법

# print(java.union(pytho)) 

# # 차집합을 하는 방법

# print(java - pytho)

# # 차집합을 하는 다른 방법

# print(java.difference(pytho))

# # pytho을 할줄 하는 사람이 늘어남 set에 값을 추가하는 방법

# pytho.add("김태호")

# # set에서 값을 제외 시키는 방법

# java.remove("김태호")


# # 자료구조의 변경 
# #커피숍

# menu = {"커피", "우유", "주스"}

# print(menu, type(menu))


# # 리스트로 자료 구조를 바꾸는법

# menu = list(menu)

# print(menu, type(menu)) #type() 부분은 자료의 구조형을 보여주는 함수

# #튜플로 바꾸는법

# menu = tuple(menu)

# #다시 set으로 바꾸는법

# menu = set(menu)

# #퀴즈 4----------------------------------

# from random import * 

# users = [1, 2,3, 4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] #만약 리스트를  하나하나 쓰기 싫을때 range()함수 사용 예를 들어 1~20까지 하고 싶으면 range(1, 21)까지 하기

# # !!! range함수를 쓸경우 타입이 range이기 때문에 users(변수명) = list(users)하기

# shuffle(users)

# a = sample(users, 1)


# b = sample(users, 3)


# print("-- 당첨자 발표 -- \n 치킨 당첨자 : " + str(a) + "\n커피 당첨자 : " + str(b) + "\n -- 축하 합니다 --")

# #if문----------------------------------------------------------------------------------------------

# weather = "비"

# if  weather == "비":
#     print ("우산을 챙기세요")
    
# # 만약 변수가 정수형일때

# #temp = int(input("기온은 어때요? "))#input = 사용자의 입력을 받음 int = 기온이 숫자이기 때문에 정수형 자료형으로 감싸줌

# #for문--------------------------------------------

# for i in range(1, 61):
#     print(i)


# #리스트 for문

# starbucks = ["아이언맨", "토르", "헐크"]

# for customor in starbucks:
#     print("{0}, 커피가 준비 되었습니다.".format(customor))


# # while문

# #무한루프

# # while True:
# #     print("파이썬 잘하고 싶다.") #무한루프 프로그램을 끝내고 싶을때는 ctrl + c

# # 조건이 만족할때까지 계속 돌리고 싶을때

# # customor = "토르"
# # person = "Unknown"
# # while person != customor:
# #     print ("{0}, 커피가 준비되었어요.".format(customor))


# #한줄 for문

# #출석 번호가 1, 2,3,4, 앞에 100을 붙이기로 함 -> 101 102 103 104 105

# students = [1, 2, 3, 4, 5]

# students = [i + 100 for i in students] # i에 students를 넣어주고 그 i에 100을 더해주는 구문


# # 길이를 알아내고 싶을때 len(사용)
 
# import random

# custermor = list(range(1, 51))

# cartime = list(range(5, 51))

# random.shuffle(cartime)

# for i  in custermor:
#     if cartime >= 5 & cartime <= 15:
#         print("[0] {0}번째 손님 (소요시간 : {1}분".format(i, cartime))
#     elif cartime <=5 & cartime >=15:
#         print("[] {0}번째 손님 (소요시간 : {1}분)".format(i, cartime))

print("성별을 입력해주세요 : ")
gen = std(input())
print("키를 입력해주세요 : ")
heig = std(input())
def std_weight(gen, heig):
    if gen == "남자":
        manheig = round(heig * heig * 22, 2)
        return manheig
    elif gen == "여자":
        girlheig = round(heig * heig * 21, 2)
        return girlheig
    else:
        print("잘못 입력했습니다.")

age_weight = std_weight(gen, heig)

print("키" + heig + "cm" + gen + "의 표준 체중은 {0} 입니다.".format(age_weight))