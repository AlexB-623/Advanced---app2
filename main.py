from flat import Bill, Flatmate
from report import PdfReport, FileSharer


def dih_validator(who):
    """
    This function validates that days-in-house is an integer
    :param who: flatmate name variable
    :return: integer for days-in-house
    """
    while True:
        user_input = input(f"How many days in the bill period was {who} in the house? ")
        try:
            dih = int(user_input)
            break
        except ValueError:
            print("Please only enter whole numbers, i.e. 25 30 or 16")
    return dih


#while loop to validate bill amount input:
while True:
    bill_input = input("Please enter the bill amount: ")
    try:
        bill_amount = float(bill_input)
        break
    except ValueError:
        print("Please enter only numeric values in the following format: 000.00")

bill_period = input("Please enter the bill's date period: ")
flat_mate_1 = input("Please enter your name: ")
#while loop to validate days input
fm1_dih = dih_validator(flat_mate_1)

flat_mate_2 = input("Please enter the other flatmate's name: ")
fm2_dih = dih_validator(flat_mate_2)


the_bill = Bill(amount=bill_amount, period=bill_period)
fm1 = Flatmate(name=flat_mate_1, days_in_house=fm1_dih)
fm2 = Flatmate(name=flat_mate_2, days_in_house=fm2_dih)

# print(f'John pays: {john.pays(bill=the_bill, flatmate2=marry)}')
# print(f'Marry pays: {marry.pays(bill=the_bill, flatmate2=john)}')

pdf_report = PdfReport(filename=f"{bill_period}.pdf")
pdf_report.generate(flatmate1=fm1, flatmate2=fm2, bill=the_bill)

file_sharer = FileSharer(filepath=pdf_report.filename)
print(file_sharer.share())
