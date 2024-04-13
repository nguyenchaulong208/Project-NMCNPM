# Import libray
import function
#------main------


str_url = 'https://www.lix.polytechnique.fr/~hermann/conf.php#'
source =function.open_link(str_url)
get_contents = []
# get_content = function.get_context(source)
# get_contents = function.get_information(get_content)
# for item in get_contents:
#     print(item)

get_contents = function.get_infor(source)


function.show(get_contents)
function.writeData(get_contents)