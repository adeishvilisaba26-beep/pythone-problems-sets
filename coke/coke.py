def main():
    amount_due = 50
    inserted = 0

    while inserted < amount_due:
        print(f"Amount Due: {amount_due - inserted}")
        coin = int(input("Insert coin: "))

        if coin in [25, 10, 5]:
            inserted += coin
        else:
           
            continue

    change = inserted - amount_due
    print(f"Change Owed: {change}")


if __name__ == "__main__":
    main()