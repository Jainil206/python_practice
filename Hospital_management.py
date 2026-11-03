
patients = [
    {"id": 101, "name": "Rahul", "age": 25, "gender": "Male", "disease": "Fever", "doctor_id": 201, "room_no": 101, "bill": 5000, "payment": "Unpaid", "status": "Admitted"},
    {"id": 102, "name": "Priya", "age": 30, "gender": "Female", "disease": "Flu", "doctor_id": 202, "room_no": 102, "bill": 3000, "payment": "Paid", "status": "Admitted"},
    {"id": 103, "name": "Amit", "age": 40, "gender": "Male", "disease": "Fracture", "doctor_id": 201, "room_no": 103, "bill": 10000, "payment": "Unpaid", "status": "Admitted"}
]

doctors = [
    {"id": 201, "name": "Dr. Sharma", "specialization": "General Physician", "fee": 1000},
    {"id": 202, "name": "Dr. Patel", "specialization": "Cardiologist", "fee": 1500}
]

appointments = []


def room_available(room_no, patient_id=None):
    for patient in patients:
        if patient["room_no"] == room_no and patient["status"] == "Admitted":
            if patient["id"] != patient_id:
                return False

    return True


def get_doctor_fee(doctor_id):
    for doctor in doctors:
        if doctor["id"] == doctor_id:
            return doctor["fee"]

    return 0


def add_patient():
    patient_id = int(input("Enter Patient ID: "))

    for patient in patients:
        if patient["id"] == patient_id:
            print("Patient ID already exists!")
            return

    name = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))
    gender = input("Enter Gender: ")
    disease = input("Enter Disease: ")
    doctor_id = int(input("Enter Doctor ID: "))
    room_no = int(input("Enter Room Number: "))
    bill = float(input("Enter Patient Bill: "))

    if name == "" or age <= 0 or gender == "" or disease == "" or room_no <= 0 or bill < 0:
        print("Enter valid patient details!")
        return

    if not room_available(room_no):
        print("Room is already occupied!")
        return

    if get_doctor_fee(doctor_id) == 0:
        print("Doctor not found!")
        return

    patient = {
        "id": patient_id,
        "name": name,
        "age": age,
        "gender": gender,
        "disease": disease,
        "doctor_id": doctor_id,
        "room_no": room_no,
        "bill": bill,
        "payment": "Unpaid",
        "status": "Admitted"
    }

    patients.append(patient)
    print("Patient added successfully!")


def display_patients():
    if len(patients) == 0:
        print("No patients available!")
        return

    print("\n---------------- PATIENT RECORDS ----------------")

    for patient in patients:
        print("\nPatient ID:", patient["id"])
        print("Name:", patient["name"])
        print("Age:", patient["age"])
        print("Gender:", patient["gender"])
        print("Disease:", patient["disease"])
        print("Doctor ID:", patient["doctor_id"])
        print("Room:", patient["room_no"])
        print("Bill:", patient["bill"])
        print("Payment:", patient["payment"])
        print("Status:", patient["status"])


def search_patient():
    patient_id = int(input("Enter Patient ID to search: "))

    for patient in patients:
        if patient["id"] == patient_id:
            print("\nPatient Found!")
            print("ID:", patient["id"])
            print("Name:", patient["name"])
            print("Age:", patient["age"])
            print("Gender:", patient["gender"])
            print("Disease:", patient["disease"])
            print("Doctor ID:", patient["doctor_id"])
            print("Room:", patient["room_no"])
            print("Bill:", patient["bill"])
            print("Payment:", patient["payment"])
            print("Status:", patient["status"])
            return

    print("Patient not found!")


def update_patient():
    patient_id = int(input("Enter Patient ID to update: "))

    for patient in patients:
        if patient["id"] == patient_id:

            print("\n1. Update Name")
            print("2. Update Age")
            print("3. Update Disease")
            print("4. Update Doctor")
            print("5. Update Room")
            print("6. Update Bill")

            choice = input("Enter your choice: ")

            if choice == "1":
                name = input("Enter new name: ")

                if name != "":
                    patient["name"] = name
                    print("Name updated successfully!")
                else:
                    print("Invalid name!")

            elif choice == "2":
                age = int(input("Enter new age: "))

                if age > 0:
                    patient["age"] = age
                    print("Age updated successfully!")
                else:
                    print("Invalid age!")

            elif choice == "3":
                disease = input("Enter new disease: ")

                if disease != "":
                    patient["disease"] = disease
                    print("Disease updated successfully!")
                else:
                    print("Invalid disease!")

            elif choice == "4":
                doctor_id = int(input("Enter new Doctor ID: "))

                if get_doctor_fee(doctor_id) > 0:
                    patient["doctor_id"] = doctor_id
                    print("Doctor updated successfully!")
                else:
                    print("Doctor not found!")

            elif choice == "5":
                room_no = int(input("Enter new room number: "))

                if room_no <= 0:
                    print("Invalid room number!")

                elif patient["status"] == "Discharged":
                    print("Cannot change room of discharged patient!")

                elif room_available(room_no, patient_id):
                    patient["room_no"] = room_no
                    print("Room updated successfully!")

                else:
                    print("Room is already occupied!")

            elif choice == "6":
                bill = float(input("Enter new bill: "))

                if bill >= 0:
                    patient["bill"] = bill
                    print("Bill updated successfully!")
                else:
                    print("Invalid bill!")

            else:
                print("Invalid choice!")

            return

    print("Patient not found!")


