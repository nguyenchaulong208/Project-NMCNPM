from bs4 import BeautifulSoup
import requests
import data_meeting


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
    data_crawl = []
    find_tag = contents.find_all('tr')
    for item in find_tag:
        for new_item in item.find_all('td'):
            data = data_meeting.InfoMeeting()
            confer = new_item.find('td', class_="confname")
            data.conference = confer
            print(data.conference)
            loca = new_item.find('td', class_='location')
            data.location = loca
            deadl = new_item.find('td', class_='now-deadline')
            data.deadline = deadl
            dat =  new_item.find('td', class_='date')
            data.date = dat
            notify =  new_item.find('td', class_='notification')
            data.notification = notify
            submission = new_item.find('td', class_='subformat')
            data.rules = submission
            data_crawl.append(data)
    return data_crawl

     
            
def show(data):
     for item in data:
        print(f"Conference: {item.conference}")
        print(f"Location: {item.location}")
        print(f"Deadline: {item.deadline}")
        print(f"Date: {item.date}")
        print(f"Notification: {item.notification}")
        print(f"Rules: {item.rules}")
        print("-" * 30)
     