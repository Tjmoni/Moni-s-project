item_dict={}
f=open("stationary_dar.txt","r")
while True:
    item=f.readline()
    if item=='':
        break
    qnt=f.readline()
    uprice=f.readline()
    item=item[:len(item)-1]
    qnt=int(qnt[:len(qnt)-1])
    uprice=float(uprice[:len(uprice)-1])
    item_dict[item]=[qnt,uprice]
f.close()

"""
item_dict={
    "kids_book":[500,1.75],
    "pen":[30,5],
    "pencil":[350,20],
    "ereser":[400,25],
    "colour_paper":[450,9]
    }
    """
def show_dict():
    print("Welcome to Moni's Stationary shop")
    print(30*"=")
    print("Available Products and Quantity")
    print(30*"=")      
    for x in item_dict:
         print(x,(15-len(x))*" ",
               (6-len(str(item_dict[x][0])))*" ",item_dict[x][0])
    print(30*"-")

def dec_quant(key,val):
    item_dict[key][0]-=val
    
def inc_quant(key,val):
    item_dict[key][0]+=val
    
def receive_order():
    print("Order Received")
    while True:
        item=input("Item(type 'x' to stop):")
        if item=="x":
            break
        value=int(input("Quantity:"))
        if item not in item_dict:
            print("New item Found!")
            uprice = float(input("Unit Price:"))
            item_dict[item] = [value,uprice]
            continue
        inc_quant(item,value)
    #show_dict()

def process_demand():
    print("Input Demand")
    # demand_list =
    demand_list = []
    while True:
        item=input("Item(type 'x' to stop):")
        if item=="x":
            break
        if item not in item_dict:
            print(f"The item '{item}' is not available!")
            continue
        value=int(input("Quantity:"))
        if value>item_dict[item][0]:
            print(f"Total of {item_dict[item][0]} pcs are available!")
            continue
        dec_quant(item,value)
        demand_list+=[item,value,
                      item_dict[item][1],value*item_dict[item][1]],
    #printing the payment receipt    
    print(40*"=")
    print("** payment Receipt **".center(40))
    print(40*"=")
    print("Item",7*" ","Quant"," ","U.price",2*" ","S.Total")
    print(40*"-")
    tprice = 0
    for x in demand_list:
        tprice+=x[3]
        print(x[0].title(),(11-len(x[0]))*" ",
              (4-len(str(x[1])))*" ",x[1],
              (7-len(str("%.2f"%x[2])))*" ","%.2f"%x[1],
              (9-len(str("%.2f"%x[3])))*" ","%.2f"%x[2])
    print(40*"-")
    print("Total Price:"," ",tprice)
    print(40*"-")      
    #show_dict()    
    
while True:
    show_dict()
    print("Choose an option:")
    print("Type '1': To process of demand product")
    print("Type '2': To process of ordered product")
    print("Type '3': To exit the process")
    choice = input("choice: ")
    if choice=='1':
        process_demand()
    elif choice=='2':
        receive_order()
    elif choice=='3':
        break
    else:
        continue
    
f=open("stationary_dar.txt","r")
for x in item_dict:
    f.write(x+"\n")
    f.write(str(item_dict[x][0])+"\n")
    f.write(str(item_dict[x][1])+"\n")
f.close()
