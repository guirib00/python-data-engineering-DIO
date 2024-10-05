from datetime import datetime, timezone, timedelta
import pytz

data = datetime.now(pytz.timezone("Europe/Oslo"))
data2 = datetime.now(pytz.timezone("America/Sao_Paulo"))

print(data)
print(data2)

data3 = datetime.now(timezone(timedelta(hours=-3), "BRT"))
print(data3)

data_utc = data3.astimezone(timezone.utc)
print(data_utc)