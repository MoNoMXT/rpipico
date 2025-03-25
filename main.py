# Germán Andrés Xander 2024

d = dht.DHT11(machine.Pin(13))
d.measure()
temperatura=d.temperature()
print(f"\nla temperatura actual es de {temperatura} C")
humedad=d.humidity()
print(f"la humedad actual es de {humedad} %")