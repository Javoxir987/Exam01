def year(birth_year, current_year):
    age = current_year - birth_year
    return age

def main():
    birth_year = int(input("sizni yoshingiz: "))
    age = year(birth_year, 2026)
    print(age)
main()