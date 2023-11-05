from pkg.flat.bill import Bill
from pkg.flat.flatmate import Flatmate
from pkg.exporter.pdf import PDFExporter

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
