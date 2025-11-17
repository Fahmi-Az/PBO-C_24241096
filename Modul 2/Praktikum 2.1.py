class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.__saldo = saldo 


akun_budi = RekeningBank("Budi", 1000000)
try :
 print(f"Saldo awal Budi: {akun_budi.__saldo}")
except: 
   print("Error: Tidak bisa mengakses atribut __saldo secara langsung.")



