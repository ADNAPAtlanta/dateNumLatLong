from firebase import firebase
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from geopy.geocoders import Nominatim
from geopy.geocoders import GoogleV3
import datetime
import time
from email.mime.text import MIMEText
import os


try:
    # for Python2
    from Tkinter import *
    from tkinter import filedialog
except ImportError:
    # for Python3
    from tkinter import *
    from tkinter import filedialog



ksuBuildings = {"Baily Athletic Facility": "220 Kennesaw State Univ Rd NW Kennesaw, GA 30144",
                "Bailey Performance Hall":"488 Prillaman Way NW Kennesaw, GA 30144",
                 "Baseball Field": "208 Kennesaw State Univ Rd NW Kennesaw, GA 30144",
                "Burruss":"560 Parliament Garden Way NW Kennesaw, GA 30144",
                 "Campus Green": "565 Cobb Ave Kennesaw, GA 30144",
                "Campus Services":"1075 Canton Pl NW Kennesaw, GA 30144",
                "Chastain Pointe":"1200 Chastain Rd NW Kennesaw, GA 30144",
                "Clendenin":"275 Kennesaw State Univ Rd NW Kennesaw, GA 30144",
                "Convocation Center":"590 Cobb Ave NW Kennesaw, GA 30144",
                "Education Classroom Facility":"580 Parliament Garden Way NW Kennesaw, GA 30144",
                "English Building":"440 Bartow Ave NW Kennesaw, GA 30144",
                "Gazebo":"410 Bartow Ave NW Kennesaw, GA 30144",
                "House 48 - ASap":"3499 Campus Loop Rd NW Kennesaw, GA 30144",
                "House 49 - Cox Family Enterprise":"3495 Campus Loop Rd NW Kennesaw, GA 30144",
                "House 51 - TBD":"3217 Campus Loop Rd NW Kennesaw, GA 30144",
                "House 52 - Clinic":"3215 Campus Loop Rd NW Kennesaw, GA 30144",
                "House 54 - CETL":"3211 Campus Loop Rd NW Kennesaw, GA 30144",
                "House 55 - MEBUS":"3209 Campus Loop Rd NW Kennesaw, GA 30144",
                "House 56 - Alumni":"3207 Campus Loop Rd NW Kennesaw, GA 30144",
                "House 57 - Center for Elections":"3205 Campus Loop Rd NW Kennesaw, GA 30144",
                "House 58 - Distance Learning":"3203 Campus Loop Rd NW Kennesaw, GA 30144",
                "House 59 - ATOMS":"3201 Campus Loop Rd NW Kennesaw, GA 30144",
                "J.M Wilson":"471 Bartow Ave NW Kennesaw, GA 30144",
                "Jolley Lodge":"1055 Canton Pl NW Kennesaw, GA 30144",
                "Kennesaw Hall":"585 Cobb Ave NW Kennesaw, GA 30144",
                "KSU Center":"3333 Busbee Dr NW Kennesaw, GA 30144",
                "Library":"385 Cobb Ave NW Kennesaw, GA 30144",
                "Math and Statistics":"365 Cobb Ave NW Kennesaw, GA 30144",
                "Music":"491 Bartow Ave NW Kennesaw, GA 30144",
                "Office Annex":"371 Paulding Ave NW Kennesaw, GA 30144",
                "Owl's Nest":"3220 Busbee Dr NW Kennesaw, GA 30144",
                "Pilcher":"375 Cobb Ave NW Kennesaw, GA 30144",
                "Prillaman Health Sciences":"520 Parliament Garden Way NW Kennesaw, GA 30144",
                "Public Safety":"351 Paulding Ave NW Kennesaw, GA 30144",
                "Rec Fields" : "270 Kennesaw State Univ Rd NW Kennesaw, GA 30144",
                "Science":"370 Paulding Ave NW Kennesaw, GA 30144",
                "Science Laboratory":"105 Marietta Dr NW Kennesaw, GA 30144",
                "Student Recreation & Activities Center":"290 Kennesaw State Univ Rd NW Kennesaw, GA 30144",
                "Soccer Field": "1000 Chastain Rd NW Kennesaw, GA 30144",
                "Social Sciences":"402 Bartow Ave NW Kennesaw, GA 30144",
                "Softball Field":"250 Kennesaw State Univ Rd NW Kennesaw, GA 30144",
                "Sports and Recreation Park":"390 Big Shanty Rd NW Kennesaw, GA 30144",
                "Student Athlete Success":"1150 Big Shanty Rd NW Kennesaw, GA 30144",
                "Student Center/Bookstore":"395 Cobb Ave NW Kennesaw, GA 30144",
                "Tech Annex":"361 Paulding Ave NW Kennesaw, GA 30144",
                "Technology Services":"1075 Canton Pl NW Kennesaw, GA 30144",
                "The Commons":"540 Parliament Garden Way NW Kennesaw, GA 30144",
                "Town Point":"3391 Town Point Dr NW Kennesaw, GA 30144",
                "University College":"430 Bartow Ave NW Kennesaw, GA 30144",
                "Visual Arts":"411 Bartow Ave NW Kennesaw, GA 30144",
                "Willingham Hall":"420 Bartow Ave NW Kennesaw, GA 30144",
                "Wilson Annex":"462 Prillaman Way NW Kennesaw, GA 30144",
                "Zuckerman Museum":"492 Prillaman Way NW Kennesaw, GA 30144",
                #Housing
                "Austin Residence Complex":"125 Marietta Dr NW Kennesaw, GA 30144",
                "University Village":"1074 Canton Pl NW Kennesaw, GA 30144",
                "KSU Place Apartments":"1175 Idlewood Ave NW Kennesaw, GA 30144",
                "Other":"",
                "Select building.":""}

