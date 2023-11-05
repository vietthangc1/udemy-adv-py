import os
import webbrowser
from fpdf import FPDF
from ..flat.bill import Bill
from filestack import Client


class PDFExporter:
    def __init__(self, bill: Bill) -> None:
        self.bill = bill

    def export(self, filename:str = "Billing.pdf", border = True) -> None:
        pdf = FPDF(
            orientation="P",
            unit="pt",
            format="A4",
        )

        pdf.add_page()

        # Add icon
        pdf.image("https://cdn-icons-png.flaticon.com/512/4752/4752101.png", w=30, h=30)
        
        # Add title
        pdf.set_font(family="Times", size=24)
        pdf.cell(w=0, h=50, txt="Flamate Bill sharing", border=border, ln=1)

        # Add metadata
        pdf.set_font(family="Times", size=20)
        pdf.cell(w=200, h=100, txt="Number of Days", border=border)
        pdf.cell(w=200, h=100, txt=str(self.bill.days), border=border)
        pdf.cell(w=100, h=100, txt=str(self.bill.amount), border=border, ln=1)

        # Add column headers
        pdf.cell(w=200, h=40, txt="Flatmate name", border=border)
        pdf.cell(w=50, h=40, txt="Days", border=border)
        pdf.cell(w=100, h=40, txt="Amount", border=border, ln=1)

        # Add Flatmates
        for flatmate in self.bill.flatmates:
            amount = self.bill.calculate(flatmate)
            pdf.set_font(family="Times", size=16)
            pdf.cell(w=200, h=40, txt=flatmate.name, border=border)
            pdf.cell(w=50, h=40, txt=str(flatmate.days), border=border)
            pdf.cell(w=100, h=40, txt="{:,.0f}".format(amount), border=border, ln=1)

        # Save to Billing.pdf 
        pdf.output(filename)

class FileStackUpload:
    def __init__(self) -> None:
        client = Client('ATidPNVyQpa7QEPmuutgfz')
        self.client = client

    def upload(self, filepath = "Billing.pdf"):
        new_fileline = self.client.upload(filepath=filepath)
        return new_fileline.url