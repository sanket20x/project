def da():
    d = {}
    n = int(input("Enter the number of doctors: "))
    for i in range(n):
        cno = input("Enter contact number for doctor {}: ".format(i + 1))
        exp = input("Enter expertise for doctor {}: ".format(i + 1))
        d[i + 1] = {"contact_number": cno, "expertise": exp}
    return d
    
def e(d, p):
    for dr_id, dd in d.items():
        if dd["expertise"].lower() == p.lower():
            print("Doctor {}, Contact Number: {}".format(dr_id, dd["contact_number"]))
            return 
    print("No matching emergency contact found.")

di = da()

s = input("Enter the patient's emergency: ")
e(di, s)
