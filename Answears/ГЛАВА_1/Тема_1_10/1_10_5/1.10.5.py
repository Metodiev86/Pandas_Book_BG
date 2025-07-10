#Напишете код, който чете файл с числа, разделени със запетаи, и изчислява тяхната сума.

sum = 0
with open("file_of_number.txt", "r") as file:
	# Четене на файла ред по ред
	for line in file:
		# Премахваме водещи/задни интервали и разделяме по запетаи
		numbers = line.strip().split(",")

		# Добавяме всяко число към сумата
		for number in numbers:
			sum += float(number)

print(sum)
