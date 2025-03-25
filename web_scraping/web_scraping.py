import requests
from bs4 import BeautifulSoup
import zipfile
import os

url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

def find_pdf_links(url):
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.content, 'html.parser')
    pdf_links = []
    for a in soup.find_all('a', href=True):
        href = a['href']
        if href.endswith('.pdf') and ('Anexo I' in a.text or 'Anexo II' in a.text):
            if not href.startswith('http'):
                href = url + href
            pdf_links.append(href)
    return pdf_links

def download_pdf(url, filename):
    response = requests.get(url, stream=True)
    response.raise_for_status()
    with open(filename, 'wb') as pdf_file:
        for chunk in response.iter_content(chunk_size=8192):
            pdf_file.write(chunk)

def compress_files(filenames, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for filename in filenames:
            zipf.write(filename, os.path.basename(filename))

def main():
    pdf_links = find_pdf_links(url)
    print("Links encontrados:", pdf_links)

    filenames = []
    for link in pdf_links:
        filename = link.split('/')[-1]
        print(f"Baixando {filename}...")
        try:
            download_pdf(link, filename)
            filenames.append(filename)
        except Exception as e:
            print(f"Erro ao baixar {filename}: {e}")

    zip_filename = "Anexos_ANS.zip"
    compress_files(filenames, zip_filename)

    print(f"Arquivos compactados em '{zip_filename}' com sucesso.")

if __name__ == "__main__":
    main()