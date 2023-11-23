def faktorials(skaitlis):
    if skaitlis < 0:
        return "Faktoriālu nevar aprēķināt negatīvam skaitlim."
    elif skaitlis == 0 or skaitlis == 1:
        return 1
    else:
        rezultats = 1
        for i in range(2, skaitlis + 1):
            rezultats *= i
        return rezultats
sskaitlis = int(input("Ievadiet veselu skaitli!: "))
# Aprēķina faktoriālu un izvada rezultātu
print(f"{sskaitlis} faktoriāls ir: {faktorials(sskaitlis)}")
