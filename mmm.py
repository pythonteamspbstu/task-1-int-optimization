
FOOTING = 2**15
MAX_LEN = 50


def main():
    print("Основание системы M - 2^15")
    print("Максимальная разрядность N - 50")
    print()

    while True:
        print("_________________________________")
        print("")
        print(" 1 - Сложение")
        print(" 2 - Вычитание")
        print(" 3 - Умножение")
        print(" 4 - Целочисленное деление")
        print(" 5 - Выход")
        print(" 6 - Временная проверка перевода числа")
        print("_________________________________")

        choice = input("Выберите операцию (1-5): ").strip()

        match choice:
            case '1':

                print(f"")

            case '2':

                print(f"")

            case '3':

                print(f"")

            case '4':

                print(f"")
            case '5':

                print(f"END")
                break
            case '6':
                a = input()
                print(f"{number_conversion(a)}")

def number_conversion(pol_str):
    st = pol_str.strip()




    #Обработка нуля
    if len(st) == 0 or st == "0":
        return (0, [0])

    #Знак
    if st[0] == '-':
        sign = 1
        st = st[1:]
    else:
        sign = 0

    if not st.isdigit():
        raise ValueError(f"ERROR")

    st = st.lstrip('0')
    if len(st) ==0:
        return (0, [0])

    main_array = []

    for char in st:
        di = int(char)

        carry = 0
        for i in range(len(main_array)):
            temp = main_array[i] * 10 + carry
            main_array[i] = temp % FOOTING
            carry = temp // FOOTING

        while carry > 0:
            main_array.append(carry % FOOTING)
            carry //= FOOTING

        carry = di
        for i in range(len(main_array)):
            temp = main_array[i] + carry
            main_array[i] = temp % FOOTING
            carry = temp // FOOTING
            if carry == 0:
                break

        while carry > 0:
            main_array.append(carry % FOOTING)
            carry //= FOOTING

    main_array = list(reversed(main_array))

    return (sign, main_array)

if __name__ == "__main__":
    main()