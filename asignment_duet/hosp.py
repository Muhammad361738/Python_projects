
# patient_list = ["talha","zain","waqar","salman","usama"]
# time_slot = ["9 To 10 AM","4 To 5 PM" , "8 To 9 PM"]

# appointment_patient_list = []

# def new_appointment(name,select_time):
#     if name in patient_list :
#         if select_time == "1" or select_time == "2" or select_time == "3":
#             print(f"New Apointment Confirmed with {name} at {time_slot[int(select_time)-1]}")
#             appointment_patient_list.append({"Patient name":name,"Time slot":time_slot[int(select_time)-1]})
#             print(appointment_patient_list)
#         else:
#             print("Enter the available slot ont this time you have not available")
#     else:
#         print("This name patient is not in our system please enter the valid name")   
 
# def reshudle_appointment(name,select_time):
#     if name in patient_list :
#         if select_time == "1" or select_time == "2" or select_time == "3":
#             print(f"Reshudale  Apointment Confirmed with {name} at {time_slot[int(select_time)-1]}")
#             appointment_patient_list.append({"Patient name":name,"Time slot":time_slot[int(select_time)-1]})
#             print(appointment_patient_list)
#         else:
#             print("Enter the available slot ont this time you have not available")
#     else:
#         print("This name patient is not in our system please enter the valid name")   
   
# def remve_appointment():
#     print("remove appointment")
# condition = True
# while(condition):

#     print("1 : New Apointment \n")
#     print("2 : Reshudle Apointment \n")
#     print("3 : Cancel Apointment \n")
#     user_req = input("Enter the option from above section use (1,2,3) for selection \n : ")

#     if user_req == "1":
#         patient_name = input("Enter the patient name for confirm the appointment \n : ").lower()
#         # print("Select the time slot ",time_slot[::])
#         for i,mytime in enumerate( time_slot,1):
#             print(f"{i} :  {mytime}")   
#         doc_time = input("Enter the available time slot  for confirm the appointment \n : ")
#         new_appointment(patient_name,doc_time)




#     elif user_req == "2":
    
#         for key , value in enumerate(appointment_patient_list,1):
#          print(f" {key} : {value}")
        
#         want_reshudle = input("Enter the patent number which you want to reshudele")
    
#         for i,mytime in enumerate( time_slot,1):
#              print(f"{i} :  {mytime}")   
#         doc_time = input("Enter the available time slot  for confirm the appointment \n : ")
  

#         reshudle_appointment(want_reshudle,doc_time)    
#     elif user_req == "3":
#         remve_appointment()
#     elif user_req == "exit":
#         break
#     else:
#         print("Enter the valid input ")

   

# patient_list = ["talha","zain","waqar","salman","usama"]
# time_slot = ["9 To 10 AM","4 To 5 PM" , "8 To 9 PM"]

# appointment_patient_list = []

# def new_appointment(name, select_time):
#     if name in patient_list:
#         if select_time == "1" or select_time == "2" or select_time == "3":
#             print(f"New Appointment Confirmed with {name} at {time_slot[int(select_time) - 1]}")
#             appointment_patient_list.append({"Patient name": name, "Time slot": time_slot[int(select_time) - 1]})
#             print(appointment_patient_list)
#         else:
#             print("Enter the available slot, this time is not available")
#     else:
#         print("This patient name is not in our system, please enter a valid name")   

# def reshudle_appointment(patient_number, select_time):
#     if 1 <= patient_number <= len(appointment_patient_list):
#         patient_info = appointment_patient_list[patient_number - 1]
#         name = patient_info["Patient name"]
        
#         if select_time == "1" or select_time == "2" or select_time == "3":
#             print(f"Reschedule Appointment for {name} at {time_slot[int(select_time) - 1]}")
#             appointment_patient_list[patient_number - 1]["Time slot"] = time_slot[int(select_time) - 1]
#             print(appointment_patient_list)
#         else:
#             print("Enter the available slot, this time is not available")
#     else:
#         print("Invalid patient number. Please choose a valid number from the list.")

# def remove_appointment():
#     print("Remove appointment functionality not implemented yet")

# condition = True
# while condition:
#     print("1 : New Appointment \n")
#     print("2 : Reschedule Appointment \n")
#     print("3 : Cancel Appointment \n")
#     print("4 : Exit \n")
#     user_req = input("Enter the option from above section use (1, 2, 3) for selection \n : ")

