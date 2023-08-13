from fpdf import FPDF

def main():
    print_shirt(input("Name: ").strip())


def print_shirt(name):
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.add_page()
    pdf.set_font("helvetica", size = 48)
    pdf.cell(0,57,'CS50 Shirtificate', align='C')
    pdf.image("shirtificate.png", x=10, y=70,  w=190, keep_aspect_ratio=True)
    pdf.set_font("helvetica", size = 24)
    pdf.set_text_color(255,255,255)
    pdf.set_y(108)
    pdf.cell(0,57,f"{name} took CS50", align='C')
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()