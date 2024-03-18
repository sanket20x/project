def doctor():
    d = {}
    n = int(input("Enter the number of doctors: "))
    for i in range(n):
        cont = int(input("Enter contact number: "))
        exp = input("Enter expertise: ")
        d[cont] = exp
    print("Doctors dictionary:", d)
    return d

def patient(d, emergency):
    for cont, expertise in d.items():
        if expertise == emergency:
            print("Contact number: {}".format(cont))
            return
    print("No matching emergency contact found.")


doctors_dict = doctor()
emergency = input("Enter the patient's emergency: ")
patient(doctors_dict, emergency)
