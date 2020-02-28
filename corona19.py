# 라이브러리를 불러온다.
import datetime
from bs4 import BeautifulSoup
from urllib.request import urlopen




ll = ['확진환자','검사진행','격리해제','사망자'] 
numm = []
while True:
    now = datetime.datetime.now()
    response = urlopen('https://m.search.daum.net/search?nil_profile=btn&w=tot&DA=SBC&q=%EC%BD%94%EB%A1%9C%EB%82%98%EB%B0%94%EC%9D%B4%EB%9F%AC%EC%8A%A4%EA%B0%90%EC%97%BC%EC%A6%9D19&rtmaxcoll=0SP&DA=TCN')
    soup = BeautifulSoup(response, 'html.parser')
    i = 0
    val = int(input('==  1을 입력하고 엔터를 누르면 코로나 정보가 나옵니다. : '))
    if val == 1:
        print('이 정보는 다음을 통해서 받아옵니다.')
        print ("%s년 %s월 %s일 %s시 %s분" %(now.year, now.month, now.day, now.hour, now.minute))
        for anchor in soup.select("dd.num_info"):
            # print(ll[i] +' : ' + anchor.get_text())
            # i = i+1
            numm.append(anchor.get_text())
    else:
        break       


    for i in range(0,4):
        print('| '+ll[i]+' : '+numm[i]+' |',end=" ")
        i = i+1
    print('\n')