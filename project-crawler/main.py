# Import libray
import function
import selenium_funtion
import time
#------main------

str_url = 'https://www.lix.polytechnique.fr/~hermann/conf.php#'
str_Url = 'https://conf.researchr.org/'

get_contents = []


while True:
    print("Crawling data, Plesea wait a minute...!!!")
    # function.show(get_contents)
    source = function.open_link(str_url)
    source_selenium = selenium_funtion.get_url(str_Url)
    get_contents = function.get_infor(source)
    get_content_selenium = selenium_funtion.get_element(source_selenium)
    source_selenium.quit()
    get_contents.extend(get_content_selenium)
    function.writeData(get_contents)
    get_contents.clear()
    print ('Successfully crawled data and exported to file!')
    print('File location:/PROJECT-NMCNPM/Export Data.txt')
    time.sleep(30)