def delete_patient():
    patient_id = int(input("Enter Patient ID to delete: "))

    for patient in patients:
        if patient["id"] == patient_id:
            patients.remove(patient)
            print("Patient deleted successfully!")
            return

    print("Patient not found!")


def add_doctor():
    doctor_id = int(input("Enter Doctor ID: "))

    for doctor in doctors:
        if doctor["id"] == doctor_id:
            print("Doctor ID already exists!")
            return

    name = input("Enter Doctor Name: ")
    specialization = input("Enter Specialization: ")
    fee = float(input("Enter Consultation Fee: "))

    if name == "" or specialization == "" or fee <= 0:
        print("Enter valid doctor details!")
        return

    doctor = {
        "id": doctor_id,
        "name": name,
        "specialization": specialization,
        "fee": fee
    }

    doctors.append(doctor)
    print("Doctor added successfully!")


def display_doctors():
    if len(doctors) == 0:
        print("No doctors available!")
        return

    print("\n---------------- DOCTOR RECORDS ----------------")

    for doctor in doctors:
        print("\nDoctor ID:", doctor["id"])
        print("Name:", doctor["name"])
        print("Specialization:", doctor["specialization"])
        print("Consultation Fee:", doctor["fee"])


# NEW FEATURE 1: Search doctors by specialization

def search_doctor():
    specialization = input("Enter Doctor Specialization: ").strip().lower()

    found = False

    for doctor in doctors:
        if doctor["specialization"].lower() == specialization:
            print("\nDoctor Found!")
            print("ID:", doctor["id"])
            print("Name:", doctor["name"])
            print("Specialization:", doctor["specialization"])
            print("Fee:", doctor["fee"])
            found = True

    if not found:
        print("No doctor found with this specialization!")


def book_appointment():
    appointment_id = int(input("Enter Appointment ID: "))

    for appointment in appointments:
        if appointment["id"] == appointment_id:
            print("Appointment ID already exists!")
            return

    patient_id = int(input("Enter Patient ID: "))
    doctor_id = int(input("Enter Doctor ID: "))
    date = input("Enter Appointment Date: ")

    patient_exists = False
    doctor_exists = False

    for patient in patients:
        if patient["id"] == patient_id:
            if patient["status"] == "Admitted":
                patient_exists = True
            break

    for doctor in doctors:
        if doctor["id"] == doctor_id:
            doctor_exists = True
            break

    if not patient_exists:
        print("Admitted patient not found!")
        return

    if not doctor_exists:
        print("Doctor not found!")
        return

    if date == "":
        print("Invalid appointment date!")
        return

    appointment = {
        "id": appointment_id,
        "patient_id": patient_id,
        "doctor_id": doctor_id,
        "date": date
    }

    appointments.append(appointment)
    print("Appointment booked successfully!")


def display_appointments():
    if len(appointments) == 0:
        print("No appointments available!")
        return

    print("\n---------------- APPOINTMENTS ----------------")

    for appointment in appointments:
        print("\nAppointment ID:", appointment["id"])
        print("Patient ID:", appointment["patient_id"])
        print("Doctor ID:", appointment["doctor_id"])
        print("Date:", appointment["date"])


# NEW FEATURE 2: Cancel appointment

def cancel_appointment():
    appointment_id = int(input("Enter Appointment ID to cancel: "))

    for appointment in appointments:
        if appointment["id"] == appointment_id:
            appointments.remove(appointment)
            print("Appointment cancelled successfully!")
            return

    print("Appointment not found!")


def generate_bill():
    patient_id = int(input("Enter Patient ID: "))

    for patient in patients:
        if patient["id"] == patient_id:

            doctor_fee = get_doctor_fee(patient["doctor_id"])
            total = patient["bill"] + doctor_fee

            print("\n========== HOSPITAL FINAL BILL ==========")
            print("Patient ID:", patient["id"])
            print("Patient Name:", patient["name"])
            print("Disease:", patient["disease"])
            print("Doctor Fee:", doctor_fee)
            print("Treatment Charges:", patient["bill"])
            print("-----------------------------------------")
            print("Total Amount:", total)
            print("Payment Status:", patient["payment"])
            print("=========================================")
            return

    print("Patient not found!")


