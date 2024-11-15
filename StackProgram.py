# Name: Parejas, Arron Kian
#       Marquez, Jian Kalel
#       Miranda, Josh Daniele
#       Lumba, Nelwin

import matplotlib.pyplot as plt
import numpy as np

# View the entire shelf with categories
def view_shelf(shelf): # view the whole shelf with categories and amount using terminal
    try:
        if shelf: 
            for category, items in shelf.items():
                if items:
                    print(f"\nCategory: {category}")
                    print("--------------")
                    for item, stack in items.items():
                        if len(stack) != 0:
                            print("\nItem:", item)
                            print("--------------")
                            for each in range(len(stack) - 1, -1, -1):
                                print("     ", item, "#" + str(each))
        else:
            print("\nShelf is empty!")
    except Exception as e:
        print(f"Error while viewing shelf: {e}")

# Push operation to add items to the shelf within a category
def push(shelf):
    try:
        # Step 1: Prompt for a valid category name
        while True:
            category = input("\nCategory: ").strip()  # Get category input from the user
            if category:  # Ensure the input is not empty
                break  # If valid, exit the loop
            print("Category cannot be empty. Please enter a valid category name.")  # Prompt again if invalid
        
        # Step 2: Check if the category exists; if not, create it
        if category not in shelf:  # If the category is not already in the shelf
            shelf[category] = {}  # Initialize a new dictionary for the category

        # Step 3: Prompt for a valid item name
        while True:
            item = input("\nItem: ").strip()  # Get item input from the user
            if item:  # Ensure the input is not empty
                break  # If valid, exit the loop
            print("Item cannot be empty. Please enter a valid item name.")  # Prompt again if invalid
        
        # Step 4: Prompt for the amount of items to add
        while True:
            amount = input("Amount: ").strip()  # Get amount input from the user
            # Check if the input is a positive integer
            if amount.isdigit() and int(amount) > 0:  
                amount = int(amount)  # Convert valid input to an integer
                break  # If valid, exit the loop
            print("Amount must be a positive integer. Please enter a valid amount.")  # Prompt again if invalid

        # Step 5: Add new item to the category if it doesn't already exist
        if item not in shelf[category]:  # If the item is not in the specified category
            # Create a list of the item, limiting the quantity to a maximum of 10
            shelf[category][item] = [item for _ in range(min(amount, 10))]  
        else:
            # Step 6: If the item exists, add to the stack until it reaches a maximum of 10
            counter = 0  # Initialize a counter to track how many items are added
            while counter < amount and len(shelf[category][item]) < 10:  # Continue adding until the desired amount is reached or stack is full
                shelf[category][item].append(item)  # Add the item to the shelf
                counter += 1  # Increment the counter
            if len(shelf[category][item]) == 10:  # Check if the stack is now full
                print(f"Item: {item}\nStack: Full")  # Inform the user that the stack is full

    # Step 7: Catch any unexpected errors that might occur during the operation
    except Exception as e:
        print(f"Error while pushing stocks: {e}")  # Print the error message

# Pop operation to remove items from a specific category and item
def pop(shelf):
    try:
        if shelf:  # Check if the shelf has any items
            print("\nItem bought")
            
            # Step 1: Ask the user to input a valid category
            while True:
                category = input("  - Category: ").strip()  # Prompt user for category
                if category in shelf:  # Check if category exists in the shelf
                    break  # If category exists, proceed to the next step
                else:
                    print("Category not found. Try again.")  # If not, prompt again

            # Step 2: Ask the user to input a valid item within the selected category
            while True:
                item = input("  - Item: ").strip()  # Prompt user for item
                if item in shelf[category]:  # Check if the item exists in the selected category
                    break  # If the item exists, proceed to the next step
                else:
                    print("Item not found. Try again.")  # If not, prompt again

            # Step 3: Ask the user to input the amount to remove (pop from stack)
            while True:
                amount = input("  - Amount: ").strip()  # Prompt user for amount
                # Check if the input is a positive integer and does not exceed the current stock
                if amount.isdigit() and 0 < int(amount) <= len(shelf[category][item]):
                    amount = int(amount)  # Convert valid input to an integer
                    break  # Proceed to the next step
                else:
                    print("Amount over the limit or invalid. Try again.")  # If not valid, prompt again

            # Step 4: Calculate the index where to stop popping items
            stop = len(shelf[category][item]) - amount  # Determine how many items to remove
            print("\nItems removed:")
            # Step 5: Pop the specified number of items from the item's stack
            for i in range(len(shelf[category][item]) - 1, -1, -1):  # Loop through the stack in reverse
                print(" ", shelf[category][item].pop() + " #" + str(i))  # Remove the item from the stack and print the index
                if i == stop:  # Stop when the required amount is removed
                    break

            # Step 6: Check if any items are running low or out of stock
            warning(shelf)  # Call the warning function to check low stock or empty items
            # Step 7: Display the updated shelf
            view_shelf(shelf)  # Call the view_shelf function to display the current state of the shelf
        else:
            # If the shelf is empty, inform the user and prompt to return to the main menu
            print("\nShelf is empty!\n")
            input("press enter to go back to the main menu")
    
    # Catch any unexpected errors that might occur during the operation
    except Exception as e:
        print(f"Error while popping stocks: {e}")