#     if user_req == "1":
#         print("Patient List ")
#         for i, patient in enumerate(patient_list,1):
#             print(i," ",patient)
            
#         patient_name = input("Enter the patient name to confirm the appointment \n : ").lower()
#         for i, mytime in enumerate(time_slot, 1):
#             print(f"{i} :  {mytime}")   
#         doc_time = input("Enter the available time slot to confirm the appointment \n : ")
#         new_appointment(patient_name, doc_time)

#     elif user_req == "2":
#         for key, value in enumerate(appointment_patient_list, 1):
#             print(f"{key} : {value}")
        
#         want_reshudle = int(input("Enter the patient number you want to reschedule: "))
        
#         for i, mytime in enumerate(time_slot, 1):
#             print(f"{i} :  {mytime}")   
#         doc_time = input("Enter the available time slot to reschedule the appointment \n : ")

#         reshudle_appointment(want_reshudle, doc_time)    

#     elif user_req == "3":
#         remove_appointment()

#     elif user_req == "4":
#         break

#     else:
#         print("Enter a valid input")
patient_list = ["talha","zain","waqar","salman","usama"]
time_slot = ["9 To 10 AM","4 To 5 PM" , "8 To 9 PM"]

appointment_patient_list = []

def new_appointment(name, select_time):
    if name in patient_list:
        if select_time == "1" or select_time == "2" or select_time == "3":
            print(f"New Appointment Confirmed with {name} at {time_slot[int(select_time) - 1]}")
            appointment_patient_list.append({"Patient name": name, "Time slot": time_slot[int(select_time) - 1]})
            print(appointment_patient_list)
        else:
            print("Enter the available slot, this time is not available")
    else:
        print("This patient name is not in our system, please enter a valid name")   

def reshudle_appointment(patient_number, select_time):
    if 1 <= patient_number <= len(appointment_patient_list):
        patient_info = appointment_patient_list[patient_number - 1]
        name = patient_info["Patient name"]
        
        if select_time == "1" or select_time == "2" or select_time == "3":
            print(f"Reschedule Appointment for {name} at {time_slot[int(select_time) - 1]}")
            appointment_patient_list[patient_number - 1]["Time slot"] = time_slot[int(select_time) - 1]
            print(appointment_patient_list)
        else:
            print("Enter the available slot, this time is not available")
    else:
        print("Invalid patient number. Please choose a valid number from the list.")

def remove_appointment():
    if len(appointment_patient_list) == 0:
        print("No appointments to cancel. The list is empty.")
        return
    
    print("Current Appointments:")
    for idx, patient_info in enumerate(appointment_patient_list, 1):
        print(f"{idx}: {patient_info['Patient name']} - {patient_info['Time slot']}")
    
    try:
        patient_number = int(input("Enter the patient number to cancel the appointment: "))
        if 1 <= patient_number <= len(appointment_patient_list):
            removed_patient = appointment_patient_list.pop(patient_number - 1)
            print(f"Appointment for {removed_patient['Patient name']} at {removed_patient['Time slot']} has been canceled.")
        else:
            print("Invalid patient number. Please choose a valid number from the list.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

condition = True
while condition:
    print("1 : New Appointment \n")
    print("2 : Reschedule Appointment \n")
    print("3 : Cancel Appointment \n")
    print("4 : Exit \n")
    user_req = input("Enter the option from above section use (1, 2, 3) for selection \n : ")

    if user_req == "1":
        print("Patient List ")
        for i, patient in enumerate(patient_list,1):
            print(i," ",patient)
            
        patient_name = input("Enter the patient name to confirm the appointment \n : ").lower()
        for i, mytime in enumerate(time_slot, 1):
            print(f"{i} :  {mytime}")   
        doc_time = input("Enter the available time slot to confirm the appointment \n : ")
        new_appointment(patient_name, doc_time)

    elif user_req == "2":
        for key, value in enumerate(appointment_patient_list, 1):
            print(f"{key} : {value}")
        
        want_reshudle = int(input("Enter the patient number you want to reschedule: "))
        
        for i, mytime in enumerate(time_slot, 1):
            print(f"{i} :  {mytime}")   
        doc_time = input("Enter the available time slot to reschedule the appointment \n : ")

        reshudle_appointment(want_reshudle, doc_time)    

    elif user_req == "3":
        remove_appointment()

    elif user_req == "4":
        break

    else:
        print("Enter a valid input")
