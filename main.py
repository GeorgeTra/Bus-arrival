
import requests
bus_stop_id = input("Bus stop: ")  # 18141
print()
url = f'https://sg-bus-arrival.haris-samingan.repl.co/?id={bus_stop_id}'
data = requests.get(url)
data_dictionary = data.json()
print(data_dictionary)
print()

bus_services = data_dictionary['services']
print(bus_services)
print()

buses_numbers = []
for each_bus in bus_services:
    buses_numbers.append(each_bus['bus_no'])
print(f"Buses numbers: {buses_numbers}")
print()

chosen_bus = input("Bus number: ")
bus_index = buses_numbers.index(chosen_bus)

chosen_bus_timing = bus_services[bus_index]['next_bus_mins']
if chosen_bus_timing > 0:
    print(f"Bus {chosen_bus} is arriving in {chosen_bus_timing} mins")
else:
    print(f"Bus {chosen_bus} has arrived")






