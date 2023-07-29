from quiz import *

def build():
    q1 = Quiz("Care sunt personajele principale in No Game No Life?", "Shiro & Sora", "Stephanie & Jibril", "Tet & Miko",
              "Shiro & Sora", 10)
    q2 = Quiz("Cati Espada sunt in Bleach?", "10", "7", "1", "10", 10)
    q3 = Quiz("Cum se numeste fratele lui Edward din Fullmetal Alchemist? ", "Alphonse", "Roy", "Bradley", "Alphonse", 10)
    q4 = Quiz("Cate cozi are vulpea din interiorul lui Naruto?", "9", "8", "2", "9", 10)

    lista = [q1, q2, q3, q4]
    return lista


def start():
    quiz_list = build()
    punctaj = 0

    for quiz in quiz_list:
        print(quiz.get_intrebare())
        print("a)", quiz.get_r1(), "\nb)", quiz.get_r2(), "\nc)", quiz.get_r3())

        choices = ["a", "b", "c"]
        raspuns = input("Raspuns: ")

        if raspuns in choices:
            if raspuns == quiz.get_r_corect().lower():
                print("Raspuns corect!")
                punctaj += quiz.get_punctaj()
            else:
                print("Raspuns gresit!")
                punctaj -= quiz.get_punctaj()
        else:
            raise ValueError("Te rog să alegi una dintre variantele de răspuns.")

    if punctaj > 0:
        print("Felicitări! Ai acumulat un punctaj total de {} puncte".format(punctaj))
    else:
        print("Ai un punctaj de: {} puncte.".format(punctaj))


def main():
    menu_options = {1: start}

    print("1) Start\n2) Iesire")
    try:
        cmd = int(input("Alege: "))
        if cmd == 2:
            return
        elif cmd in menu_options:
            menu_options[cmd]()
        else:
            print("Invalid choice")
    except Exception as ex:
        print(ex)


if __name__ == "__main__":
    main()

