# APP Deportiva de Matrículas
from IPython.display import display, HTML  
from pathlib import Path  

def register_athlete(list):
    name = input("Insert the name of the athlete: ")
    age = int(input("Insert the age of the athlete: "))
    sport = input("Insert the sport of the athlete: ")
    fee = float(input("Insert the mensal fee of the athlete: "))
    athlete = {
        "name": name,
        "age": age,
        "sport": sport,
        "fee": fee
    }
    list.append(athlete)
    print("✅ athlete successfully registered.\n")

def show_athlete(list):
    if not list:
        print("There is no athlete registered yet.\n")
    else:
        print("\n--- ATHLETES LIST ---")
        for d in list:
            print(f"Name: {d['name']}, Age: {d['age']}, Sport: {d['sport']}, Fee: €{d['fee']:.2f}")
        print()

def calculate_total(list):
    total = sum(d["fee"] for d in list)
    print(f"💶 Total profit: €{total:.2f}\n")

def sportive_app():
    athlete_list = []
    while True:
        print("===== SPORTS REGISTRATION APP =====")
        print("1. Register athlete ")
        print("2. Show athlete list")
        print("3. Calculate total profit")
        print("4. Exit")
        option = input("Select one option: ")

        if option == "1":
            register_athlete(athlete_list)
        elif option == "2":
            show_athlete(athlete_list)
        elif option == "3":
            calculate_total(athlete_list)
        elif option == "4":
            print("👋 Thanks for using the app.")
            break
        else:
            print("Invalid option, try again.\n")

sportive_app()

template_path = Path(__file__).parent / "index.html"
with open(template_path, "r", encoding="utf-8") as f:
    template = f.read()


output_html = template.format(
   age = age , 
   name=name,
   sport=sport,
   fee=fee,
   total=total, 
   athlete=athlete,
   list=list,
   athlete_list=athlete_list,
)

display(HTML(output_html))
