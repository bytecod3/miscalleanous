
houses = ['Erics', 'kyles', 'edwins', 'stans']


def deliver_presents(houses):
    if len(houses) == 1:
        house = houses[0]
        print("Delivering presents to ", house)

    # manager elf doing his work
    else:
        mid = len(houses) // 2
        first_half = houses[:mid]
        second_half = houses[mid:]

        # divides his work among two elves
        deliver_presents(first_half)
        deliver_presents(second_half)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    deliver_presents(houses)


