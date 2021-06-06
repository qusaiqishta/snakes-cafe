print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
************************************** 
""")

Appetizers=['Wings','Cookies','Spring Rolls']

Entrees=['Salmon','Steak', 'Meat TornadoA ','Literal Garden']

Desserts=['Ice', 'CreamCake','Pie']

Drinks=['Coffee','Tea','Unicorn Tears']

print("""
Appetizers
----------
""")

for sweet in Appetizers:
    print(sweet)


print("""
Entrees
-------
""")

for meal in Entrees:
    print(meal)


print("""
Desserts
--------
""")

for dessert in Desserts:
    print(dessert)


print("""
Drinks
------
""")    

for drink in Drinks:
    print(drink)


print("""
***********************************
** What would you like to order? **
***********************************
""")   

whole_menu=Appetizers+Entrees+Desserts+Drinks
ordered=[]

while True:
    order=input('>')
    if order in whole_menu:
        ordered.append(order)
        print('** '+ str(ordered.count(order)) +' eorder of ' +order +' have been added to your meal **')

    elif order not in whole_menu and order!='quit':
        print(f'Sorry! {order} is not included in the menu')

    elif order=='quit':
        print('I guess you finish ordering !')   

        break


