temperature = float(input("Enter todays temperature in centegrade : "))

if temperature <= 10:
    print("Its very cold..")
elif temperature > 10 and temperature <= 25:
    print("Weather is pleasant outside")
elif temperature > 25 and temperature < 35:
    print("Its warm outside...")
elif temperature >= 35:
    print("Its hot")
else:
    print("Its burning outside")