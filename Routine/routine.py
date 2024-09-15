import random

def print_schedule(day, full_day_name):
    schedules = {
        "monday": '''
0500 - Math
0600 - Math
0700 - SCHOOL & READ BOOK
1800 - Geography
1900 - Physics
2000 - PHY//MATH//GEO
2100 - Hobby
        ''',
        "tuesday": '''
0500 - Math
0600 - Math
0700 - SCHOOL & READ BOOK
1800 - Geography
1900 - Physics
2000 - PHY//MATH//GEO
2100 - Hobby
        ''',
        "wednesday": '''
0500 - Math
0600 - Math
0700 - SCHOOL & READ BOOK
1800 - Geography
1900 - Physics
2000 - PHY//MATH//GEO
2100 - Hobby
        ''',
        "thursday": '''
0500 - Math
0600 - Math
0700 - SCHOOL & READ BOOK
1800 - Geography
1900 - Physics
2000 - PHY//MATH//GEO
2100 - Hobby
        ''',
        "friday": '''
0500 - Math
0600 - Math
0700 - SCHOOL & READ BOOK
1800 - Geography
1900 - Physics
2000 - PHY//MATH//GEO
2100 - Hobby
        ''',
        "saturday": '''
0600 - Math
0700 - Math
0800 - Math
0900 - Math
1000 - Getting ready
1100 - Taekwondo
1200 - Taekwondo
1300 - HOME
1400 - Physics
1500 - Physics
1600 - Geography
1700 - Math
1800 - Geography
1900 - Physics
2000 - PHY//MATH//GEO
2100 - Hobby
        ''',
        "sunday": '''
0600 - Math
0700 - Math
0800 - Math
0900 - Math
1000 - Physics
1100 - Physics
1200 - Geography
1300 - Geography
1400 - Physics
1500 - Physics
1600 - Geography
1700 - Math
1800 - Geography
1900 - Physics
2000 - PHY//MATH//GEO
2100 - Hobby
        '''
    }
    
    if day in schedules:
        print(f"\n{full_day_name} ---")
        print(schedules[day])
    else:
        print("Sorry, I don't have a schedule for that day.")

def dayFinder():
    shorthand_to_full = {
        "m": ("monday", "Monday"),
        "t": ("tuesday", "Tuesday"),
        "w": ("wednesday", "Wednesday"),
        "th": ("thursday", "Thursday"),
        "f": ("friday", "Friday"),
        "sa": ("saturday", "Saturday"),
        "su": ("sunday", "Sunday")
    }

    while True:
        day = input("\nEnter the day of the week (or 'go back' to return to the main menu): ").strip().lower()
        if day == "go back":
            return
        elif day in shorthand_to_full:
            full_day, full_day_name = shorthand_to_full[day]
            print_schedule(full_day, full_day_name)
        elif day in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
            full_day_name = day.capitalize()
            print_schedule(day, full_day_name)
        else:
            print("Sorry, you misspelled the day. Please try again.")

def freeActivity():
    hobbies = ["Hobby1", "Hobby2", "Hobby3", "Hobby4"]
    while True:
        choice = input("\nWrite \"choose\" to choose a hobby (or 'go back' to return to the main menu): ").strip().lower()
        if choice == "go back":
            return
        elif choice == "choose":
            selected_hobby = random.choice(hobbies)
            print(f"\nYou can try {selected_hobby}.")
        else:
            print("Invalid hobby choice. Please try again.")

def main_menu():
    while True:
        task = input("\nWhat would you like to do? (options: routine, free, exit): ").strip().lower()
        if task == "routine":
            dayFinder()
        elif task == "free":
            freeActivity()
        elif task == "exit":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please type 'routine', 'free', or 'exit'.")


main_menu()
