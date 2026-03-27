def main():
    camel = input("camelCase: ")
    print(to_snake(camel))


def to_snake(camel):
    snake = ""
    for char in camel:
        if char.isupper():
            # თუ დიდი ასოა, ვამატებთ "_" და პატარა ასოს
            snake += "_" + char.lower()
        else:
            snake += char
    return snake


if __name__ == "__main__":
    main()