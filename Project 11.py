productsDict = {} 
currentID = 1

def order():
    orderList = []
    ID = 1
    subtotal = 0
    while True:
        A_makeup_artist = input('Enter makeup artist name: ')
        print_by_makeup(A_makeup_artist)
        name = input('Type makeup brand name: ')
        makeup_artist = productsDict[name][1]
        price = productsDict[name][3]
        quantity = productsDict[name][4]
        if quantity == 0:
            print('Not in the stock! Sorry!')
            continue
        productsDict[name][4] -= 1
        orderList.append([name, makeup_artist, price])
        subtotal += price
        cont = input('Continue? Please Press Y: ')
        if cont != 'Y':
            break

    print('-----Bill-----')
    for order in orderList:
        print(ID, order[0], order[1], order[2])
    print('4% sales tax: ', 0.48*subtotal)
    print('Total: ', subtotal + 0.48*subtotal)

def create_product():
    productname = input('Enter makeup product: ')
    fout = open(productname, 'w')
    fout.close()
    return productname

def print_by_makeup(makeup_artist):
    for name in productsDict:
        product = productsDict[name]
        if makeup_artist == product[1]:
            print ('%d\t%s\t%s\t%s\t%g\t%d' % (product[0],name,product[1],product[2],product[3],product[4]))
    
def add_product():
    global productsDict, currentID
    
    makeupName = input('Enter makeup artist: ')
    brandname = input('Enter brand name: ')
    product = input('Enter product: ')
    price = float(input('Enter price: '))
    quantity = int(input('Enter quantity: '))
    if makeupName not in productsDict:
        productsDict[makeupName] = [currentID, brandname, product, price, quantity]
        currentID += 1
    else:
        print('Product associated with brand name exists')
        
def revise_makeup_product():
    global productsDict
    name = input('Enter product name: ')
    if name not in productsDict:
        print('Product not found')
    else:
        product = productsDict[name]
        print('Press enter to skip')
        artist = input('Enter makeup artist name: ')
        if artist != '':
            product[1] = brand
        brand = input('Enter brand name: ')
        if brand != '':
            product[2] = product
        price = input('Enter price: ')
        if price != '':
            product[3] = float(price)
        quantity = input('Enter quantity: ')
        if quantity != '':
            product[4] = int(quantity)
            
            
            
def load_from_file():
    global productsDict, currentID
    filename = input('Enter filename to open: ')
    fin = open(filename, 'r')

    productsDict = {}

    lines = fin.readlines()

    for line in lines:
        parsedLine = line.split(',')
        recordID = int(parsedLine[0])
        makeupName = parsedLine[1]
        brand = parsedLine[2]
        product = parsedLine[3]
        price = float(parsedLine[4])
        quantity = int(parsedLine[5])
        productsDict[makeupName] = [recordID, makeupartist, brand, price, quantity]
        currentID = max(currentID, recordID)

    fin.close()
    currentID += 1
    return filename

def total_sum():
    global productsDict
    total = 0
    for product in productsDict:
        total += productsDict[product][3]*productsDict[product][4]
    return total

def save_into_file(filename):
    fout = open(filename, 'w')
    for makeupName in productsDict:
        currentID = productsDict[makeupName][0]
        makeupartist = productsDict[makeupName][1]
        brand = productsDict[makeupName][2]
        price = productsDict[makeupName][3]
        quantity = productsDict[makeupName][4]
        fout.write('%d,%s,%s,%s,%g,%d\n' % (currentID, recordName,makeupartist, brand, price, quantity) )

    fout.close()
    
def print_all():
    print('ID\tName\tMakeupArtist\tBrand\tPrice\tQuantity')   
    for recordName in productsDict:
        ID = productsDict[recordName][0]
        makeupartist = productsDict[recordName][1]
        brand = productsDict[recordName][2]
        price = productsDict[recordName][3]
        quantity = productsDict[recordName][4]
        print('%d\t%s\t%s\t%s\t%g\t%d' % (ID, recordName, makeupartist, brand, price, quantity))

def create_file():
    filename = input('Enter filename: ')
    fout = open(filename, 'w')
    fout.close()
    return filename

def main():
    option = ''
    # menu
    state = 'BEGIN'
    while True:
        # BEGIN STATE
        if state == 'BEGIN':
            print('Q: Quit\tC: Create\tL: Load')
            option = input('Select the option: ')
            if option == 'Q':
                # END STATE
                break
            elif option == 'C':
                productname = create_product()
                state = 'WORKSPACE'
            elif option == 'L':
                productname = load_from_file()
                state = 'WORKSPACE'
        elif state == 'WORKSPACE':
            # WORKSPACE
            print('WORKSPACE: ', productname)
            print('A:Add\tS:Save\tM:Modify:\tO:Order\tT:Total\tP:Print')
            option = input('Select the option: ')
            if option == 'A':
                add_product()
            elif option == 'S':
                save_into_file(productname)
            elif option == 'P':
                print_all()
            elif option == 'T':
                print(total_sum())
            elif option == 'M':
                revise_makeup_product()
            elif option == 'O':
                order()
            else:
                break
            

main()
