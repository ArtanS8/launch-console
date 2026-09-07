def show_about_me(name):
    print(f"Hi my name is {name} and I am a senior at JPS high school. I love to play sports for pleasure. In my free time, I like creating apps from ideas I had during the week.")


def show_my_goals():
    print("My goals are to be successful in life. To do that I want to create "
          "products that benefit others and make this world a much better place.")


def show_fun_fact():
    print("Fun fact: I'm left-handed! Only about 15% of people in the world are left-handed.")


def main():
    print("Welcome to the Launch Console!")
    name = input("What's your name? ")
    print(f"Great to meet you, {name}!")

    while True:
        print("\nMenu:")
        print("1. About me")
        print("2. My goals")
        print("3. Fun fact")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_about_me(name)
        elif choice == "2":
            show_my_goals()
        elif choice == "3":
            show_fun_fact()
        elif choice == "4":
            print(f"Goodbye, {name}! Thanks for stopping by.")
            break
        else:
            print("Invalid option, please choose 1-4.")


if __name__ == "__main__":
    main()