days = ["01", "02", "03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24",
        "25","26","27","28","29","30","31"]

months = {"Jan": "01", "Feb":"02", "Mar":"03", "Apr":"04",
	   			    "May":"05", "Jun":"06", "July":"07", "Aug":"08",
				    "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}

years = ["2016","2017","2018"]

hours = ["00","01","02","3","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"]

minutes = ["00","01", "02", "03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24",
        "25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57",
           "58","59","60"]
pmAM = ["PM", "AM"]

class eventForm:
    def __init__(self,master):
        self.master = master
        master.title("KSU Event System (organization ver.)")
        master.minsize(width=300, height=300)
        self.type = StringVar()
        self.type.set("Vacation")
        self.lat = StringVar()
        self.longitude = StringVar()
        self.address = StringVar()
        self.day = StringVar()
        self.day.set("01")
        self.month = StringVar()
        self.month.set("Jan")
        self.year = StringVar()
        self.year.set("2016")

        self.pmAM = StringVar()
        self.pmAM.set("PM")
        self.hour = StringVar()
        self.hour.set("00")
        self.minute = StringVar()
        self.minute.set("00")
        self.endHour = StringVar()
        self.endHour.set("00")
        self.endMinute = StringVar()
        self.endMinute.set("00")

        
        self.submitButton = Button(master, text="Submit", command=self.submit)
        self.submitButton.grid(column=1)

        self.dayOption = OptionMenu(master, self.day,*days)
        self.dayOption.grid(column=1)
        self.monthOption = OptionMenu(master,self.month,*months)
        self.monthOption.grid(column=1)
        self.yearOption = OptionMenu(master,self.year,*years)
        self.yearOption.grid(column=1)

        self.pmAMOption = OptionMenu(master, self.pmAM, *pmAM)
        self.pmAMOption.grid(column=1)

        self.hourLabel = Label(master, text=" StartingHour", underline=0)
        self.hourLabel.grid(column=1)
        self.hourOption = OptionMenu(master,self.hour,*hours)
        self.hourOption.grid(column=1)
        self.minuteLabel = Label(master, text="Starting Minute", underline=0)
        self.minuteLabel.grid(column=1)
        
        self.minuteOption = OptionMenu(master,self.minute,*minutes)
        self.minuteOption.grid(column=1)
        
        self.endHourLabel = Label(master, text="Enter ending hour", underline=0)
        self.endHourLabel.grid(column=1)
        self.endHourOption = OptionMenu(master, self.endHour,*hours)
        self.endHourOption.grid(column=1)
        self.endMinuteLabel = Label(master, text="Enter ending minute", underline=0)
        self.endMinuteLabel.grid(column=1)
        
        self.endMinuteOption = OptionMenu(master, self.endMinute, *minutes)
        self.endMinuteOption.grid(column=1)
        self.addressEntryLabel = Label(master, text="Enter address.", underline=0)
        self.addressEntryLabel.grid(column=1)
        self.addressEntry = Entry(master, textvariable=self.address,bd=3)
        self.addressEntry.grid(column=1)


    def submit(self):
        geolocator = GoogleV3(api_key="AIzaSyB9NYRXQZN3gIcJue5SJa2jem7UdOzmOvI")
        address = self.address.get()
        location = geolocator.geocode(address, timeout=10)
        lat = location.latitude
        longitude = location.longitude
        print(location)
        print("lat: " + str(lat))
        print("longitude: " + str(longitude))
        month =  months[self.month.get()]
        hour = self.hour.get()
        minute = self.minute.get()
        date =  self.day.get() + "/" + month + "/" + self.year.get() + " " + hour + ":" + minute
        dateNum =  time.mktime(datetime.datetime.strptime(date, "%d/%m/%Y %H:%M").timetuple())
        print(dateNum)
        

if __name__ == "__main__":
    root = Tk()
    root.resizable(width=False, height=False)
    GUI = eventForm(root)
    root.mainloop()    

        
