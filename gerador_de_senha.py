from random import choice
import string

tamanho_da_senha = int(input("Quantos digitos você quer na senha? ") )
caracteres = string.ascii_letters + string.digits + string.punctuation
senha_segura = ''

for i in range(tamanho_da_senha):
    senha_segura+= choice(caracteres)
    
print("A senha gerada foi: ", senha_segura)