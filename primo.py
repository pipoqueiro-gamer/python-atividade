primo:int=0
par=0
for c in range (1,1001):
    if c%2==0:
        par+=1
        print(f"{c} par")
        
    else:
        print(f"{c}impar")

    if c%c==0 and c%1==0:
        primo+=1
        print(f"{c} primo")
        print(f"primos = {primo}")
    else:
        print(f"{c}não primo")


