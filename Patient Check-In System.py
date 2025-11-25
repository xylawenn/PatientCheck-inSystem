patients = []  
queue_number = 1

while True:
    print("\n===== Patient Check-in System =====")
    print("1. Clinic Staff/Nurse")
    print("2. Doctor/Medical Officer")
    print("3. Exit")
    
    choice = input("Choose user role: ").strip()

    if choice == "1":
        # Clinic Staff/Nurse functions
        print("\n--- Clinic Staff/Nurse Panel ---")
        name = input("Enter patient name: ").strip()
        concern = input("Enter patient concern: ").strip()
        
        if name == "" or concern == "":
              print("\nPlease, Enter your response! ")      
                                  
        else:             
              patients.append({"queue": queue_number, "name": name, "concern": concern})
              print(f"Patient registered successfully! Assigned Queue Number: {queue_number}")
              queue_number += 1
              
    elif choice == "2":
        # Doctor/Medical Officer functions
        print("\n--- Doctor/Medical Officer Panel ---")
        if not patients:
            print("No patients in queue.")
        else:
            print("\nCurrent Queue List:")
            for p in patients:
                print(f"Queue {p['queue']}: {p['name']} - {p['concern']}")
            
            call = input("\nCall next patient? (y/n): ")
            if call.lower() == 'y':
                next_patient = patients.pop(0)
                print(f"\nCalling Patient {next_patient['queue']}: {next_patient['name']}")
                
                # Reset queue number to 1
                if len(patients) == 0:
                    queue_number = 1
                
    elif choice == "3":
        print("Exiting system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")