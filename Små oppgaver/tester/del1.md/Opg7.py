MVA_SATS = 0.25

pris = float(input("Hvor mye koster produktet? "))
pris = pris * (1 + MVA_SATS)

print(f"produktet koster {pris:.2f}kr inkludert mva")