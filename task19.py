text = "Salom Dunyo"
unlilar = "aeiou"
soni = 0

for harf in text.lower():
    if harf in unlilar:
        soni += 1

print(soni)