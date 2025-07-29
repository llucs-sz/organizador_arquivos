📚 Anotação Completa do Projeto: Organizador Automático de Arquivos
1. Objetivo do projeto
Criar um script Python que organiza automaticamente os arquivos da pasta Downloads, movendo-os para pastas específicas com base na extensão do arquivo (ex: imagens, documentos, executáveis).

2. Conceitos e tópicos abordados
a) Biblioteca os
Biblioteca padrão do Python para interagir com o sistema operacional.

Permite navegar por pastas, listar arquivos, verificar tipos e manipular caminhos.

b) Biblioteca shutil
Também padrão, usada para operações com arquivos, como copiar e mover.

c) Função os.listdir()
Lista todos os arquivos e pastas dentro de um diretório.

d) Função os.path.splitext()
Separa o nome do arquivo da sua extensão (ex: "foto.jpg" → "foto", ".jpg").

e) Verificação de arquivo com os.path.isfile()
Confirma se o item listado é um arquivo e não uma pasta.

f) Criar pasta com os.makedirs()
Cria uma pasta, caso ela ainda não exista, evitando erros.

g) Estruturas de controle (loops, condicionais)
Para iterar sobre arquivos e aplicar regras de organização.

3. Importância dos códigos e funções
Automatização: Elimina o trabalho manual de organizar arquivos, economizando tempo e esforço.

Reutilização: Código pode ser adaptado para outras pastas ou tipos de arquivos.

Lógica de programação: Uso de listas, dicionários, funções e módulos padrão reforça conceitos fundamentais.

Boas práticas: Criação de pastas se não existirem, tratamento de erros simples.

4. Como o código funciona, passo a passo
Define o caminho da pasta Downloads
Com os.path.expanduser("~/Downloads") para pegar a pasta correta no sistema do usuário.

Define categorias e extensões
Um dicionário (pastas_destino) onde a chave é o nome da pasta e o valor é uma lista de extensões correspondentes.

Função mover_arquivo()
Recebe o nome do arquivo, pega sua extensão, verifica onde ele deve ir, cria a pasta se necessário, e move o arquivo para lá.

Percorre todos os arquivos na pasta Downloads
Para cada arquivo, verifica se é realmente um arquivo (não uma pasta) e chama mover_arquivo().

5. O que você aprendeu como dev
A importância de planejar o que o programa deve fazer antes de codar

Como manipular arquivos e pastas no sistema operacional via Python

Como usar estruturas de dados para organizar regras (dicionários e listas)

A importância de validar dados (checar se é arquivo e se a pasta existe)

Como criar funções para deixar o código mais organizado e reutilizável

Como testar pequenos trechos de código e ir evoluindo até o sistema completo