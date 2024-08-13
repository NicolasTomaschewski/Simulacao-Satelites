import math

velocidade_inicial = float(input('Insira a velocidade inicial do veículo (em m/s): '))
orbita_inicial = float(input('Insira o raio da órbita inicial (em metros): '))
tempo_inicial = float(input('Insira o tempo necessário para o satélite completar uma volta completa ao redor da Terra (em segundos): '))
orbita_final = float(input('Insira o raio da órbita final (em metros): '))

print('O primeiro passo da manobra de Hohmann é dar um impulso ao veículo para que exista uma variação de velocidade')

modulo1 = math.sqrt((2 * (orbita_final / orbita_inicial)) / ((orbita_final / orbita_inicial) + 1)) - 1
deltav1 = velocidade_inicial * modulo1

print('Para que a manobra seja realizada com sucesso, o primeiro impulso dado ao veículo deve ser forte o suficiente para criar uma variação na velocidade de: {:.2f} m/s'.format(deltav1))

print('No momento em que o satélite se encontrar na metade da nova órbita, um segundo impulso deve ser dado, criando uma nova variação de velocidade.')

modulo2 = 1 - math.sqrt(2 / ((orbita_final / orbita_inicial) + 1))
deltav2 = velocidade_inicial * modulo2 * math.sqrt(orbita_inicial / orbita_final)

print('O valor dessa nova variação na velocidade deve ser igual a {:.2f} m/s'.format(deltav2))

print('Este segundo impulso faz com que o satélite atinja a órbita de destino.')
print('Também é possível determinar o tempo necessário para realizar a manobra em função do período da órbita inicial.')

tempo_total = 0.5 * ((1 + orbita_final / orbita_inicial) / 2) ** (3 / 2) * tempo_inicial

print('O tempo necessário para a realização dessa manobra de Hohmann é {:.2f} segundos.'.format(tempo_total))
