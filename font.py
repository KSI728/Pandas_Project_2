# 함수기능 : 시각화 시 폰트 설정
# 함수이름 : set_font
# 매개변수 : font_path
# 반환값 : 없음

# 한글 폰트 설정
# 모듈 불러오기
from matplotlib import font_manager,rc  # matplotlib의 환경설정 - 폰트

# 함수 선언
def set_font(font_path):
    
    # 설정할 한글 폰트 이름 추출
    font_name=font_manager.FontProperties(fname=font_path).get_name()
    
    # 한글 폰트 설정
    rc('font',family=font_name)
    
    # 확인 출력 
    print(f'{font_name} 폰트 설정')


# 폰트 파일 자체를 긁어와서 적용해도 됩니다.
# kor_font=r'C:/Users/knudc/AppData/Local/Microsoft/Windows/Fonts/강원교육모두 Bold.ttf'
# ex) font_path='./강원교육모두 Bold.ttf'