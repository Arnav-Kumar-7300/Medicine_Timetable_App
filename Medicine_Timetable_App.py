# Medicine Timetable App

medicines = []   # list to store medicines

while True:
    print("\n===== MEDICINE TIMETABLE APP =====")
    print("1. Add Medicine")
    print("2. View Medicine Timetable")
    print("3. Update Medicine")
    print("4. Delete Medicine")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # ---------------- ADD MEDICINE ----------------
    if choice == "1":
        name = input("Enter medicine name: ")
        time = input("Enter time (HH:MM, 24-hour format): ")
        dose = input("Enter dosage (e.g., 1 tablet): ")

        medicine = {"name": name, "time": time, "dose": dose}
        medicines.append(medicine)

        print("Medicine added successfully!")

    # ---------------- VIEW MEDICINE ----------------
    elif choice == "2":
        if len(medicines) == 0:
            print("No medicines added yet.")
        else:
            print("\n--- Medicine Timetable ---")
            for i in range(len(medicines)):
                print(f"{i+1}. {medicines[i]['name']} - {medicines[i]['time']} - {medicines[i]['dose']}")

    # ---------------- UPDATE MEDICINE ----------------
    elif choice == "3":
        if len(medicines) == 0:
            print("No medicines to update.")
        else:
            for i in range(len(medicines)):
                print(f"{i+1}. {medicines[i]['name']} - {medicines[i]['time']} - {medicines[i]['dose']}")

            index = int(input("Enter medicine number to update: ")) - 1

            if 0 <= index < len(medicines):
                new_name = input("Enter new name: ")
                new_time = input("Enter new time (HH:MM): ")
                new_dose = input("Enter new dosage: ")

                medicines[index]["name"] = new_name
                medicines[index]["time"] = new_time
                medicines[index]["dose"] = new_dose

                print("Medicine updated successfully!")
            else:
                print("Invalid medicine number!")

    # ---------------- DELETE MEDICINE ----------------
    elif choice == "4":
        if len(medicines) == 0:
            print("No medicines to delete.")
        else:
            for i in range(len(medicines)):
                print(f"{i+1}. {medicines[i]['name']} - {medicines[i]['time']} - {medicines[i]['dose']}")

            index = int(input("Enter medicine number to delete: ")) - 1

            if 0 <= index < len(medicines):
                medicines.pop(index)
                print("Medicine deleted successfully!")
            else:
                print("Invalid medicine number!")

    # ---------------- EXIT ----------------
    elif choice == "5":
        print("Exiting the program. Thank you!")
        break

    # ---------------- INVALID OPTION ----------------
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
