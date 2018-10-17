# Created a function to determine the order of books
def determine_order_of_books(first_book, second_book):
  if first_book < second_book:
    print("Order is first book followed by second book")
  elif first_book > second_book:
    print("Order is second book followed by first book")
  else:
    print("The order does not matter")
  
# The following are calls to the function for testing purposes
determine_order_of_books(7, 5)
determine_order_of_books(1, 3)
determine_order_of_books(4, 4)
