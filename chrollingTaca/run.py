# 인터파크 투어사이트- 여행지 입력후 검색> 잠시후> 결과
# 로그인시 PC웹사이트에서 처리가 어려울 경우> 모바일 로그인 진입
# 모듈
from selenium import webdriver as wd
# ㄴ여기까지 실행해서 확인

# 사전에 필요한 정보를 로드> DB,shell,batch 에서 인자 받아 세팅
# 마지막에 / 넣냐마냐 일관성있게 ㄱㄱ
main_url= "http://tour.interpark.com/"
# send_keys 에 넣을 값
keyword= '로마'

# 드라이버 로드
driver= wd.Chrome(executable_path= 'lib/chromedriver.exe')
# 옵션: proxy, user-Agent, 이미지배제_훨씬 빨라짐
# 주의: 크롤링을 오래 돌리면 임시파일이 쌓임> temp를 비워야

# 사이트 접속. get
driver.get(main_url)

# 잠시 대기- 페이지 로드되고 즉각 데이터 획득하는 행위는 자제
# 서버 속도가 천차만별이라, 그 요소가 정말 떴는지 확신할 수 X
# 묵시적, 명시적_sleep(2 sec)
# 원래는 예외처리 해야!

# 검색창 찾기> 검색어 입력
# id: SearchGNBText
# send_keys: 검색어 넣기
driver.find_element_by_id('SearchGNBText').send_keys(keyword)
# path= '//*[@id="SearchGNBText"]'

# 검색버튼 클릭

