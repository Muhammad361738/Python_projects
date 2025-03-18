# f Dr. Sarah selects Book New Appointment, she enters the patient's name,
# selects a preferred date, and the system suggests available time slots. 
# She chooses a slot, and the system confirms the appointment.

patient_list = ["talha","zain","waqar","salman","usama"]
time_slot = ["9 To 10 AM","4 To 5 PM" , "8 To 9 PM"]

appointment_patient_list = []

def new_appointment(name,select_time):
    if name in patient_list :
        if select_time == "1" or select_time == "2" or select_time == "3":
            print(f"New Apointment Confirmed with {name} at {time_slot[int(select_time)-1]}")
            appointment_patient_list.append({"Patient name":name,"Time slot":time_slot[int(select_time)-1]})
            print(appointment_patient_list)
        else:
            print("Enter the available slot ont this time you have not available")
    else:
        print("This name patient is not in our system please enter the valid name")   
 
def reshudle_appointment(name,select_time):
    if name in patient_list :
        if select_time == "1" or select_time == "2" or select_time == "3":
            print(f"Reshudale  Apointment Confirmed with {name} at {time_slot[int(select_time)-1]}")
            appointment_patient_list.append({"Patient name":name,"Time slot":time_slot[int(select_time)-1]})
            print(appointment_patient_list)
        else:
            print("Enter the available slot ont this time you have not available")
    else:
        print("This name patient is not in our system please enter the valid name")   
 
    
        
        
 
 
 
 
   
def remve_appointment():
    print("remove appointment")
condition = True
while(condition):

    print("1 : New Apointment \n")
    print("2 : Reshudle Apointment \n")
    print("3 : Cancel Apointment \n")
    user_req = input("Enter the option from above section use (1,2,3) for selection \n : ")

    if user_req == "1":
        patient_name = input("Enter the patient name for confirm the appointment \n : ").lower()
        # print("Select the time slot ",time_slot[::])
        for i,mytime in enumerate( time_slot,1):
            print(f"{i} :  {mytime}")   
        doc_time = input("Enter the available time slot  for confirm the appointment \n : ")
        new_appointment(patient_name,doc_time)




    elif user_req == "2":
    
        for key , value in appointment_patient_list:
         print(f"{key} : {value}")
        
        want_reshudle = input("Enter the patent number which you want to reshudele")
    
        for i,mytime in enumerate( time_slot,1):
             print(f"{i} :  {mytime}")   
        doc_time = input("Enter the available time slot  for confirm the appointment \n : ")
  

        reshudle_appointment(want_reshudle,doc_time)    
    elif user_req == "3":
        remve_appointment()
    elif user_req == "exit":
        break
    else:
        print("Enter the valid input ")

   