# This global variable keeps track of the state of our program.
customer_count = 0

# This function has a side effect: it changes the state of the
# program  when it's called. Note that it doesn't even have a real
# return value.
def add_customers(n):
    global customer_count
    customer_count = customer_count + n
    print("Added {} new customers".format(n))
    return None
    
# First let's print the state of our program before changing it.
print(customer_count)

# Now let's call our function and see what happens.
add_customers(10)
add_customers(3)
print(customer_count)

# Here is a much better approach.
sale_count = 0

def add_sale(n, sale_count):
    return n + sale_count

sale_count = add_sale(40, sale_count)
sale_count = add_sale(2, sale_count)
print(sale_count)
