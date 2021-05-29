import math

def giai_pt_bac_nhat(a, b):
   if a == 0:
       if b == 0:
           return "Phuong trinh co vo so nghiem"
       return "Phuong trinh vo nghiem"
   return "Phuong trinh co mot nghiem duy nhat: \nx = {}".format(-b / a)

def giai_pt_bac_hai(a, b, c):
   if a == 0:
       return giai_pt_bac_nhat(b, c)
   delta = b * b - 4 * a * c
   if delta > 0:
       x1 = float((-b + math.sqrt(delta)) / (2 * a))
       x2 = float((-b - math.sqrt(delta)) / (2 * a))
       return "Phuong trinh co hai nghiem phan biet la: \nx1 = {} \nx2 = {}".format(x1, x2)
   if delta == 0:
       x = -b / (2 * a)
       return "Phuong trinh co nghiem kep: \nx1 = x2 = {}".format(x)
   return "Phuong trinh vo nghiem"

try:
   #Nhap bac cua phuong trinh
   Bac = input('Nhap bac cua phuong trinh: ')
  
   #TH 1: Giai phuong trinh bac nhat
   if Bac == '1':
       #Doc dong du lieu thu hai
       #Ep kieu du lieu sang so thuc
       a, b = map(float, input().split())
       #Goi ham giai phuong trinh bac nhat
       print(giai_pt_bac_nhat(a, b))
   #TH 2: Giai phuong trinh bac hai
   elif Bac == '2':
       a, b, c = map(float, input().split())
       print(giai_pt_bac_hai(a, b, c))
   else:
       print("Vui long chon lai bac la 1 hoac 2")
except:
   print("Dinh dang dau vao khong hop le!")
