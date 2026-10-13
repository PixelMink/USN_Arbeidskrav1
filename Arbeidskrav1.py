
#ARBEIDSKRAV 1 USN 

#For begge biler
km_årlig = 8000
tr_avg = round(8.38 * 365)

#Forsikring
forsikring_bensin = 7500
forsikring_el = 5000

dif_forsikring = forsikring_bensin - forsikring_el

#Drivstoff

kr_km_bensin = 1
drivstoff_årlig_bensin = km_årlig * kr_km_bensin

kr_kwh = 2.0
kwh_km = 0.2
kr_km_el = kr_kwh * kwh_km
drivstoff_årlig_el = round(km_årlig * kr_km_el)

dif_drivstoff = drivstoff_årlig_bensin - drivstoff_årlig_el

#Bom
bom_km_bensin = 0.3
bom_årlig_bensin = round(km_årlig * bom_km_bensin)

bom_km_el = 0.1
bom_årlig_el = round(km_årlig * bom_km_el)

dif_bom = bom_årlig_bensin - bom_årlig_el


# Sum kostnader
sum_bensin = tr_avg + forsikring_bensin + drivstoff_årlig_bensin + bom_årlig_bensin

sum_el = tr_avg + forsikring_el + drivstoff_årlig_el + bom_årlig_el

dif_sum = sum_bensin - sum_el


#print

print(str("Sammenligne kostnader for bensinbil og elbil:"))
print()
print(str("For begge biler gjelder: "))
print("Årlig kjørelengde:", km_årlig, "km.")
print("Årlig trafikkforsikringsvgift på", tr_avg, "kr.")
print()

print(str("Forskjellene i årlige kostnader vil derfor være knyttet til forsikring, drivstofforbruk og bomavgift, på følgende måte:"))
print()
print(str("Forsikring: "))
print("For bensinbil:", forsikring_bensin, "kr. og for elbil:", forsikring_el,"kr. i året. Differanse:", dif_forsikring,"kr." )
print()
print("Drivstoff, med en årlig kjørelengde på", km_årlig, "km årlig:")
print("For bensinbil:", drivstoff_årlig_bensin, "kr. og for elbil:", drivstoff_årlig_el, "kr i året. Differanse:", dif_drivstoff, "kr.")
print()
print(str("Bomavgift: "))
print("For bensinbil:", bom_årlig_bensin, "kr. og for elbil:", bom_årlig_el,"kr. i året. Differanse:", dif_bom,"kr." )
print()
print()
print("De årlige kostnadene vil følgelig bli", sum_bensin, "kr. for bensinbil og", sum_el, "kr. for elbil. Det vil altså være", dif_sum, "kr. dyrere med en bensinbil.")








