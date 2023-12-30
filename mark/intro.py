from bs4 import BeautifulSoup
import requests
import time
import datetime


# wish() function wishes you according to the time at your place
def wish() :
    hour=int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12 :
        wish = "Good Morning! "
    elif hour>=12 and hour<18 :
        wish = "Good Afternoon! "
    else :
        wish = "Good Evening! "
    
    return wish



# curr_time() function tells the current time
def curr_time():
    strTime = time.strftime("%I:%M %p")
    curr_t = f" {strTime} "
    return curr_t



# curr_date() function tells the current date
def curr_date():
    dat = datetime.datetime.now().date()
    day=time.strftime("%A")
    curr_d = f" {day}, {dat} "
    return curr_d

# curr_loc() function tells the current location of your device
def curr_loc():
    response = requests.get('https://ipinfo.io/')
    if response.status_code == 200:
        data = response.json()
        city = data['city']
        return city
    else:
        print("Error in the HTTP request")


# curr_temprature() function tells the current temprature in your city
def curr_temprature():   
    #city="temprature of delhi"
    city=f"temprature of {curr_loc()}"
    url=f"https://www.google.com/search?q={city}"

    r=requests.get(url)

    d=BeautifulSoup(r.text,"html.parser")
    temp = d.find("div",class_="BNeawe").text
    
    return f"Temperature is {temp} ° Celcius"
