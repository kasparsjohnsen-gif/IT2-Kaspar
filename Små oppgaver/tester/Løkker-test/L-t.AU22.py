n = 1
print(f"""
            ------------------
            Enkel gange tabell
            ------------------
""")
print("   ",end="")

for k in range(1,11):
  print(f"{k:>4}", end="")
print("")
print("   ________________________________________")

for i in range(1, 11):
  print(f"{n:2}|", end="")
  n += 1
  for j in range(1, 11):
    print(f"{(i * j):4}", end="")
    
  print("")
