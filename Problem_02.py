def get_name():
    name=input("enter your name:-")
    return name

def get_tshirt():
    name=get_name()
    company=input("which brand do you want:-")
    sinput=input("in which size do you want:-")
    brand=['adidas', 'peter england', 'calvin klein', 'zara', 'raymond']
    size=['xs', 's', 'm', 'l', 'xl', 'xxl']
    for i in brand and size:
      if i==company or i==sinput:
        print("Hi", name + ",", "the brand you are looking for is available in our store.")
        break
      else:
        print("Hi", name + ",", "the brand you are looking for is not available in our store.")
        break
get_tshirt()