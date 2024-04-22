def get_name():
    global name
    name=input("enter your name:")
    return name

def get_tshirt():
    global name
    get_name()
    a=input("which brand do you want:")
    brand=['adidas', 'peter england', 'calvin klein', 'zara', 'raymond']
    for i in brand:
      if i==a:
        print("Hi", name , ",", "the brand you are looking for is available in our store.")
        break
      else:
        print("Hi", name , ",", "the brand you are looking for is not available in our store.")
        break

get_tshirt()
