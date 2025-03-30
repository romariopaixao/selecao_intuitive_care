import os
import requests
import zipfile
from datetime import datetime
from bs4 import BeautifulSoup

def main():
    # Criar diretório para salvar os downloads
    download_dir = "downloads"
    os.makedirs(download_dir, exist_ok=True)       
    
    
    # Lista para armazenar os caminhos dos arquivos baixados
    downloaded_files = []
    
    urls = get_urls()

    # URLs específicas para os anexos
    anexos = [
        {
            "url": urls[0],
            "nome": "Anexo_I.pdf"
        },
        {
            "url": urls[1],
            "nome": "Anexo_II.pdf"
        }
    ]
    
    # Baixar cada anexo
    print("Iniciando o download dos anexos...")
    for anexo in anexos:
        file_path = download_pdf(anexo["url"], anexo["nome"], download_dir)
        if file_path:
            downloaded_files.append(file_path)    
    
    
    # Compactar os arquivos se algum foi baixado
    if downloaded_files:
        print("\nArquivos baixados:")
        for file in downloaded_files:
            print(f"- {file}")
        
        # Compactar em 
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        zip_filename = os.path.join(download_dir, f"anexos_ans_{timestamp}.zip")
        compress_files_zip(downloaded_files, zip_filename)
        print(f"\nTodos os anexos foram compactados com sucesso em: {zip_filename}")
    else:
        print("Nenhum arquivo foi baixado. Verifique se os URLs estão corretos ou se o site mudou.")

def download_pdf(url, filename, download_dir):
    """Função para baixar um arquivo PDF usando requests"""
    print(f"Baixando {filename}... de url{url}")
    try:
        response = requests.get(url, stream=True, timeout=30)
        if response.status_code == 200:
            filepath = os.path.join(download_dir, filename)
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"✓ {filename} baixado com sucesso!")
            return filepath
        else:
            print(f"✗ Erro ao baixar {filename}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"✗ Erro ao baixar {filename}: {str(e)}")
        return None

def compress_files_zip(files, output_filename):
    """Função para compactar arquivos em ZIP"""
    print(f"\nCompactando arquivos em {output_filename}...")
    try:
        with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in files:
                zipf.write(file, os.path.basename(file))
        return True
    except Exception as e:
        print(f"Erro ao compactar arquivos: {str(e)}")
        return False
    
def get_urls():
    """
    Função para extrair as URLs dos Anexos I e II de um HTML fornecido.
            
    Returns:
        dict: Um dicionário com as URLs dos Anexos I e II.
    """
    url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança uma exceção para status de erro
        soup = BeautifulSoup(response.content, 'html.parser') # Cria um objeto BeautifulSoup
        
        anexos = soup.find_all('a', href=True)
        urls = []
        for anexo in anexos:
            if "Anexo_I" in anexo['href'] or "Anexo_II" in anexo['href']:
                if "pdf" in anexo['href']:#Exclui os links que não são pdf
                    urls.append(anexo['href'])
        return urls

    except Exception as e:
        print(f"✗ Erro ao extrair URLs: {str(e)}")

if __name__ == "__main__":
    main()