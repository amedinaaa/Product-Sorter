"""
 Description:  Program that gathers inputted information to form and sort a list of products,
 with the ability to search for a product in the list if wanted.

"""

# Function that returns the number of products wanted in list
def get_number():
    numbers = ""
    # While loop that asks user to enter an input, preferably a numeral input
    while numbers.isdigit() == False:
        numbers = input( "Enter the number of products you would like to add.\nEnter 0 (zero) if you do not wish to add products: ")
        # if a negative or non-numeral input is entered the following executes
        if numbers.lstrip("-").isdigit() == True:
            if int(numbers) < 0:
                print("Incorrect Value entered!")
                continue
            else:
                break
        else:
            print("Incorrect date type entered!")
    return int(numbers)

# Function that displays the name of each product
def display_products(products):
    for product in products:
        print(product)

# Function that selection sorts products list
def sort_products(products):
    for i in range(len(products)):
        min = i
        for j in range(i + 1, len(products)):
            if products[j] < products[min]:
                min = j
        if i != min:
            products[i], products[min] = products[min], products[i]
    return products

# Function that conducts a sequential/linear search to identify if a product is in list
def search_products(products, name):
    for i in range(len(products)):
        if products[i] == name:
            return i
    return -1

# Main function for rest of program
def main():
    max_size = get_number()
    products = []
    if max_size == 0:
        print("No products required!")
    else:
        # For loop that will insert inputted products into list
        for i in range(max_size):
            products.insert(i, input("Please enter the product name: "))
        print("Unordered list\n--------------------")
        display_products(products)
        products = sort_products(products)
        print("\nOrdered list\n--------------------")
        display_products(products)
        # Searches for product name, N if No
        name = input("\nEnter a product's name, or N if you do not wish to enter a product's name: ")
        if name == "N":
            pass
        else:
            index = search_products(products, name)
            if index >= 0:
                print("{} is one of the product's names.\nThe position is {}".format(name, index))
            else:
                print("Not Found")

# calls main function
main()

"""--------------Sample Run(1)---------------

Enter the number of products you would like to add.
Enter 0 (zero) if you do not wish to add products:g
Incorrect date type entered!
Enter the number of products you would like to add.
Enter 0 (zero) if you do not wish to add products:-5
Incorrect Value entered!
Enter the number of products you would like to add.
Enter 0 (zero) if you do not wish to add products:3
Please enter the product name: Red
Please enter the product name: White
Please enter the product name: Blue
Unordered list
--------------------
Red
White
Blue

Ordered list
--------------------
Blue
Red
White

Enter a product's name, or N if you do not wish to enter a product's name: Red
Red is one of the product's names.
The position is 1

--------------------End Run-----------------"""