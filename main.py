from Menu import Pizza,Burger,Drinks,Menu
from Restaurant import Restaurant
from Users import Chef,Customer,Server,Manager
from Order import Order

def main():
    menu=Menu()
    pizza_1=Pizza('mangsho',600,'large',['mangsho,onion'])
    menu.add_item_type('pizzza',pizza_1)
    pizza_2=Pizza('chicken',400,'large',['chicken,onion,oil'])
    menu.add_item_type('pizzza',pizza_2)
    pizza_3=Pizza('alu pizza',200,'large',['alu,doniya,oil'])
    menu.add_item_type('pizzza',pizza_3)

     # add burger to the menu
    burger_1 = Burger('Naga Burger', 1000, 'chicken', ['bread', 'chili'])
    menu.add_item_type('burger', burger_1)
    burger_2 = Burger('Beef Burger', 1200, 'beef', ['goru', 'haddi'])
    menu.add_item_type('burger', burger_2)

    # add drinks to the menu
    coke = Drinks('Coke', 50, True)
    menu.add_item_type('drinks', coke)
    coffee = Drinks('Mocha Coffee', 300, False)
    menu.add_item_type('drinks', coffee)

    # menu.show_menu()

    restaurant=Restaurant('Rahat restaurant',1000,menu)

    #add employees  
    manager=Manager('robi manager',0,'robi@gmail.com','luxmipur',800,'jan 1 2022','core')
    restaurant.add_employee('manager',manager)
    chef = Chef('Rustom Baburchi', 6, 'chupa@rustom.com', 'rustomNagar', 3500, 'Feb 1, 2020', 'Chef', 'everything')
    restaurant.add_employee('chef',chef)
    server = Server('Chotu server', 6, 'nai@jai.com', 'restaurant', 200, 'March 1, 2020', 'server')
    restaurant.add_employee('server', server)

    #show employess
    # restaurant.show_employees()
   
    #customer_1 place 1 order
    customer_1=Customer('fahad',2,'fahad@gmail.com','dattarpara',100000)
    order_1=Order(customer_1,[pizza_3,coffee])
    customer_1.pay_for_order(order_1)
    restaurant.add_order(order_1)
 
    #customer_1 paying for order_1
    restaurant.recive_payment(order_1,2000,customer_1)
    print('revenue and balance',restaurant.revenue,restaurant.balance)

     # customer 2 placing an order
    customer_2 = Customer('Sakib Al Hasan', 6, 'king@khan.com', "banani", 100000)
    order_2 = Order(customer_2, [pizza_1, burger_2, burger_1, pizza_2, coffee])
    customer_2.pay_for_order(order_2)
    restaurant.add_order(order_2)
    # customer one paying for order_1
    restaurant.recive_payment(order_2, 10000, customer_2)

    print('revenue and balance after second customer', restaurant.revenue, restaurant.balance)

     # pay rent
    restaurant.pay_expense(restaurant.rent, 'Rent')
    print('after rent', restaurant.revenue, restaurant.balance, restaurant.expense)

    restaurant.pay_salary(chef)
    print('after salary', restaurant.revenue, restaurant.balance, restaurant.expense)

# call the main 
if __name__ == '__main__':
    main()