from datetime import datetime

data_atual = datetime.now()
print(data_atual.strftime("%d/%m/%Y, %H:%M:%S"))

data_string = "04/10/2024 15:30"
data_atual = datetime.strptime(data_string, "%d/%m/%Y %H:%M")
print(data_atual)