import random
group_of_items = ['Dave','Andrew', 'John', 'Ronaldo','Messi','Petr','Van Der Saar']
selectedPlayer = 5                           
listOfRandomItems = random.sample(group_of_items, selectedPlayer)
A = listOfRandomItems[0]
B = listOfRandomItems[1]
C = listOfRandomItems[2]
D = listOfRandomItems[3]
E = listOfRandomItems[4]
print("A:",A)
print("B:" ,B)
print("C:" ,C)
print("D:" ,D)
print("E:" ,E)
print ("which player do you  want? A, B, C, D or E")
