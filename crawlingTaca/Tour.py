#상품 정보를 담는 클래스
class TourInfo:
    #멤버변수
    title= ''
    price= ''
    area= ''
    link= ''
    img=''
    contents= ''
    
    #생성자
    #contents: 아까 TourInfo 만들때 이거 넣은적 없으니 디폴트값 써줌
    def __init__(self,title, price, area, link, img, contents= None):
        self.title= title
        self.price= price
        self.area= area
        self.link= link
        self.img= img
        self.contents= contents
