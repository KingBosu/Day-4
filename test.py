class MyCart:


    def __init__(self):
        self.basket = {}
        self.cart_index = 0

    def add_to_cart(self,items):
        self.basket[self.cart_index] = items
        self.cart_index +=1

    def view_cart(self):
        print(self.basket)

    def remove_from_cart(self,items):
        self.basket.pop(items)

def main():
    cart = MyCart()
    while True:
      option = input("What would you like to do, 'add' to add item', 'view' to view cart, 'remove' to remove item from cart and 'done' when finished ")
      if option == 'done':
            break
      elif option =='view':
            cart.view_cart()
      elif option == 'remove':
            print("Choose which number item you would like to remove ",cart.basket)
            response= int(input("What would you like to remove? "))
            cart.remove_from_cart(response)
      elif option == 'add':
            response = input("What would you like to add ")
            cart.add_to_cart(response)

main()
      