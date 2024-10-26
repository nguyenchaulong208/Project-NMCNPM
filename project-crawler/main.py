# Import libray
import function
import selenium_funtion_copy
import time

#------main------
#Cac link trang web can crawl du lieu
str_url = 'https://www.lix.polytechnique.fr/~hermann/conf.php#'
str_Url = 'https://conf.researchr.org/'
#Tao mang de chua du lieu cac thong tin cua meeting
get_contents = []

#Vong lap vo han de lap lap crawl du lieu
while True:
    print("Crawling data, Plesea wait a minute...!!!")
    # function.show(get_contents)
    #Thuc hien cac function trong file function.py va selenium_funtion.py de crawl va ghi du lieu vao file
    source = function.open_link(str_url)
    source_selenium = selenium_funtion_copy.get_url(str_Url)
    get_contents = function.get_infor(source)
    get_content_selenium = selenium_funtion_copy.get_element(source_selenium)
    source_selenium.quit()
    get_contents.extend(get_content_selenium)
    function.writeData(get_contents)
    get_contents.clear()
    print ('Successfully crawled data and exported to file!')
    print('File location:/PROJECT-NMCNPM/Export Data.txt')
    #Thoi gian cho de lap lai crawl du lieu sau 30s
    time.sleep(30)


