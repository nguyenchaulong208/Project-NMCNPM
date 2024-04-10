from bs4 import BeautifulSoup
import requests
import data_meeting

class SaveData:
 def __init__(self,save_data) -> None:
    self.model = save_data

    #open link
    def open_link(str_url):
        respone = requests.get(str_url)
        soup = BeautifulSoup(respone.content,'html.parser')
        return soup

    # #get conference
    # def get_context(source_content):
    #     get_contents =[]
    #     get_content = source_content.find_all('td',class_='confname')
    #     for item in get_content:
    #         get_contents.append(item)
    #     return get_contents

    # def get_information(contents):
    #     list_ref = []
    #     for item in contents:
    #         get_tag = item.find_all('a')
    #         for new_item in get_tag:
    #             list_ref.append(new_item.get_text())
    #     return list_ref

    def get_infor(contents):
        find_tag = contents.find_all('td', class_='confname')
        for item in find_tag:
            data = data_meeting.InfoMeeting()
            confer = item.find('a').get_text()
            data.conference = confer
            loca = item.find('td', class_='location').get_text()
            data.location = loca
            deadl = item.find('td', class_='now-deadline').get_text()
            data.deadline = deadl
            dat =  item.find('td', class_='date').get_text()
            data.date = dat
            notify =  item.find('td', class_='notification').get_text()
            data.notification = notify
            submission = item.find('td', class_='subformat').get_text()
            data.rules = submission
            
