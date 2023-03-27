animals= ["lion", "zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals :
    chars += len(animals)
    
print("Total Characters: {}, Average Length: {}".format(chars,chars/len(animals)))