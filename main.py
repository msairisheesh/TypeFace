import soundex

def main():
    print("-----------------")
    print("| codedrome.com |")
    print("| Soundex       |")
    print("-----------------\n")

    names1 = ["Mayhul", "Murthy"]

    names2 = ["Mehul", "Moorthi"]

    namecount = len(names1)

    for i in range(0, len(names1)):

        s1 = soundex.soundex(names1[i])
        s2 = soundex.soundex(names2[i])

        print("{:20s}{:4s}  {:20s}{:4s}".format(names1[i], s1, names2[i], s2))

main()
