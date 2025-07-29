import os  # Biblioteca
import shutil  # para mover arquivos

# Caminho da pasta Downloads
pasta_downloads = os.path.expanduser("~/Downloads")

# Pastas de destino (você pode ajustar os nomes)
pastas_destino = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Executaveis": [".exe", ".msi"],
    "Outros": []
}

# Função para mover arquivos
def mover_arquivo(arquivo):
    nome_arquivo, extensao = os.path.splitext(arquivo)
    extensao = extensao.lower()

    # Verifica a qual pasta o arquivo pertence
    for pasta, ext_list in pastas_destino.items():
        if extensao in ext_list:
            destino = os.path.join(pasta_downloads, pasta)
            # Cria a pasta se não existir
            if not os.path.exists(destino):
                os.makedirs(destino)
            # Caminho completo de origem e destino
            origem = os.path.join(pasta_downloads, arquivo)
            destino_arquivo = os.path.join(destino, arquivo)
            # Move o arquivo
            shutil.move(origem, destino_arquivo)
            print(f"Movido {arquivo} para {pasta}")
            return

    # Se a extensão não estiver nas listas, vai para 'Outros'
    destino = os.path.join(pasta_downloads, "Outros")
    if not os.path.exists(destino):
        os.makedirs(destino)
    origem = os.path.join(pasta_downloads, arquivo)
    destino_arquivo = os.path.join(destino, arquivo)
    shutil.move(origem, destino_arquivo)
    print(f"Movido {arquivo} para Outros")

# Lista arquivos da pasta
arquivos = os.listdir(pasta_downloads)

# Executa a função para cada arquivo
for arquivo in arquivos:
    # Ignora pastas e arquivos ocultos do sistema (ex: desktop.ini)
    if os.path.isfile(os.path.join(pasta_downloads, arquivo)):
        mover_arquivo(arquivo)
