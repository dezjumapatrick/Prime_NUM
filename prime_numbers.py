n =int(input("Find Prime Numbers Upto What Number? : "))
PrimeList =[]

for x in range (0, n +1):
	isPrime= True
	for y in range(0, int(x ** 0.5)+1):
		if x % y == 0:
			isPrime= False
			break

			if isPrime
			PrimeList.append(x)