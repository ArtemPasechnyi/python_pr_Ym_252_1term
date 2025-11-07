def main() -> None:
    text = input("Введите текст: ")
    word = input("Введите слово для поиска: ")

    words = text.split()
    occurrences = words.count(word)
    print(f"Слово '{word}' встречается {occurrences} раз(а).")


if __name__ == "__main__":
    main()

