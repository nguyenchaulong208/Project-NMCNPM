import function
import data_meeting

str_url = 'https://www.lix.polytechnique.fr/~hermann/conf.php#ahead'
source =function.open_link(str_url)
get_contents = []
# get_content = function.get_context(source)
# get_contents = function.get_information(get_content)
# for item in get_contents:
#     print(item)

get_contents = function.get_infor(source)


