import os
import fitz  # PyMuPDF

def split_pdf_into_sections(input_pdf, output_folder, section_height):
    pdf_document = fitz.open(input_pdf)
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        page_height = page.rect.height
        num_sections = int(page_height / section_height)
        for section_num in range(num_sections):
            section_start_y = section_num * section_height
            section_end_y = min((section_num + 1) * section_height, page_height)
            output_pdf = os.path.join(output_folder, f'page_{page_num + 1}_section_{section_num + 1}.pdf')
            new_document = fitz.open()
            new_page = new_document.new_page(width=page.rect.width, height=section_end_y - section_start_y)
            new_page.show_pdf_page(new_page.rect, pdf_document, page_num, clip=(0, section_start_y, page.rect.width, section_end_y))
            new_document.save(output_pdf)
            new_document.close()

# Example usage:
input_pdf = 'main/main.pdf'  # Replace with your input PDF file
output_folder = 'pages'  # Folder where the output pages will be saved
section_height = 250  # Set the height of each section in points (1 point = 1/72 inch)

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

split_pdf_into_sections(input_pdf, output_folder, section_height)
