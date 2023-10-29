from typing import List
from fpdf import FPDF


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
    def __init__(self, amount: int, flatmates: List[Flatmate], days = 30) -> None:
        self.amount = amount
        self.days = days
        self.flatmates = flatmates
        
        self.total_days = self.calc_total_days()
        self.amt_per_days = self.amount / self.total_days

    def calc_total_days(self) -> int:
        total_days = 0
        for flatmate in self.flatmates:
            total_days += flatmate.days
        return total_days

    def calculate(self, flatmate: Flatmate) -> float:
        return self.amt_per_days * flatmate.days
        

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
        
        # Add title
        pdf.set_font(family="Times", size=24)
        pdf.cell(w=0, h=50, txt="Flamate Bill sharing", border=border, ln=1)

        # Add metadata
        pdf.set_font(family="Times", size=20)
        pdf.cell(w=200, h=100, txt="Number of Days", border=border)
        pdf.cell(w=200, h=100, txt=str(self.bill.days), border=border, ln=1)

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

if __name__ == "__main__":
    flatmate1 = Flatmate("Thang", 25)
    flatmate2 = Flatmate("Kem", 15)
    
    lexington = Bill(10000, [flatmate1, flatmate2], 30)
    print(lexington.calculate(flatmate1))
    print(lexington.calculate(flatmate2))

    pdf_export = PDFExporter(lexington)
    pdf_export.export(border=False)
