lista = ["Hiderlano", "Luciano", "Euclides", "Aldeci", "Sousajr"]
conta = "yes"
print ("=" * 30)
name = input("Type the first name: ")
#while conta=="yes":
while name in lista:
            print(name.upper()," is a contact from Brazil. Analyze WhatsApp? (yes/no)")
            resp = input()
            if resp == "yes":
                print("Fetching data... Press ENTER after 5s")
                input()
                if name == "Luciano":
                    print("Boco'")
                    break
                else:
                    if name == "Hiderlano":
                        print("Panda")
                        break
                    else:
                        if name == "Euclides":
                            print("Pai")
                            break
                        else:
                            if name == "Aldeci":
                                print("highlander")
                                break
                            else:
                                if name == "Sousajr":
                                    print("Malhacao")
                                    break
            else:
                print("Thanks for coming")
                break
else:
    print(name.upper(), ' Is not a contact.')
