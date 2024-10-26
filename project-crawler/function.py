# Import libray
from bs4 import BeautifulSoup
import requests
import data_meeting

#-----function------

    #open link and get source code html
def open_link(str_url):
        #Dung module requests de tao 1 request toi trang web va lay source code html
        respone = requests.get(str_url)
        #Su dung BeautifulSoup de chuyen source code html sang kieu du lieu cua BeautifulSoup
        soup = BeautifulSoup(respone.content,'html.parser')
        return soup

#Crawl data from source code html
def get_infor(contents):
    #Tao mang de chua du lieu cac thong tin cua meeting theo object cua class InfoMeeting
    data_crawl = []

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
            data.conference = new_confer.text.strip() if new_confer else None #neu co thi lay ra chuoi con cua the <a> con khong thi gan bang None
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
            get_url = item.find('a')
            data.url = get_url['href']
            #Add du lieu cua cac the tim duoc theo object InfoMeeting luu vao mang data_crawl
            data_crawl.append(data)
    return data_crawl

#Ghi du lieu vao file txt
def writeData(exp_data):
    #Tao file txt de ghi du lieu
    file_name = 'Export Data.txt'
    #Mo file de ghi du lieu
    write_file = open(file_name,'w')
    #Truyen mang du lieu vao exp_data va ghi tat ca cac thong tin cua meeting vao file txt
    for item in exp_data:
        write_file.write(f"Conference: {item.conference},")
        write_file.write(f"Location: {item.location},")
        write_file.write(f"Deadline: {item.deadline},")
        write_file.write(f"Date: {item.date},")
        write_file.write(f"Notification: {item.notification},")
        write_file.write(f"Rules: {item.rules},")
        write_file.write(f"URL: {item.url} \n")
    write_file.close()
    
    
        
         
   
   
#Hien thi du lieu cua meeting len console (dung de test code)
def show(data):
     for item in data:
        print(f"Conference: {item.conference}")
        print(f"Location: {item.location}")
        print(f"Deadline: {item.deadline}")
        print(f"Date: {item.date}")
        print(f"Notification: {item.notification}")
        print(f"Rules: {item.rules}")
        print("-" * 30)




        
