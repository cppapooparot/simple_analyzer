from analyzer import Analyzer
import random
import time

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

analyzer = Analyzer()
a = 1

while True:
	num = random.randint(1, 100)
	analyzer.add_number(num)
	
	if len(analyzer.numbers) > sequence_length:
			analyzer.numbers.pop(0)
	print("Numbers:", analyzer.numbers)
	print("Even count:", analyzer.even_count())
	print("Odd count:", analyzer.odd_count())
	print("Highest number:", analyzer.highest_number())
	print("Increasing pairs:", analyzer.increasing_pairs())
	print("-" * 40)

	current_seconds = time.localtime().tm_sec
	if len(analyzer.numbers) == sequence_length and current_seconds == 0:
		print("Stopping the loop.")
		break
	time.sleep(interval)
