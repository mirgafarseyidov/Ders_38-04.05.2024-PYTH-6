# 1
# def kvadratlar(liste):
#     kvadratlar_listesi = []
#     for num in liste:
#         if num >= 0 and num*0.5 == int(num*0.5):  
#             kvadratlar_listesi.append(num)
#     return kvadratlar_listesi

# def kvadratlarin_listesi(liste):
#     kvadratlar_listesi = kvadratlar(liste)
#     return [int(x**0.5) for x in kvadratlar_listesi]

# mylist = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# kvadratlar_listesi = kvadratlar(mylist)
# kvadratlarin_yeni_listesi = kvadratlarin_listesi(mylist)

# print("Listdəki ədədlərin kvadrat kökləri:")
# print(kvadratlarin_yeni_listesi)




# 2
# def tekrarlanmayan_list(liste):
#     tekrarlanmayanlar = []
#     for eleman in liste:
#         if liste.count(eleman) == 1:
#             tekrarlanmayanlar.append(eleman)
#     return tekrarlanmayanlar

# liste =[-1,1,2,2,6,7,7,'say']

# print(tekrarlanmayan_list(liste))
#3
# def raqamlari_vur(input_str):
#     vurma = 1
#     for char in input_str:
#         if char.isdigit():
#             vurma *= int(char)
#     return vurma

# input_str = input("Bir eded daxil: ") 
# print("Rəqəmlərin hasil edilməsi:", raqamlari_vur(input_str))
 #4
# eded=int(input("Eded daxil edin : "))
# print(list(i for i in range(1,eded) if eded % i==0))
# 5

# months=["Yanvar","Fevral","Mart","Aprel","May","Iyun","Iyul","Avqust","Sentyabr","Oktyabr","Noyabr","Dekabr"]
# print(dict((i, len(i)) for i in months))

# 6
# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith","Elvin Abi]
# print(list(i.split().lower() for i in names))
# 7
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]

# ortalama = [(nums1[i] + nums2[i]) / 2 for i in range(len(nums1))]
# print(ortalama)