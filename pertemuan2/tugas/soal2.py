# program ini akan menghitung rata - rata sejumlah angka yang di imput oleh pengguna
# Pertama. perintah input() akan meminta pengguna untuk memasukan sebuah nilai, yang kemudian di simpandi dalam variabel inp
# Variabel inp akan di konversi menjadi tipe integer dengan menggunakan fungsi int()
# Selanjutnya, variabel total diinisialisasi dengan nilai 0, Variabrl ini akan digunakan untuk meyimpan jumlah dari semua angka  yang di input
# Kemudia, perintah for akan memulai looping dengan mengiterasi variabel1 dengan nilai - nilai yang ditentukan oleh fungsi range()
# Fungsi range() akan mengembalikan sebuah objek yang menyimapan urutan  angka dari 0 hinga inp-1
# Setiap iterasi, perintah input() akan meminta pengguna untuk memasukan sebuah angka, yang kemudian disimpan di dalam variabel nilai
# Variabel nilai juga akan di konversi menjadi tipe integer dengan mengunakan fungsi int()
# Selanjutnya, nilaidari nilai akan di tambahkan ke dalam total
# Setelah semua iterasi selesai, looping akan berakhir dan prograam akanmelanjutkan ke perintah selanjutnya
# Kemudian, variabrl ratarata dihitung dengan mengelompokan jumlah dari semua angka yang diinput dengan banyak angka tersebut (inp)
# Terakgir, perintah print() akan mencetak hasil dari ratarata ke layar

inp = int(input("Msukan Banyak angka: "))
total = 0
for i in range(inp):
    nilai = int(input("Masukan angka: "))
    total += nilai

ratarata = total / inp

print("Rata rata = ", ratarata)