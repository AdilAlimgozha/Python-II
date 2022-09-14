d = {"Astana" : ("Kokshetau", "Temirtau", "Karaganda"),
"Karaganda" : "Balhash",
"Balhash" : ("Almaty", "Taraz", "Shymkent"),
"Shymkent" : "Kyzylorda"
}

city = input("write city: ")

i = 1
for x in d:
    if city == "Astana":
        print("capital city")
        break
    elif city in d[x] :
        print(i)
    else:
        i += 1
#done