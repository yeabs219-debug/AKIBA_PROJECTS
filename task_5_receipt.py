name = input("Enter your name: ")

addProduct = input("add product(yes/no)? ")
products =[]
total = 0

while addProduct.strip().lower() == "yes":
      product = { 'name' : input("Enter product name: "),
              'price' :float(input("Enter product price: ")),
              'quantity' : int(input("Enter product quantity: "))       
            }
      item_total = product['price'] * product['quantity']
      products.append(product)
      total += item_total 
      addProduct = input("add product(yes/no)? ")

print(f"""
{products}
========================================
              RECEIPT
========================================

Customer: {name}

Product        Price       Qty
----------------------------------------
{ "\n".join(f"{product['name']}        {product['price']}       {product['quantity']}" for product in products)}

 
Total:         {total} ETB

Thank you for shopping!
========================================

"""
)