# Warning for low stock or empty shelf
def warning(shelf):
    try:
        for category, items in shelf.items():
            for item, stack in items.items():
                if 0 < len(stack) <= 3:
                    print(f"\nWARNING: Stock Low for {item} in {category}")
                elif len(stack) == 0:
                    print(f"\nWARNING: No Stocks for {item} in {category}")
    except Exception as e:
        print(f"Error while checking warning: {e}")

# Graph visualization of all stacks in categories
def visualize_shelf(shelf):
    try:
        if shelf:
            categories = [] # list of categories
            item_counts = [] # list of item counts
            for category, items in shelf.items(): # loop the interation of an item
                for item, stack in items.items():
                    categories.append(f"{category} - {item}")
                    item_counts.append(len(stack))

            if categories and item_counts:
                colors = plt.get_cmap('tab20')(np.linspace(0, 1, len(categories)))  # Use a colormap with distinct colors
                x_positions = np.arange(len(categories))  # Positions for the bars

                plt.bar(x_positions, item_counts, color=colors) # Get the positions, colors(Random) of the bars for each category 
                plt.xticks(x_positions, categories, rotation=90)  # Rotate x-axis labels for better readability
                plt.ylabel('Number of Items in Stack') # Get the number of items
                plt.title('Shelf Stock Levels') # Get Stock Levels of its amount
                plt.tight_layout()  # Adjust layout to prevent label overlap
                plt.show()
            else:
                print("No items to display in the graph.")
        else:
            print("Shelf is empty!")
    except Exception as e:
        print(f"Error while visualizing shelf: {e}")

# Main logic to run the menu and handle user actions
# without for loop in 2d array
"""shelf = {
    "Beverages": {
        "Coke": ["Coke", "Coke", "Coke", "Coke", "Coke"],  # 5 items
        "Pepsi": ["Pepsi", "Pepsi", "Pepsi", "Pepsi"],  # 4 items
        "Orange Juice": ["Orange Juice", "Orange Juice", "Orange Juice"],  # 3 items
    },
    "Snacks": {
        "Chips": ["Chips", "Chips", "Chips", "Chips", "Chips", "Chips", "Chips", "Chips"],  # 8 items
        "Chocolate": ["Chocolate", "Chocolate", "Chocolate", "Chocolate", "Chocolate", "Chocolate"],  # 6 items
    },
    "Canned Goods": {
        "Baked Beans": ["Baked Beans", "Baked Beans", "Baked Beans", "Baked Beans", "Baked Beans", "Baked Beans", "Baked Beans"],  # 7 items
        "Tuna": ["Tuna", "Tuna", "Tuna", "Tuna", "Tuna"],  # 5 items
    }
}"""
# with for loop in 2d array
shelf = {                                                           
    "Beverages": {
        "Coke": ["Coke" for _ in range(5)],
        "Pepsi": ["Pepsi" for _ in range(4)],
        "Orange Juice": ["Orange Juice" for _ in range(3)],
    },
    "Snacks": {
        "Chips": ["Chips" for _ in range(8)],
        "Chocolate": ["Chocolate" for _ in range(6)],
    },
    "Canned Goods": {
        "Baked Beans": ["Baked Beans" for _ in range(7)],
        "Tuna": ["Tuna" for _ in range(5)],
    }
}
main = True # Boolean Value

print("\n\t  Welcome to the store!")

while main:
    try:
        print("\n------------- Main Menu -------------")
        print("\n\t  [1]\tView Shelf\n\t  [2]\tPush Stocks\n\t  [3]\tPop Stocks\n\t  [4]\tVisualize Shelf (Data Analytics)\n\t  [5]\tQuit") # Menus Visualize

        action = input("\nAction: ")

        match action:
            case "1":  # Viewing
                view_shelf(shelf)
                input("\npress enter to go back to the main menu")
            case "2":  # Adding / Pushing
                push(shelf)
                input("\npress enter to view shelf")
                view_shelf(shelf)
                input("\npress enter to go back to the main menu")
            case "3":  # Removing / Popping
                pop(shelf)
                input("\npress enter to go back to the main menu")
            case "4":  # Visualize Stock Levels
                visualize_shelf(shelf)
                input("\npress enter to go back to the main menu")
            case "5":  # Quit
                print("\nquitting program\n")
                main = False
            case _:
                raise ValueError("Invalid input. Please enter a valid action number [1-5].")

    except Exception as e: # Exception handling is implemented when error is raised
        print(f"An unexpected error occurred: {e}")
