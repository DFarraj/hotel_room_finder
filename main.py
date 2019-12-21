hotel_file = open("./hotelrooms.csv", "r")
hotel_data = hotel_file.readlines()
for i in range(len(hotel_data)):
    if i == 0:
        continue
    print(hotel_data[i])

hotel_file.close()