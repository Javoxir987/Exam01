def ticket(age):
    asl_narx = 100
    
    if 0 <= age <= 7:
        return asl_narx * 0.5, "50%"
    elif 7 <= age <= 17:
        return asl_narx * 0.8, "20%"
    elif age >= 60:
        return asl_narx * 0.7, "30%"
    else:
        return asl_narx, "0%"

age = int(input('age: '))
narx, skidka = ticket(age)

print(f"Yakuniy narx: {int(narx)} so'm ({skidka} chegirma qo'llanildi)")