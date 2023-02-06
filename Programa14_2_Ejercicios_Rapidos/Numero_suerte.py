def main():
    print("Este programa te dira tu número de la suerte!!!\n")
    day = input("Escribe tu día de nacimiento en formato dd: ")
    month = input("Escribe tu mes de nacimiento en formato mm: ")
    year = input("Escribe tu año de nacimiento en formato aaaa: ")

    list_day = [int(x) for x in day]
    list_month = [int(x) for x in month]
    list_year = [int(x) for x in year]
    
    pre = list_day[0] + list_day[1] + list_month[0] + list_month[1] + list_year[0] + list_year[1] + list_year[2] + list_year[3]

    list_pre = [int(x) for x in str(pre)]

    if len(list_pre)>1:
        fin = list_pre[0] + list_pre[1]
    else:
        fin = list_pre[0]

    print("Tu número de la suerte es: ", fin)


if __name__ == "__main__":
    main()