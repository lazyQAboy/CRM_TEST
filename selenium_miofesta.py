from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(options=options)

url = 'https://miofesta.com'
driver.get(url)

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
    driver.find_elements_by_class_name('listTr')[0].click()
    driver.find_elements_by_class_name('select2-selection.select2-selection--single')[0].click()
    driver.find_elements_by_class_name('select2-search__field')[0].send_keys('64555004')
    driver.find_elements_by_class_name('select2-results__option.select2-results__option--highlighted')[0].click()
    time.sleep(3)

    # 각 모드 입장
    driver.find_elements_by_class_name('radio')[i].click()
    time.sleep(ST)
    driver.find_element_by_class_name('btn.btn-sm.btn-success.pull-left.saveBtn').click()
    time.sleep(ST)
    driver.find_element_by_class_name('swal-button.swal-button--confirm').click()
    if i == 2:
        time.sleep(30)
    else:
        time.sleep(5)

    # 게임 사용여부 OFF
    driver.find_element_by_class_name('onoffswitch-switch').click()
    time.sleep(ST)
    driver.find_element_by_class_name('swal-button.swal-button--confirm').click()
    time.sleep(5)

#===================================================================================================================================================

#================================================================회원 모드 이동 테스트================================================================