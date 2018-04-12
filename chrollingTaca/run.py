# 인터파크 투어사이트- 여행지 입력후 검색> 잠시후> 결과
# 로그인시 PC웹사이트에서 처리가 어려울 경우> 모바일 로그인 진입
# 모듈
from selenium import webdriver as wd
# ㄴ여기까지 실행해서 확인
from selenium.webdriver.common.by import By #find랑 혼합해서 찾으려고
from selenium.webdriver.support.ui import WebDriverWait # 명시적대기
from selenium.webdriver.support import expected_conditions as EC

import time

from Tour import TourInfo #Tour 파일의 TourInfo클래스에 담을것

# 사전에 필요한 정보를 로드> DB,shell,batch 에서 인자 받아 세팅
# 마지막에 / 넣냐마냐 일관성있게 ㄱㄱ
main_url= "http://tour.interpark.com/"
# send_keys 에 넣을 값
keyword= '로마'
## 구조정보
# 상품정보를 담는 리스트. TourInfo 리스트
tour_list= []



# 드라이버 로드
driver= wd.Chrome(executable_path= 'lib/chromedriver.exe')
# 옵션: proxy, user-Agent, 이미지배제_훨씬 빨라짐
# 주의: 크롤링을 오래 돌리면 임시파일이 쌓임> temp를 비워야

# 사이트 접속. get
driver.get(main_url)

# 잠시 대기1

# 검색창 찾기> 검색어 입력
# id: SearchGNBText
# send_keys: 검색어 넣기
driver.find_element_by_id('SearchGNBText').send_keys(keyword)
# path= '//*[@id="SearchGNBText"]'

# 수정할 경우> 뒤에 내용이 붙어버림
# 먼저 .clear() -> send_keys('내용')

# 검색버튼 클릭
# id가 없더라. class="search-btn". 유일하더라 ㅎㅎ
# 누르는 것만으론 안 되면 script 구동. searchBarModule.ClickForSearch(); 
# .search-btn 만 써도 괜춚
driver.find_element_by_css_selector('button.search-btn').click() 

# 결과중에 패키지 여행만. 여행더보기
# url 직링? 큰 회사일 수록 자주 바꾸니 ㄴㄴ
# 하나씩 찾아서 따라 들어가는 게 좋음

# selenium python> 5.wait
# 잠시 대기- 페이지 로드되고 즉각 데이터 획득하는 행위는 자제
# 서버 속도가 천차만별이라, 그 요소가 정말 떴는지 확신할 수 X
# 묵시적, 명시적_sleep(2 sec)
# 명시적 대기: 특정 요소가 로케이트(발견될때까지) 대기
# 암묵적 대기: DOM이 다 로드 될때까지 대기. 먼저 로드 되면 바로 진행
    #요소를 찾을 특정 시간 동안 DOM풀링을 지시. EX_10초이내. 발견되면 진행
# 절대적 대기: time.sleep(10) <- 클라우드 페어(디도스 방어 솔루션)
# 특히 작은 회사는 크롤링에 대해서도 민감. 성능이슈라서

# 명시적
try:
    element= WebDriverWait(driver, 10).until(
        # 지정 1개 요소가 올라오면 wait 종료
        EC.presence_of_element_located((By.CLASS_NAME, 'oTravelBox'))
    )
except Exception as e:
    print('error',e)

# 암묵적. 그냥 빠르게 만들고 싶다면
driver.implicitly_wait(10)

# 더보기 클릭> 게시판 진입
driver.find_element_by_css_selector('.oTravelBox>.boxList>.moreBtnWrap>.moreBtn').click()

## 인터파크엔 해당 안 되지만,
# 게시판에서 많은 데이터를 가져올 때
# 로그인 필요한 사이트(세션)라면, 주기적으로 로그인/로그아웃 반복해야
# 특정 게시물이 사라질 경우> 팝업 발생? 없는?> 팝업 처리 검토

# 게시판 끝 지점? 수집이 안 되는 시점! ~ 임계점 찾기
# 게시판 스캔> 메타 정보 획득> loop> 일괄적으로 방문/접근 처리
# searchModule.SetCategoryList(1, '')
# 끝 페이지 14. 초과했을 때 뭔일 일어났나 보려고, 15까지 보자는 것
pageEnd= 1
for page in range(1,pageEnd+1): 
    try:
        # JS 구동하기
        driver.execute_script("searchModule.SetCategoryList(%s, '')"%page)
        #페이지 파바바박 방지. 강제로 쉬기
        time.sleep(2) #sec
        print('잘되고 있니',page)
        ##### 내용 가져오기
        # 변수 파악. 여러 사이트 비교해서 table 칼럼 '잘 정의'하기
        # 상품명, 코멘트, 기간1, 기간2, 가격, 평점, 썸네일, 링크(상품상세정보)
        boxItems= driver.find_elements_by_css_selector('.oTravelBox>.boxList>li')
        # 상품 하나하나 접근
        for li in boxItems:
            # 이미지 링크값을 쓸건지? 아니면 다운로드해서 내 서버에 업로드 할건지?
            # 의존적 vs 저작권 뚫뚫
            print('썸네임',li.find_element_by_css_selector('img').get_attribute('src'))   
            print('링크',li.find_element_by_css_selector('a').get_attribute('onclick'))   
            print('상품명',li.find_element_by_css_selector('h5.proTit').text)
            print('코멘트',li.find_element_by_css_selector('p.proSub').text)
            # print('기간', (li.find_element_by_css_selector('p.proInfo').text).split(' : ')[1])
            print('가격',li.find_element_by_css_selector('.proPrice').text)
            # error! not element but elements
            # for info in li.find_element_by_css_selector('.info-row .proInfo'):
            for info in li.find_elements_by_css_selector('.info-row .proInfo'):
                print(info.text)
            print('= '*20)

            #데이터 모음
            # 깔끔히 하려면 변수에 받아서~
            obj= TourInfo(
                li.find_element_by_css_selector('h5.proTit').text
                , li.find_element_by_css_selector('.proPrice').text
                , li.find_elements_by_css_selector('.info-row .proInfo')[1].text
                , li.find_element_by_css_selector('a').get_attribute('onclick')
                , li.find_element_by_css_selector('img').get_attribute('src')
            )
            tour_list.append(obj)
    except Exception as e1:
        print('페이징 error',e1)

# strong.proPrice 대신 .proPrice 를 써야!
print(tour_list, len(tour_list)) #왜 11? 강사님- 12



##
# 수집한 정보 개수만큼 loop> 페이지 방문> 콘텐츠 획득_상품상세정보> DB
