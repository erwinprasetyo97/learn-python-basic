def jumlahkan(*list_angka):
    total = 0
    for angka in list_angka:
        total = total + angka
    return (list_angka,total)

list_angka, total = jumlahkan(10,10,10,10)\

#mengambil data total
print(f" Total dari {list_angka} = {total}")