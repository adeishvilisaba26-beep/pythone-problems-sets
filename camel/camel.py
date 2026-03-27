def main():
    camel = input("camelCase: ")
    print(to_snake(camel))


def to_snake(camel):
    snake = ""
    for char in camel:
        if char.isupper():
           
            snake += "_" + char.lower()
        else:
            snake += char
    return snake


if __name__ == "__main__":
    main()