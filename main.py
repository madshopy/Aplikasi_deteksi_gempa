"""
aplikasi deteksi gempa
modularisasi dengan fungction

modularisasi adalah kerangka berpikir dalam memecahkan program
yang kompleks menjadi bagian" kecil yang bisa dikembangkan
"""

"""

27 November 2024, 18:59:36 WIB
2.6
10 km
2.50 LS - 140.55 BT
Pusat gempa berada di darat 17 km barat laut Kota Jayapura
Dirasakan (Skala MMI): II-III Kab. Jayapura
"""


def exstrasi_data(): #data akan disimpan pada reprpsitory pypi
    hasil = dict()
    hasil['tanggal'] = '27 November 2024 '
    hasil['waktu'] = '18:59:36 WIB'
    hasil['magnitudo'] = '2.6'
    hasil['kedalaman'] = '10 km'
    hasil['lokasi'] = {'ls' : 2.50, 'bt' : 140.55 }
    hasil['pusat'] = 'Pusat gempa berada di darat 17 km barat laut Kota Jayapura'
    hasil['dirasakan'] = 'II-III Kab. Jayapura'

    return(hasil)


def tampilkan_data(result):
    print("Gempa Terakhir berdasarkan BMKG")
    print(f"Tanggal = {result['tanggal']}")
    print(f"Waktu = {result['waktu']}")
    print(f"Magnitudo = {result['magnitudo']}")
    print(f"kedalaman = {result['kedalaman']}")
    print(f"lokasi : LS = {result['lokasi'] ['ls']}, BT = {result['lokasi']['bt']}")
    print(f"pusat = {result['pusat']}")
    print(f"Dirasakan = {result['dirasakan']}")



if __name__ == '__main__':
    print("Aplikasi Utama")
    result = exstrasi_data()
    tampilkan_data(result)