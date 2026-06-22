def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }

    correct = 0

    for word in translations:
        answer = input("What is the Spanish translation for " + word + "? ")
        if answer == translations[word]:
            print("That is correct!")
            correct += 1  # increment only on correct answer
        else:
            print("That is incorrect, the Spanish translation for " + word + " is " + translations[word] + ".")
        print()  # blank line between each Q&A

    print("You got " + str(correct) + "/" + str(len(translations)) + " words correct, come study again soon!")

if __name__ == '__main__':
    main()