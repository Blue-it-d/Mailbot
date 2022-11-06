# function to generate pdf from a given text and a given template
def generate_pdf(text, name):
    # import fpdf
    from fpdf import FPDF
    # add text to the pdf
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=text, ln=1, align="C")
    # save the pdf with name
    pdf.output(name)



# Test generating a pdf 

text = """
Some Text 1!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
generate_pdf(text, "new1.pdf")

