# Opret en liste, kaldet t, med tallene 0 til og med 10
t = list(range(11))  

# Find ud af hvilket indeks tallet 3 har i t
index_of_3 = t.index(3)
print(f"Indeks af tallet 3: {index_of_3}")

# Erstat det første element i t med "zero"
t[0] = "zero"
print(f"Liste efter erstatning af første element: {t}")

# Udtræk følgende fra t med list slicing:
# De første 3 elementer
first_3_elements = t[:3]
print(f"De første 3 elementer: {first_3_elements}")

# Det 3., 4. og 5. element
third_to_fifth_elements = t[2:5]
print(f"Det 3., 4. og 5. element: {third_to_fifth_elements}")

# De sidste 3 elementer
last_3_elements = t[-3:]
print(f"De sidste 3 elementer: {last_3_elements}")

# Kontroller om tallet 10 virkelig er indeholdt i t ved brug af in-operatoren
contains_10 = 10 in t
print(f"Indeholder t tallet 10? {contains_10}")

# Find længden af t
length_of_t = len(t)
print(f"Længden af t: {length_of_t}")

# Print hvert element af t på en ny linje (hint: brug et for-loop)
print("Hvert element i t på en ny linje:")
for element in t:
    print(element)
