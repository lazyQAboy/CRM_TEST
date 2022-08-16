# ========== pip ==============
# pip install selenium
# pip install webdriver-manager
# =============================


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

url = 'https://miofesta.com'
driver.get(url)

# ================   class   ====================
CRM_list_line= 'listTr'                                                                  # CRM 타석 리스트
ID_choice = 'select2-selection.select2-selection--single'                                # 배정 시 회원 선택 칸
ID_choice_box = 'select2-search__field'                                                  # 회원 선택 리스트 입력칸   
ID_choice_list = 'select2-results__option.select2-results__option--highlighted'          # 회원 선택 리스트 회원 선택
CRM_list_radio = 'radio'                                                                 # CRM 타석 리스트 라디오 버튼
CRM_list_ok_btn = 'btn.btn-sm.btn-success.pull-left.saveBtn'                             # CRM 타석 리스트 배정/수정 버튼
CRM_list_okpopup_ok_btn = 'swal-button.swal-button--confirm'                             # 배정 시, 확인 팝업 OK 버튼
Onoff_btn = 'onoffswitch-switch'                                                         # 게임 사용여부 버튼
Onoff_btn_popup_ok_btn = 'swal-button.swal-button--confirm'                              # 게임 사용여부 버튼 팝업 OK 버튼
Book_btn = 'btn.btn-xs.btn-primary.bookBtn'
# ===============================================/

# 사이 시간
ST = 1.5

#miofesta login ID
M_login_ID = 'qedtest'
M_login_PW = 'qed1234$#@!'


#로그인
driver.find_element_by_id("username").send_keys(M_login_ID)
driver.find_element_by_id("password").send_keys(M_login_PW)
driver.find_element_by_class_name('btn.btn-primary').click()


#우측 상단 매장 선택 - 실패!
# driver.find_element_by_class_name('fa.fa-angle-down').click()
# driver.find_element_by_id('storeDrop').send_keys('QED 테스트매장_2')
# driver.find_element_by_class_name('active').send_keys(Keys.ENTER)

time.sleep(3)


#================================================================각 모드 입장 테스트================================================================
for i in range(1,8):

    #회원 선택
    driver.find_elements_by_class_name(CRM_list_line)[0].click()
    driver.find_elements_by_class_name(ID_choice)[0].click()
    driver.find_elements_by_class_name(ID_choice_box)[0].send_keys('64555004')
    driver.find_elements_by_class_name(ID_choice_list)[0].click()
    time.sleep(3)

    # 각 모드 입장
    driver.find_elements_by_class_name(CRM_list_radio)[i].click()
    time.sleep(ST)
    driver.find_element_by_class_name(CRM_list_ok_btn).click()
    time.sleep(ST)
    driver.find_element_by_class_name(CRM_list_okpopup_ok_btn).click()
    if i == 2:
        time.sleep(30)
    else:
        time.sleep(5)

    # 게임 사용여부 OFF
    driver.find_element_by_class_name(Onoff_btn).click()
    time.sleep(ST)
    driver.find_element_by_class_name(Onoff_btn_popup_ok_btn).click()
    time.sleep(5)

#===================================================================================================================================================

#================================================================회원 모드 이동 테스트================================================================