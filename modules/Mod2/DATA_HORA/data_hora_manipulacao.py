from datetime import datetime, date, timedelta



tipo_carro = str(input("Digite o tipo do carro em P, M, G: "))
tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 60
data_atual = datetime.now()

if tipo_carro == 'P':
    data_estimada = data_atual + timedelta(minutes=tempo_pequeno)
elif tipo_carro == 'M':
    data_estimada = data_atual + timedelta(minutes=tempo_medio)
elif tipo_carro == 'G':
    data_estimada = data_atual + timedelta(minutes= tempo_grande)
print(f"O carro chegou {data_atual} e ficara pronta as {data_estimada}")
print(data_atual.time())
print(data_atual.date())