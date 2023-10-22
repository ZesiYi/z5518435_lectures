words = ["Amazing", "Green", "Python", "Code", "Coke Colar", "Hello"]
num = 1
with open("famous_quotes.txt", "w") as file:
    for word in words:
        file.write("No." + str(num) + "  " + word + "\n")
        num = num + 1
