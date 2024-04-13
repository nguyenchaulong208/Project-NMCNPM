# Import libray
from bs4 import BeautifulSoup
import requests
import data_meeting

#-----function------



    #open link and get source code html
def open_link(str_url):
        respone = requests.get(str_url)
        soup = BeautifulSoup(respone.content,'html.parser')
        return soup

#Crawl data from source code html
def get_infor(contents):
    data_crawl = []
# ver1
    # # find all table in soucre code html

    # find_tag = contents.find_all('table', class_='conference')
    # for item in find_tag:
    # # find all <tr> tag name in <table> with class conference
    #    for row in item.find_all('tr'):
    #         # print(row)
    #         data = data_meeting.InfoMeeting()
    #         confer = row.find('td', class_="confname")
    #         data.conference = confer.text.strip() if confer else None
    #         # print(data.conference)
    #         loca = row.find('td', class_='location')
    #         data.location = loca.text.strip() if loca else None
    #         # print(data.location)
    #         deadl = row.find('td', class_='now-deadline') or row.find('td', class_='deadline')
    #         data.deadline = deadl.text.strip() if deadl else None
    #         dat =  row.find('td', class_='date')
    #         data.date = dat
    #         notify =  row.find('td', class_='notification')
    #         data.notification = notify.text.strip() if notify else None
    #         submission = row.find('td', class_='subformat') or row.find('td', class_='remark')
    #         data.rules = submission.text.strip() if submission else None
    # # add data to data_meeting list
    #         data_crawl.append(data)
# -------------------
# ver2
# find the first 'tbody' tag
    find_tag = contents.find('tbody')
    # find all <tr> tag in <tbody>
    find_all = find_tag.find_all('tr')
    # find all <td> tag in <tr> tag
    for item in find_all:

            data = data_meeting.InfoMeeting()
            confer = item.find('td', class_="confname")
            # get content in <a> tag
            new_confer =confer.find('a')
            data.conference = new_confer.text.strip() if new_confer else None
            loca = item.find('td', class_='location')
            data.location = loca.text.strip() if loca else None
            deadl = item.find('td', class_='now-deadline') or item.find('td', class_='deadline')
            data.deadline = deadl.text.strip() if deadl else None
            dat =  item.find('td', class_='date')
            data.date = dat.text.strip() if deadl else None
            notify =  item.find('td', class_='notification')
            data.notification = notify.text.strip() if notify else None
            submission = item.find('td', class_='subformat') or item.find('td', class_='remark')
            data.rules = submission.text.strip() if submission else None

            data_crawl.append(data)
    return data_crawl


def writeData(exp_data):
      
    file_name = 'Export Data.txt'
    write_file = open(file_name,'w')
    for item in exp_data:
        write_file.write(f"Conference: {item.conference} ||")
        write_file.write(f"Location: {item.location} ||")
        write_file.write(f"Deadline: {item.deadline} ||")
        write_file.write(f"Date: {item.date} ||")
        write_file.write(f"Notification: {item.notification} ||")
        write_file.write(f"Rules: {item.rules} ||\n---\n")
    write_file.close()
    print ('Export data successfully')
    print('File location:/PROJECT-NMCNPM/Export Data.txt')
    
        
         
    # Xuất DataFrame vào file Excel
   

def show(data):
     for item in data:
        print(f"Conference: {item.conference}")
        print(f"Location: {item.location}")
        print(f"Deadline: {item.deadline}")
        print(f"Date: {item.date}")
        print(f"Notification: {item.notification}")
        print(f"Rules: {item.rules}")
        print("-" * 30)
