import ice_cream
print("your order id being prepared with ")

scoop_size=input('Enter size: ')
toopings=input('Enter toopings: ')
ice_cream.add_topping(scoop_size, toopings)  

type_of_shake=input('Enter shake flavour: ')
ice_cream.make_shake(type_of_shake)
