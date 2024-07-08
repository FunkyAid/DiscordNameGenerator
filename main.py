import random
import requests

def generate_name():
    response = requests.get("https://raw.githubusercontent.com/dwyl/english-words/master/words.txt")
    words = response.text.splitlines()
    suffixes = ["son", "man", "ster", "ley", "ton", "sonic", "star", "bolt", "fire", "storm"]
    word1 = random.choice(words)
    word2 = random.choice(words)
    suffix = random.choice(suffixes)
    username = f"{word1}{word2}{suffix}".capitalize()
    return username

def main():
    print("Discord Name Generator By FunkyAid Join VoidCord For More https://discord.gg/kSNetSpH2U")
    print("---------------------")
    print("Options:")
    print("1. Generate a random name")
    print("2. Quit")

    while True:
        choice = input("Enter your choice: ")
        if choice == '1':
            print("Your generated Discord name is:", generate_name())
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
