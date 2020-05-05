#importing Modules

import requests
import bs4
import plyer
import tkinter as tk
import time
import datetime


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
        all_details=all_details + text + ": "+ count +"\n"

    return all_details

#function to refresh data
def Refresh():
    new_data=Get_Corona_updates_India()
    print("Refreshing")
    mainlabel['text']=new_data
#Creating GUI

root=tk.Tk()
root.geometry("500x500")
root.title("Corona Tracker of India")
root.configure(background='white')
f=("poppins",25,"bold")
f2=("times new roman",15,"bold")

photo=tk.PhotoImage(file=r"C:\Users\sidha\PycharmProjects\Track\globe.png")
resize=photo.subsample(4,4)
photoLabel=tk.Label(root,image=resize,bg='white')
photoLabel.pack()

mainlabel=tk.Label(root,text=Get_Corona_updates_India(),font=f,bg='white')
mainlabel.pack()

button=tk.Button(root,text="REFRESH",font=f2,foreground="green",relief='solid',command=Refresh)
button.pack()

root.mainloop()


def main():
    Get_Corona_updates_India()


if __name__ == '__main__':main()