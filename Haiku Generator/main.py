from ai import call_gpt

def main():
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    print("Creating your haiku....")

    create_haiku = call_gpt(f"Create haiku with name {name} and topic {topic}")
    print(create_haiku)


if __name__ == "__main__":
    main()