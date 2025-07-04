#calculando a idade de uma pessoa
from datetime import date

d = int(input("Dia de nascimento: "))
m = int(input("Mês de nascimento: "))
a = int(input("Ano de nascimento: "))

hoje = date.today()
idade = hoje.year - a
if (hoje.month, hoje.day) < (m, d):
    idade -= 1

if idade > 50:
    print("Você está quase aposentado!")
else:
    print(f"Você tem {idade} anos." if idade >= 0 else "Data de nascimento no futuro!")
