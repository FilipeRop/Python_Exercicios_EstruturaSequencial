#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
#

lado = float(input('Digite o tamanho do lado de um quadrado => '))

area = pow(lado,2)
dobro = area * 2

print(f'Área do quadrado => : {area}')
print(f'O dobro da área do quadrado => {dobro}')