from random_word import RandomWords


def hangman():

    r = RandomWords()
    wor = r.get_random_word()
    word = list(wor)
    word1 = wor
    guess = len(word)
    segment1 = list(len(word) * "_")
    length = len(word)

    while 0 <= guess <= len(word1) + 1:
        segment3 = []
        print(f'You have {guess} chances left! ')

        ui = list(input(f'Guess the letter it is a {len(word)} letters word. Only {length} letters limited : '))
        if len(ui) <= length:

            for item in ui:
                if item in list(word):
                    length -= 1

                    value = word.index(item)
                    segment1[value] = item

                    word.pop(value)
                    word.insert(value, "_")

        else:
            print(f"Not allowed {len(ui)} letters!")

        if not 0 <= guess <= len(word1) + 1:
            break

        if length == 0:
            break

        for item in segment1:
            segment3.append(item)
        segment2 = ''

        for i in segment3:
            segment2 += i

        print(segment2)
        guess -= 1

    if length == 0:
        print('You nailed it!')
        print(str(wor))

    else:
        print("Sorry, you failed it!")
        print(str(wor))


hangman()
