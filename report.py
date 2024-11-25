import webbrowser, os
from fpdf import FPDF
from filestack import Client


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
        pdf.image(r'files/house.png')

        # insert title
        pdf.set_font('Times', 'B', 24)
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align='C', ln=1)

        #insert period label/value
        pdf.set_font('Times', 'B', 14)
        pdf.cell(w=80, h=40, txt="Period:", border=1)
        pdf.cell(w=175, h=40, txt=bill.period, border=1, ln=1)

        # insert name and amount due for flatmate1
        pdf.set_font('Times', size=12)
        pdf.cell(w=80, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=175, h=40, txt=flatmate1_pay, border=1, ln=1)

        # insert name and amount due for flatmate2
        pdf.set_font('Times', size=12)
        pdf.cell(w=80, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=175, h=40, txt=flatmate2_pay, border=1, ln=1)

        os.chdir("files")
        pdf.output(self.filename)
        webbrowser.open(self.filename)


class FileSharer:
    def __init__(self, filepath, api_key='ABqQzqBpJR3mqIss7ZB3oz'):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        client = Client(self.api_key)

        new_filelink = client.upload(filepath=self.filepath)
        print(new_filelink.url)

