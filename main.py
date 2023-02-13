# En este ejercicio, tendréis que crear un archivo py donde creéis un archivo txt, lo abráis y escribáis dentro del archivo. Para ello, tendréis que acceder dos veces al archivo creado.

f = open('fichero.txt','a')
nombreSinCorregir = input('Ingrese su nombre por favor: ')
nombre = nombreSinCorregir.capitalize()
apellidoSinCorregir= input ('Ingrese su apellido por favor: ')
apellido = apellidoSinCorregir.capitalize()
print(f'Bienvenido {nombre} {apellido}')

listaClientes = [
    f"{nombre} ",
    f'{apellido}\n'
]
f.writelines(listaClientes)

f.close()