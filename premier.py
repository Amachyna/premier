from utils import estPremier

n = int(input("Entrer un nombre: "))

if estPremier(n):
    print(n, "est premier")
else:     
    print(n, "n'est pas premier")
