import os
import fitz  # PyMuPDF
import re

def find_groupe_value(pdf_path):
    doc = fitz.open(pdf_path)
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        match = re.search(r'Groupe:\s*(\w+)', text)
        if match:
            groupe_value = match.group(1)
            doc.close()
            return groupe_value
    doc.close()
    return None

def rename_pdf_with_groupe_value(pdf_path, output_folder):
    groupe_value = find_groupe_value(pdf_path)
    if groupe_value:
        new_name = f'{groupe_value}.pdf'
        output_path = os.path.join(output_folder, new_name)
        os.rename(pdf_path, output_path)
        print(f'Renamed {pdf_path} to {output_path}')
    else:
        print(f'No "Groupe" value found in {pdf_path}')

# Example usage:
input_folder = 'pages'  # Folder containing the PDFs
output_folder = 'renamed_pages'  # Folder where the renamed PDFs will be saved

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join(input_folder, filename)
        rename_pdf_with_groupe_value(pdf_path, output_folder)
