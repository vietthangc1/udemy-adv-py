from typing import List
from fpdf import FPDF
import webbrowser
import os
from datetime import datetime
import calendar


class Flatmate:
    """
    Contains information about flatmates who share the bill,
    including name and days in house
    """
    def __init__(self, name: str, days = 30) -> None:
        self.name = name
        self.days = days


class Bill:
    """
    Contains information about monthly Bill,
    including amount, period in days
    """
    def __init__(self, amount: int, flatmates: List[Flatmate], period = "Dec 2020") -> None:
        self.amount = amount
        self.flatmates = flatmates
        self.period = period
        
        self.total_days = self.calc_total_days()
        self.amt_per_days = self.amount / self.total_days
        self.days = self.month_days()

    def calc_total_days(self) -> int:
        total_days = 0
        for flatmate in self.flatmates:
            total_days += flatmate.days
        return total_days

    def calculate(self, flatmate: Flatmate) -> float:
        return self.amt_per_days * flatmate.days
        
    def month_days(self) -> int:
        period_parsed = datetime.strptime(self.period, "%b %Y")
        month = period_parsed.month
        year = period_parsed.year
        return calendar.monthrange(year, month)[1]


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
        webbrowser.open("file://"+os.path.realpath(filename))

if __name__ == "__main__":
    bill_amount = eval(input("Bill amount: "))
    period = input("Bill period (e.g: Dec 2020): ")
    num_flatmates = int(input("Number of Flatmates: "))

    list_flatmates = []
    for i in range(num_flatmates):
        prompt_name = "Flatmate " + str(i+1) + " name: "
        prompt_days = "Flatmate " + str(i+1) + " days occupied: "
        
        name = input(prompt_name)
        days = int(input(prompt_days))

        list_flatmates.append(Flatmate(name, days))

    bill_instance = Bill(bill_amount, list_flatmates, period)

    pdf_export = PDFExporter(bill_instance)
    pdf_export.export(border=False)