# NEW FEATURE 3: Payment system

def update_payment():
    patient_id = int(input("Enter Patient ID: "))

    for patient in patients:
        if patient["id"] == patient_id:

            print("\nCurrent Payment Status:", patient["payment"])
            print("1. Mark as Paid")
            print("2. Mark as Unpaid")

            choice = input("Enter your choice: ")

            if choice == "1":
                patient["payment"] = "Paid"
                print("Payment updated to PAID!")

            elif choice == "2":
                patient["payment"] = "Unpaid"
                print("Payment updated to UNPAID!")

            else:
                print("Invalid choice!")

            return

    print("Patient not found!")


# NEW FEATURE 4: Discharge summary

def discharge_summary():
    patient_id = int(input("Enter Patient ID: "))

    for patient in patients:
        if patient["id"] == patient_id:

            if patient["status"] == "Discharged":
                print("Patient is already discharged!")
                return

            doctor_name = "Not Found"

            for doctor in doctors:
                if doctor["id"] == patient["doctor_id"]:
                    doctor_name = doctor["name"]
                    break

            doctor_fee = get_doctor_fee(patient["doctor_id"])
            total = patient["bill"] + doctor_fee

            print("\n========== PATIENT DISCHARGE SUMMARY ==========")
            print("Patient ID:", patient["id"])
            print("Patient Name:", patient["name"])
            print("Age:", patient["age"])
            print("Gender:", patient["gender"])
            print("Disease:", patient["disease"])
            print("Treating Doctor:", doctor_name)
            print("Room Number:", patient["room_no"])
            print("-----------------------------------------------")
            print("Treatment Charges:", patient["bill"])
            print("Doctor Fee:", doctor_fee)
            print("Total Bill:", total)
            print("Payment Status:", patient["payment"])
            print("-----------------------------------------------")

            if patient["payment"] == "Unpaid":
                print("WARNING: Patient has pending payment!")

            print("Patient Status: Discharged")
            print("Thank you for choosing our hospital!")
            print("===============================================")

            patient["status"] = "Discharged"

            print("Patient discharged successfully!")
            return

    print("Patient not found!")


# NEW FEATURE 5: Room availability display

def display_rooms():
    print("\n========== ROOM AVAILABILITY ==========")

    for room_no in range(101, 111):

        if room_available(room_no):
            print("Room", room_no, "- Available")
        else:
            print("Room", room_no, "- Occupied")


def total_hospital_revenue():
    paid_total = 0
    unpaid_total = 0

    for patient in patients:
        total = patient["bill"] + get_doctor_fee(patient["doctor_id"])

        if patient["payment"] == "Paid":
            paid_total += total
        else:
            unpaid_total += total

    print("\n========== HOSPITAL FINANCIAL REPORT ==========")
    print("Total Paid Revenue:", paid_total)
    print("Total Pending Payments:", unpaid_total)
    print("Total Billing Amount:", paid_total + unpaid_total)


while True:

    print("\n========== HOSPITAL MANAGEMENT SYSTEM ==========")

    print("1. Add Patient")
    print("2. Display All Patients")
    print("3. Search Patient")
    print("4. Update Patient")
    print("5. Delete Patient")
    print("6. Add Doctor")
    print("7. Display All Doctors")
    print("8. Book Appointment")
    print("9. Display Appointments")
    print("10. Generate Patient Bill")
    print("11. Calculate Hospital Revenue")
    print("12. Check Room Availability")
    print("13. Update Payment Status")
    print("14. Cancel Appointment")
    print("15. Search Doctor by Specialization")
    print("16. Generate Discharge Summary")
    print("17. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_patient()

    elif choice == "2":
        display_patients()

    elif choice == "3":
        search_patient()

    elif choice == "4":
        update_patient()

    elif choice == "5":
        delete_patient()

    elif choice == "6":
        add_doctor()

    elif choice == "7":
        display_doctors()

    elif choice == "8":
        book_appointment()

    elif choice == "9":
        display_appointments()

    elif choice == "10":
        generate_bill()

    elif choice == "11":
        total_hospital_revenue()

    elif choice == "12":
        display_rooms()

    elif choice == "13":
        update_payment()

    elif choice == "14":
        cancel_appointment()

    elif choice == "15":
        search_doctor()

    elif choice == "16":
        discharge_summary()

    elif choice == "17":
        print("Thank you for using Hospital Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
