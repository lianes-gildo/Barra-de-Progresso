import time

total = 50

print("\n")

percentagem = 0

for i in range(total +1):
    percentagem = int((i / total) *100)
    barra = "#" * (percentagem // 5)
    espacos = " " * ((100 - percentagem) // 5)
    print(f"\rProgresso: [{barra}{espacos}] {percentagem}%", end=" ")
    time.sleep(0.2)
    
    if percentagem < 100:
        print("Baixando...", end=" ")
    elif percentagem == 100:
        print("Download Finalizado.")
        break
    else:
        print("ERROR.")

    
print("\n")