# Create a list of inventory items
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", 
             "dresser", "dresser", "table", "table", "nightstand", "nightstand", 
             "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", 
             "pillow", "pillow"]

# Calculate the total number of items in the inventory
inventory_len = len(inventory)

# Select the first item in the inventory
first = inventory[0]

# Select the last item in the inventory
last = inventory[-1]

# Select items from index 2 to 5 (up to, but not including, index 6)
inventory_2_6 = inventory[2:6]

# Select the first three items in the inventory
first_3 = inventory[0:3]

# Count the number of 'twin bed' items in the inventory
twin_beds = inventory.count('twin bed')

# Remove the item at index 4 and store it in removed_item
removed_item = inventory.pop(4)

# Insert '19th Century Bed Frame' at index 10
inventory.insert(10, '19th Century Bed Frame')

# Sort the inventory list in alphabetical order
inventory.sort()

# Print the sorted inventory list
print(inventory)
