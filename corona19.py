# 라이브러리를 불러온다.
import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen



class Main:
    ll = ['확진환자','격리해제','사망자','검사진행'] 
    print('\n\n코로나 상황을 기록을 하기 편하도록 간단하게 만든 프로그램')
    print('\n\n이 정보는 코로나바이러스감염증-19(COVID-19) 사이트를 통해서 받아옵니다.\n\n\n')
    print('''--------------------------사용법--------------------------''')
    print('''프로그램을 실행 시키고 숫자 1을 치고 엔터만 누르면 됩니다.
    기록은 이 프로그램과 같은 폴더에 메모장으로 남게 됩니다.\n\n''')
    while True:
        numm = []
        now = datetime.datetime.now()
        i = 0
        val = int(input('==  숫자 1을 입력하고 엔터를 누르면 코로나 정보가 나옵니다. : '))
        if val == 1:
            response = urlopen('http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=11&ncvContSeq=&contSeq=&board_id=&gubun=')
            soup = BeautifulSoup(response, 'html.parser')
            f1 = open('코로나19기록.txt','a',encoding='UTF8')
            print('\n')
            print('=====================================================================================')
            timenow = ("%s년 %s월 %s일 %s시 %s분\n" %(now.year, now.month, now.day, now.hour, now.minute))
            print(timenow)
            f1.write(timenow)
            for anchor in soup.select('td.w_bold'):
                numm.append(anchor.get_text())
            for i in range(0,4):
                print('| '+ll[i]+' : '+numm[i]+' |',end=" ")
                f1.write('| '+ll[i]+' : '+numm[i]+' |\n')
                i = i+1
            print('\n')
            print('=====================================================================================')
            print('\n')
            del numm[:] # list 안의 데이터만 삭제
            f1.close()
        else:
            print('잘 못 누르셨습니다.')