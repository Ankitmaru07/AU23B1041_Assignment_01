Annual_profit=int(input("Annual Site Profit: "))
Current _conversion_ rate=int(input("Current Conversion Rate: "))
Improved_conversion_rate=int(input("Improved Conversion Rate: "))
Improvement_cost=int(input("Improvemenet Cost: "))
Expected_project_life=int(input("Expected Project Life: "))
i=0.05
# Future gain improvement
def FGI():
    n=(Annual_profit*(Improved_conversion_rate/Current _conversion_ rate)-Annual_profit)*((1+i)**Expected_project_life-1)/i-Improvement_cost*(1+i)**Expected_project_life
    return n

print(FGI())
#Total gain improvement
def TGI():
    l=FGI()/(i+1)**Expected_project_life
    return l
#Annual gain improment
def AGI():
    s=TGI()/Expected_project_life
    return s

def Annual_ROI():
    a=AGI()/Improvement_cost
    return a

def Total_ROI():
    b=TGI()/Improvement_cost
    return b
    #total gain improvement
    #annual gain improve

print(TGI())
print(AGI())
print(Annual_ROI())
print(Total_ROI())