"""
aplikasi deteksi gempa
modularisasi dengan fungction
modularisasi dengan package

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



import gempaterkini
if __name__ == '__main__':
    print("Aplikasi Utama")
    result = gempaterkini.exstrasi_data()
    gempaterkini.tampilkan_data(result)