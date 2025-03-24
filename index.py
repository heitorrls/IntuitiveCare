import pdfplumber
import pandas as pd
import zipfile
import os

def extract_tables_from_pdf(pdf_path):
    all_tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            tables = page.extract_tables()
            all_tables.extend(tables)
    return all_tables

def structure_data(tables):
    structured_data = []
    for table in tables:
        for row in table:
            structured_data.append(row)
    return structured_data

def replace_abbreviations(data):
    for row in data:
        for i, cell in enumerate(row):
            if cell == 'OD':
                row[i] = 'Seg. Odontológica'
            elif cell == 'AMB':
                row[i] = 'Seg. Ambulatorial'
    return data

def save_to_csv(data, csv_filename):
    df = pd.DataFrame(data)
    df.to_csv(csv_filename, index=False, encoding='utf-8')

def compress_file(csv_filename, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipf.write(csv_filename, os.path.basename(csv_filename))

def main(pdf_path, your_name):
    csv_filename = f"Teste_{your_name}.csv"
    zip_filename = f"Teste_{your_name}.zip"

    tables = extract_tables_from_pdf(pdf_path)
    structured_data = structure_data(tables)
    replaced_data = replace_abbreviations(structured_data)
    save_to_csv(replaced_data, csv_filename)
    compress_file(csv_filename, zip_filename)

    print(f"Arquivo CSV '{csv_filename}' criado com sucesso.")
    print(f"Arquivo ZIP '{zip_filename}' criado com sucesso.")

if __name__ == "__main__":
    pdf_path = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
    your_name = "Heitor_Luiz_de_Souza_Carvalho_de_Miranda"  
    main(pdf_path, your_name)