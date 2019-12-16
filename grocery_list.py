

'''
The task is broken down into three sections.
Section 1 - User Input
Section 2 - loop through the grocery list
Section 3 - provide output to the console
'''

#Task: Create the empty data structure
grocery_item = {}

grocery_history=[]

#Variable used to check if the while loop condition is met
stop = 'go'

while stop == 'go' :
  
    #Accept input of the name of the grocery item purchased.
  item_name = input('Item name:\n')
    #Accept input of the quantity of the grocery item purchased.
  quantity = input('Quantity purchased:\n')
    #Accept input of the cost of the grocery item input (this is a per-item cost).
  cost = input('Price per item:\n') 
    #Using the update function to create a dictionary entry which contains the name, number and price entered by the user.
  if item_name == '' or quantity == '' or cost == '':
    stop = 'stop'
    print('You forgot to enter some data! Please try again')
  else:
    grocery_item = {'name':item_name, 'number': int(quantity), 'price': float(cost)}
    #Add the grocery_item to the grocery_history list using the append function
    grocery_history.append(grocery_item)
    #Accept input from the user asking if they have finished entering grocery items.
  
    nextItem = input('Would you like to enter another item?\nType \'c\' for continue or \'q\' to quit:\n')
    if nextItem == 'c':
      stop = 'go'
    elif nextItem == 'q':
      stop = 'stop'
  
# Define variable to hold grand total called 'grand_total'
grand_total = 0.00
item_total = 0.00
#Define a 'for' loop.  


for items in range(0,len(grocery_history)):
  
  
  #Calculate the total cost for the grocery_item.
  item_total = (grocery_history[items]['number']) * (grocery_history[items]['price'])
  #Add the item_total to the grand_total
  grand_total += item_total 
  #Output the information for the grocery item to match this example:
  #2 apple	@	$1.49	ea	$2.98
  print('{} {} @ ${:.2f} ea ${:.2f}'.format(grocery_history[items]['number'],grocery_history[items]['name'],grocery_history[items]['price'],item_total))
 
  #Set the item_total equal to 0
  item_total = 0.00
#Print the grand total
print('Grand total: ${:.2f}'.format(grand_total))
