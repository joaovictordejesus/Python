# Mostra a data e horário atuais e formata

import datetime

data_hora_atual = datetime.datetime.now()

data_formatada = data_hora_atual.strftime("Data: %d/%m/%Y")
hora_formatada = data_hora_atual.strftime("Hora: %H:%M")

print(data_formatada)
print(hora_formatada)
