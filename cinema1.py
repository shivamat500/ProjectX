import csv
import random


########################### addbooking function ####################
def addbooking():
#creating a 2d array that is containing a data before writing it to csv file.
 bookings = []
#creating a random no for the entry between 0 to 100
 bookingref=random.randint(1,10000)
 
    
 print("your booking number is",bookingref)
#ask them to enter details
 name    = input("please give your name:")
 surname = input("please give your surname:")
 film    = input("please tell film name:").lower()
 day     = input("please tell the day:")
#adding those details to the booking 2d array variable
 bookings.append(bookingref)
 bookings.append(name)
 bookings.append(surname)
 bookings.append(film)
 bookings.append(day)
 
#now putting the data in csv file
 with open('cinema.csv','a',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(bookings)
    
 print("Booking Done Great Choice:)")  
###############################close#########################    

############################### search function ############# 
def searchfilm():
 data = []
 with open ('cinema.csv','r') as csvfile:
         reader=csv.reader(csvfile)
         for row in reader:
          data.append(row)
 print(data)
 #variable for taking the input for searchinfg
# lookup=input("please enter the film name to be searched!")
 
 
 #loop all the data of column 4 to col4 variable
 col4 = [x[3] for x in data]
 #print the data to test
 print(col4)
 lookup=input("please enter the film name to be searched!").lower()
 
 
 if lookup in col4:
#looking into col 4 and searching for given instance in col4
# assingning [k] for that instance search 
#data[k] will print all the information of that row
 
 
     for k in range(0, len(col4)):
         if col4[k] == lookup:
          print(data[k])    
 
 else:
     print("the film in not in list:")    
##############################close!##############################
     
############################### search function by no ############# 
def searchfilmno():
 data = []
 with open ('cinema.csv','r') as csvfile:
         reader=csv.reader(csvfile)
         for row in reader:
          data.append(row)
 print(data)
 #variable for taking the input for searchinfg
# lookup=input("please enter the film name to be searched!")
 
 
 #loop all the data of column 4 to col4 variable
 col1 = [x[0] for x in data]
 #print the data to test
 print(col1)
 lookup=input("please enter the film no to be searched!").lower()
 
 
 if lookup in col1:
#looking into col 4 and searching for given instance in col4
# assingning [k] for that instance search 
#data[k] will print all the information of that row
 
 
     for k in range(0, len(col1)):
         if col1[k] == lookup:
          print(data[k])    
 
 else:
     print("the film in not in list:")    
##############################close!##############################
    
    
#######################   menu system   ##########################
    
print("welcome to the ticket booking system:")  
print ("please select an option to continue:")  
print("1:addbooking:")
print("2:to search film by name:")
print("3:to search film by no:")
choice=input("please choose the option:")
if choice == "1":
    addbooking()
elif choice == "2":
    searchfilm()
elif choice == "3":
    searchfilmno()    
else:
    print("sorry!!!!! wrong selection:)")
    
#This is end of project Good Bye............    
    

 
 