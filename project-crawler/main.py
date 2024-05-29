# Import libray
import function
import time
#------main------

str_url = 'https://www.lix.polytechnique.fr/~hermann/conf.php#'
source = function.open_link(str_url)
get_contents = []
#     print(item)
    
while True:
    print("Crawling data, Plesea wait a minute...!!!")
    # function.show(get_contents)
    get_contents = function.get_infor(source)
    function.writeData(get_contents)
    time.sleep(30)

