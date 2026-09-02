# Conteúdo do arquivo main.py
import sys

# Adiciona o caminho correto usando o 'r' para evitar erros de sintaxe nas barras
sys.path.append('C:/Users/pesso/OneDrive/Desktop/Conexão/modulo02')

# Importa a variável do módulo
from dados import nome # pyright: ignore[reportMissingImports]

print(f"[MAIN] O nome importado é: {nome}")





