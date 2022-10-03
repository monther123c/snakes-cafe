if __name__ == "__main__" : 
    

    MENU = ''' 
    **************************************
    **    Welcome to the Snakes Cafe!   **
    **    Please see our menu below.    **
    **                                  **
    ** To quit at any time, type "quit" **
    **************************************
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls
    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden
    Desserts
    --------
    Ice Creamcoff
    Cake
    Pie
    Beverages
    ------
    Coffee
    Tea
    Unicorn Tears
    ****************************************************
    ** What would you like to order?                  **
    ** take care of how you right the thing u wanna   **
    ****************************************************
    '''
#menu-for order
    menuO= ("Wings", "Cookies" , "Spring Rools" ,"Salmon", "Steak", "Meat Tornado", "A literal Garden",
    "Ice Cream", "Cake", "Pie" , "Coffee", "Tea", "Unicorn Tears")
#add item
    order_add = {}

    print(MENU)
    while True : 
        order = input("> ")
        if order in menuO:
            order_add[order] = order_add.get(order,0)+1

                    
            print("** " , end = "")
            for meal in order_add:
                
                if order_add[meal] == 1:
                    print(f"1 order of {meal} ", end="")
                elif order_add[meal] > 1:  
                    print(f"{order_add[meal]} orders of {meal} ", end="")  
            print("have been added to your meal **")

                
            
        elif order == "quit":
            if len(order_add) == 0:
                print("Have a nice Day !")
            else :
                    print("You ordered : ")
            for meal in order_add:
                print(order_add[meal] , meal)
                

            
            break

           




 

