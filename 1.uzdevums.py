sskaitlis = int(input("Ievadiet skaitli: "))
# Sākam skaitīt no 1
summa = 0
# For cikls, lai saskaitītu skaitļus no 1 līdz ievadītajam skaitlim
for skaitlis in range(1, sskaitlis + 1):
    summa += skaitlis
# Izdrukājam rezultātu
print(f"Summa no 1 līdz {sskaitlis} ir: {summa}")
