import json

# Open and load the JSON file
with open('./PokeTCG.json', 'r',  encoding='utf-8-sig') as file:
    data = json.load(file)

# Print the loaded data (optional)
#print the name of all fighting type pokemon

#print all cards from the set "HeartGold & SoulSilver"

#print all cards where the averageSellPrice is greater than 1.5
#data['data']
input("name: ")
for name in data:
    if type == ['Fighting']:
        print(name)
    else:
        print("not fighting")



'''for prices in data:
    if prices == ["normal"]:
        print ('Pokémon')
print ("not fighting")'''
