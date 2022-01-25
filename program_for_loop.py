banyak = int(input("Berapa banyak data ? "))

name = []
age = []

for i in range(0, banyak):
    print(f"Data ke {i}")
    input_name = input("Nama : ")
    input_age = int(input("Umur : "))
    
    name.append(input_age)
    age.append(input_name)

for i in range(0, len(name)):
    data_name = name[i]
    data_age = age[i]
    print(f"{data_name} berumur {data_age} tahun")

# print(name)
# print(age)