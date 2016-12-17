# On start
print("Welcome to prudent Health Care")

import time



def last():
    print("Options:\n1=Register\n2=Appointment\n3=Patient Treatment Plan\n4=Accountant \n5=Exit")
    while True:
        option = input("> ")
        if option == "1":
            Register()
        elif option == "2":
            Appointment()
        elif option == "3":
            PTP()
        elif option == "4":
            Accountant()
        elif option == "5":
            print("Shutting down.....")
            break
        else:
            print(option + " is not an option")

# form
def writes(patient_id, first_name, last_name, address, gender, contact, DOB):
    fw = open('data2.txt', "a")
    fw.write("%1s%20s%20s%20s%20s%20s%20s\n" % (patient_id, first_name, last_name, address, gender, contact, DOB))
    fw.close()



def cash(pid, name, bill):
    fw = open('data1.txt', "a")
    fw.write("%1s%20s%20s\n" % (pid, name, bill))
    fw.close()


# registration
def Register():
    patient_id = input("Enter patient_id: ")
    first_name = input("Enter your first_name: ")
    last_name = input("Enter your last name: ")
    address = input("Enter your address: ")
    gender = input("Enter your gender: ")
    contact = input("Enter your contact number: ")
    DOB=input("Enter your age: ")
    writes(patient_id, first_name, last_name, address, gender, contact,DOB )
    print("THANK YOU!!!")
    print("\nUser created!\n")
    last()

def appiontment(AID, PID, status):
    fw = open('data3.txt', "a")
    fw.write("%1s%20s%20s\n" % (AID, PID, status))
    fw.close()


def Appointment():
    AID=input("Enter Your Appointment ID: ")
    PID = input("Enter Your Patient ID: ")
    status = input("Complete or Appointment: ")
    appiontment(AID, PID, status)
    last()

def PTPw(TID, PID, Complain, Treatment):
    fw = open('data3.txt', "a")
    fw.write("%1s%20s%20s%20s\n" % (TID, PID, Complain, Treatment))
    fw.close()

def PTP():
    TID = input("Enter Your Treatment ID: ")
    PID = input("Enter Your Patient ID: ")
    Complain = input("Write your complain: ")
    Treatment = input("Given treatment: ")
    PTPw(TID, PID, Complain, Treatment)
    last()


    # This is for payment process
def Accountant():
    pid = input("enter ur pid")
    users = open("data2.txt", 'r')

    for each_line in users:
        (patient_id, first_name, last_name, address, gender, contact, DOB) = each_line.split()

    if (patient_id == pid):
        print(patient_id, first_name, last_name, address, gender, contact, DOB)
    else:
        print("Patient ID doesn't match")
        last()
    users.close()

    print("For cash Enter C")
    print("For credit Enter L")
    payment = input(">")
    if payment == "C":
        pid = input("Enter your patient_id: ")
        name = input("Enter your name: ")
        bill = input("Please enter the receipt for the bill: ")
        print("payment done by cash")

        print(bill)
        cash(pid, name, bill)
        print("Thank you")
        last()

    elif payment == "L":
        pid = input("Enter your patient_id: ")
        name = input("Enter your name: ")
        bill = input("Please enter the credit card number: ")
        print("payment done by credit")

        print(bill)
        cash(pid, name, bill)
        print("Thank you")
        last()
    else:
        print("not paid and go for payment")
        print("Thank You")
        last()

# ---When you open the program....
print("---------------------------------------")

print("Options:\n1=Register \n2=Appointment\n3=Patient Treatment Plan\n4=Accountant \n5=Exit")
while True:
    option = input("> ")
    if option == "1":
        Register()
    elif option == "2":
        Appointment()
    elif option=="3":
        PTP()
    elif option == "4":
        Accountant()
    elif option == "5":
        print("Shutting down")
        break
    else:
        print(option + " is not an option")
print("-----------------------------------------")
# On exit
print("Shutting down....")
time.sleep(1)



