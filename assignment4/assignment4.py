#Write a function where it prints pokemon names based on their type1 or type2.

with open("pokemon_data.csv", "r") as file: #opening the file in read mode
    contents = file.read() #reading the contents of the file
    lines = contents.splitlines() #splitting the contents by lines
     #splitting the lines by commas and saving them to a list of columns for my sanity
    columns = [line.split(",") for line in lines] 

    header = columns[0] #grabs the column names

type1Index = header.index("type1") #finds which index the type1 column is in
type2Index = header.index("type2") #finds which index the type2 column is in
nameIndex = header.index("name") #finds which index the name column is in

type1 = [row[type1Index] for row in columns[1:]] #creates the list of type1 by using the type1Index but excludes the header
type2 = [row[type2Index] for row in columns[1:]] #creates the list of type2 by using the type2Index but excludes the header
name = [row[nameIndex] for row in columns[1:]] #creates the list of name by using the nameIndex but excludes the header


givenType = input("Enter a type: ").capitalize() #asks the user to input a type and caps it to match
try: #if the user inputs a type that exists

    #function to find the pokemon based on their type1 or type2
    def pokemonType(givenType,type1, type2, name):
        #list that will store names of pokemon that match the type
        nameList = [] 
        #loops through the length of the name list
        for i in range(len(name)):
              #If givenTpe matches type1 or type2 appends the name to the list
              if givenType == type1[i] or givenType == type2[i]: 
                  #appends the name to the list
                  nameList.append(name[i])
         #returns the list         
        return nameList
     #calls the functions and stores result in pokemon  
    pokemon = pokemonType(givenType, type1, type2, name)
    #when the list has values if will print the pokemon names of given type sanely formatted
    if pokemon:
        #{givenType} will be replaced with the type the user input
        print(f"Pokémon of type {givenType}:")
        #takes the list of pokemon names and joins into a single string that then separates each name with /n
        print("\n".join(pokemon))
    else:
         #if the list is empty it will print that no pokemon were found with the given type
         print(f"No Pokémon found with type {givenType}.")
except: #if the user inputs a type that does not exist
    print("Invalid input. Please try again.")