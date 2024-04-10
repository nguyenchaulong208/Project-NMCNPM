import function
str_url = 'https://www.lix.polytechnique.fr/~hermann/conf.php'
source =function.open_link(str_url)
get_contents = []
get_content = function.get_context(source)
get_contents = function.get_information(get_content)
for item in get_contents:
    print(item)


