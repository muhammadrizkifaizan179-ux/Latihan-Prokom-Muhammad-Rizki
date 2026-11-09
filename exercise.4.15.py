peliharaan = ['anjing', 'kucing', 'kelinci']
for hewan in peliharaan:
    if hewan == 'anjing':
        print("Anjing adalah hewan peliharaan yang setia.")
    if hewan == 'kucing':
        print("Kucing adalah hewan peliharaan yang lucu.")
    if hewan == 'kelinci':
        print("Kelinci adalah hewan peliharaan yang menggemaskan.")
        
print("\nHewan peliharaan yang saya miliki adalah:")

kubik = [angka ** 3 for angka in range(1, 11)]
print(kubik)
print("tiga bilangan kubik pertama adalah:")
print(kubik[:3])
for angka in kubik[:3]:
    print(angka)
print("tiga bilangan kubik terakhir adalah:")
for angka in kubik[-3:]:
    print(angka)
print("tiga bilangan kubik tengah adalah:")
for angka in kubik[3:6]:
    print(angka)
    
pizza = ["pepperoni", "keju", "jamur", "ayam bbq", "sosis"]
pizza_aan = pizza[:]
pizza.append('cimol')
pizza_aan.append("bawang")

print("topping pizza favoritku adalah:")
for toping in pizza:
    print(toping)
    
print("\ntopping pizza favorit temanku adalah:")
for toping in pizza_aan:
    print(toping)