hora = input("Informe a Hora: ")


try:
    horaFormatada= int(hora)
    
    if horaFormatada > -1 and horaFormatada < 12:
        print("Bom Dia")
    elif horaFormatada > 11 and horaFormatada < 18:
        print("Boa Tarde")
    elif horaFormatada > 17 and horaFormatada < 24:
        print("Boa Noite")
    else:
        print("Hora inválida")
except ValueError:
    print("valor Inválido")
