class parent():
    def _init_():
        
        print("this is parent class")
        
    def menu(dish):
        if dish == "burger":
            print("You can add following topings")
            print("More Cheese/Add Jalapenio")
            
        elif dish == "iced americano":
            print("You can add following topings")
            print("Add cocolate Flavour/ Add carimel flavour")
            
        else:
            print("plese enter valid dish")
            
    def final_dish_amount(dish, add_ons):
        if dish == "burger" and add_ons == "cheese":
            print("YOU have to pay 250 USD")
            
        elif dish == "burger" and add_ons == "Jalapenio":
            print("YOU have to pay 250 USD")
            
        elif dish == "iced americano" and add_ons == "cocolate":
            print("YOU have to pay 350 USD")
            
        elif dish == "iced americano" and add_ons == "carimel":
            print("YOU have to pay 395 USD")
            
class child1(parent):
    
    def _init_(self, dish):
        self.new_dish = dish
    def get_menu(self):
        parent.menu(self.new_dish)
        
class child2(parent):
    def _init_(self, dish, addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_final_amount(self):
        parent.final_amount(self.new_dish,  self.addons)
        
child1_object = child1("burger")
child1_object.get_menu()
            
child2_object = child2("burger", "Jalapenio")
child2_object.get_menu()
                
                