from fpdf import FPDF

pdf = FPDF(
    orientation="P",
    unit="pt",
    format="A4",
)

pdf.add_page()
