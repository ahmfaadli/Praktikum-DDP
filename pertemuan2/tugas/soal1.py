# Program ini akan mencetak angka dari 100 hinga 1 dengan kelipatan 2, yaitu 100, 95, 96, dst
# Perintah for akan mengiterasi variabel i dengan nilai-nilai yang telah di tentukan oleh fungsi fungsi()
# Fungsi range() akan melibatkan sebuah objek yang menyimpan urutan angka dari 100 hingga 1. dengan kelipatan 2 (karena ada argumen ketiga yaitu -2)
# Setiap iterasi, printah print() akan mencetak nilai dari i, diikuti oleh karakter koma dan sepasi (karena ada argumen end=", ")
# Setelah semua itersi selesai, program dan looping akan berakhir

for i in range(100, 1, -2):
    print(i, end=", ")