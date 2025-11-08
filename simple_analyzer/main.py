def read_config():
	config_values = {}
	with open("../config/config.txt", "r") as file:
		for line in file:
			key, value = line.split("=", 1)
			config_values[key] = int(value)
	return config_values

config = read_config()
interval = config.get("interval")
sequence_length = config.get("sequence_length")
print(f"interval = {interval}")
print(f"sequence_length = {sequence_length}")
