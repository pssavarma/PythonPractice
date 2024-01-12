from docx import Document
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def convert_word_to_pdf(input_file, output_file):
    doc = Document(input_file)

    pdf_canvas = canvas.Canvas(output_file, pagesize=letter)
    width, height = letter

    pdf_canvas.setFont("Helvetica", 12)

    for paragraph in doc.paragraphs:
        pdf_canvas.drawString(50, height - 50, paragraph.text)
        height -= 20  # Adjust the vertical position

    pdf_canvas.save()

if __name__ == "__main__":
    word_input = "/Users/saisriadityavarmapenmetsa/Documents/Personal Projects/Converter/Test Outputs/MAIN_Cover_Letter_template_MIM_MBA.1394769332.docx"
    pdf_output = "/Users/saisriadityavarmapenmetsa/Documents/Personal Projects/Converter/Test Outputs/New_auto.pdf"
    
    convert_word_to_pdf(word_input, pdf_output)

