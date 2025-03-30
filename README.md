# Downloade Automático de Anexos da ANS 

## Descrição

Este script Python Baixa automaticamente os Anexos I e II do Rol de Procedimentos da ANS (Agência Nacional de Saúde Suplementar) e os compacta em um único arquivo ZIP.

## Funcionalidades

- Extrai automaticamente os links mais recentes dos anexos do site oficial da ANS
- Baixa os arquivos PDF dos Anexos I e II
- Organiza os downloads em uma pasta específica
- Compacta os PDFs em um único arquivo ZIP com data e hora
- Fornece feedback detalhado durante todo o processo

## Pré-requisitos

- Python 3.x
- Bibliotecas necessárias:
  - requests
  - zipfile
  - os
  - datetime
  - bs4 (BeautifulSoup)

## Instalação

1. Clone o repositório ou baixe o arquivo do script:
2. Instale as bibliotecas necessárias:
   ```bash
   pip install requests beautifulsoup4
   ```

## Uso

1. Criar uma pasta "downloads" (se não existir)
2. Acessar o site da ANS para encontrar os links mais recentes dos anexos
3. Baixar os PDFs dos Anexos I e II
4. Salvar os arquivos na pasta de downloads
5. Compactar os PDFs em um arquivo ZIP com timestamp
6. Exibir o progresso e o resultado no terminal




