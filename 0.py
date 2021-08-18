'''print("Hello python")

a=123
print(type(a))

b=456
print(type(a))

print(a*b)

c="안녕하세요"
print(c)
print(type(c))

d,e,f,g = 0,0,0,0 
hap =0
d=int(input( ))
e=int(input( )) #값 입력 받는거
f=int(input( ))
g=int(input( ))
hap = d+e+f+g
print("합은 => %d" %hap) #출력시 %d %a 조합'''

'''aa=[]
aa.append(100)
aa.append(200)
aa.append(300)
aa.append(400)
aa.append(500)

print("리스트 변수 크기는 %d" %len(aa)) #len() 리스트 길이
print(aa)

bb=[]
for i in range(0,100): #for 문 0부터 100까지
    bb.append(i)
print(bb)'''


'''aa=[[1,2,3,4],[4,5,6,7],[8,9,10,11,12]]

print(aa[0]) # aa리스트의 첫번째 리스트 전체 출력
print(aa[0][1]) ## aa리스트의 첫번째 리스트의 첫번째 요소 출력
print(aa[1][3]) ## aa리스트의 두번째 리스트의 세번째 요소 출력'''

'''#딕션리 타입 변수 선언
dict = {'번호':10, '성명': '김태호', '나이':23, '사는곳':'천안'}
print(dict)
print(type(dict))
print(dict['나이'])
dict['나이']=30 # dict의 나이의 요소를 바꾸고 출력
print(dict['나이'])
dict['직업']='배우'#dict의 직업에 배우를 추가하고 출력

print(dict)
print(dict.keys()) #키값 번호 성명 나이 사는곳 직업 
print(dict.values()) #10 김태호 23 천안의 요소값 출력

print('사는곳' in dict) # 사는곳이라는 키의 요소가 들어가 있나? 없으면 false
del dict['사는곳']
print('사는곳' in dict) # 사는곳 지워서 false가 나옴
print(dict) '''

'''sum = 0
for i in range (1,11,1): #초기 1 증감 1 조건값 <11 이니 (1~10까지 더함)
    sum +=i
print('1~11더한값은 %d' %sum)'''

'''#for문을 이용하여 1에서 10까지 식과 합을 구하시오
sum=0
for j in range(1,11,1):
    if j<10:
        print("%d+" %j , end ="")
    elif j==10: #파이썬은 else if가 아닌 elif 조건식 끝에는 ; 이게 아니라 : 이거
        print("%d = " %j, end="")
    sum +=j

print("%d" %sum)'''

'''#while문으로 입력한 숫자만큼 str 출력
str='이이의으이의읭'
i=int(input("반복하고 싶은 숫자 입력하세요"))
j=0

while 1: #while문 조건 1로 잡으면 돌아는가지만 남이 볼때 가독성이 떨어지거나 상태를 알때 무리가 있을수 있음
         #flag = True 라는 변수로 새로 잡아서 하는 방식이 좋음
    if i<=j:
        False
    else:
        print(str)
    j=j+1'''

'''#for문과 break문을 이용하여 1에서 20까지 합하다 100보다 작고 가장 가까운 합을 구하라
sum=0
for i in range(1,50,1):
    sum+=i
    if sum > 100:
        break;
sum=sum-i
print("%d" %sum)'''

'''#while문과 break 문을 이용하여 1부터 입력한 숫자까지의 합을 구하시오
sum, i=0,1
j=int(input("숫자 입력"))
while True:
    if i<=j:
        sum+=i
        i=i+1
    elif j<i:
        break;
print("1에서 %d 까지 합은 %d요" %(j,sum)) #두개를 넣으려면 묶어야함'''



'''def mydef01(i):
    i=int(input("입력해주세요 : "))
    if type(i) ==str:
        print("str입니다")
    elif type(i)==int:
        print("int입니다")

mydef01(123)'''

import module01 #만들어놓은 클래스 가져오는거 
import sys
import math #내장모듈 sys,math를 가져온다

module01.mydef01()
module01.mydef02(10,20)
print("hello python")