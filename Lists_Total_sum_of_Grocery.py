class Grocery:   #initilization 
    def __init__(self, name, price):
        self.price = price
        self.name = name
        
def total_sum_of_item(Grocery_List):   #defining a function 

    total = sum(item.price for item in Grocery_List)
    print("The sum of the price of item in grocery list is:" , total)

Grocery_List = [
    Grocery("Vegetables", 45),
    Grocery("Meat", 43),
    Grocery("fruits", 39),
    Grocery("Drinks", 42),
    Grocery("Dairy", 34)
]

total_sum_of_item(Grocery_List)   #running a function 