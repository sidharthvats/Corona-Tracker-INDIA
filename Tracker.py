#importing Modules

import requests
import bs4
import plyer
import tkinter as tk
import time
import datetime
import threading


def Get_html_data(url):
    data=requests.get(url)
    return data

def Get_Corona_updates_India():
    url="https://www.mohfw.gov.in/"
    html_data=Get_html_data(url)
    bs=bs4.BeautifulSoup(html_data.text,'html.parser')
    info_div=bs.find("div",class_="site-stats-count").find_all("li",class_=["bg-blue","bg-green","bg-red","bg-orange"])

    all_details=""

    for block in info_div:
        text=block.find("span").get_text()
        count=block.find("strong").get_text()
        all_details=all_details + text + ":"+ count +"\n"

    return all_details

#function to refresh data
def Refresh():
    new_data=Get_Corona_updates_India()
    print("Refreshing")
    mainlabel['text']=new_data


#Notification function
def notify():
    while True:
        plyer.notification.notify(
            title="Covid-19 Cases in India",
            message=Get_Corona_updates_India(),
            timeout=10
        )
        time.sleep(20)

#Creating GUI
root=tk.Tk()
root.geometry("500x500")
root.title("Corona Tracker of India")
root.configure(background='#032A3C')
f=("franklin gothic demi cond",20,"bold")
f2=("times new roman",15,"bold")

photo=tk.PhotoImage(file="image.png")
resize=photo.subsample(4,4)
photoLabel=tk.Label(root,image=resize,bg='#032A3C')
photoLabel.pack()

mainlabel=tk.Label(root,text=Get_Corona_updates_India(),bg="#032A3C",font=f,fg='white')
mainlabel.pack()

button=tk.Button(root,text="REFRESH",font=f2,foreground="black",relief='solid',command=Refresh,padx=10,pady=10,bg="#616364")
button.pack()


#create a new thread

th1=threading.Thread(target=notify)
th1.setDaemon(True)
th1.start()

root.mainloop()


def main():
    Get_Corona_updates_India()


if __name__ == '__main__':main()