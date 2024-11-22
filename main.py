from fpdf import FPDF


class Bill:
    """
    Creates an object of Bill class, contains data about an expense (amount and period)
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Creates and object of a Flatmate class,
    contains data about the flatmate and amount of time they spent in the home
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house


    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Creates a PDF with data about the bill & the split.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #add icon
        pdf.image(r'C:\Users\alexb\PycharmProjects\App-2-Flatmates-Bill\files\house.png')

        # insert title
        pdf.set_font('Times', 'B', 24)
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align='C', ln=1)

        #insert period label/value
        pdf.cell(w=80, h=40, txt="Period:", border=1)
        pdf.cell(w=175, h=40, txt=bill.period, border=1, ln=1)

        # insert name and amount due for flatmate1
        pdf.cell(w=80, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=175, h=40, txt=flatmate1_pay, border=1, ln=1)

        # insert name and amount due for flatmate2
        pdf.cell(w=80, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=175, h=40, txt=flatmate2_pay, border=1, ln=1)

        pdf.output(self.filename)


the_bill = Bill(amount=120, period="October 2024")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print(f'John pays: {john.pays(bill=the_bill, flatmate2=marry)}')
print(f'Marry pays: {marry.pays(bill=the_bill, flatmate2=john)}')

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=john, flatmate2=marry, bill=the_bill)
