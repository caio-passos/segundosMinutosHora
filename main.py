segundos = int(input('favor, entre com o número de segundos que deseja converter:\n'))
minutos = 0
horas = 0
dias = 0
if segundos >= 60:
    minutos = segundos // 60
    segundos %= 60
if minutos >= 60:
    horas = minutos // 60
    minutos %= 60
if horas > 23:
    dias = horas // 24
    horas %= 24

print(dias, 'dias, ', horas, 'horas, ', minutos, 'minutos e ', segundos, 'segundos')
