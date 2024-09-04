import os
import subprocess
from datetime import datetime

# Configurar banco de dados
db_host = "localhost"
db_user = "root"
db_password = ""
db_database = ""

# Caminho da pasta onde o arquivo .sql vai ser salvo
diretorio = "local onde o arquivo sera salvo"
# Caso o diretório não exista, o código abaixo cria a pasta
if not os.path.exists(diretorio):
    os.makedirs(diretorio)

# Nome do arquivo de backup
dia_hora = datetime.now().strftime("%Y%m%d%H%M%S")
backup = os.path.join(diretorio, f"{db_database}_backup_{dia_hora}.sql")

# Substitua o caminho abaixo pelo caminho completo do mysqldump no seu sistema
mysqldump_path = r"C:/wamp64/bin/mysql/mysql8.3.0/bin/mysqldump.exe"

# Comando para exportar o banco de dados
dump_command = f"{mysqldump_path} --host={db_host} --user={db_user} --password={db_password} {db_database} > {backup}"


#Execução do comando de backup
subprocess.run(dump_command, shell=True, check=True)
print(f"Backup do banco de dados {db_database} realizado!")

