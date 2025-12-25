class Fridge:
    def __init__(self):
        self.items = []

        #Im using a txt file to store the data in.
        try:
            with open("data.txt", "r") as data:
                for line in data:
                    self.items.append(line.strip())
        except FileNotFoundError:
            pass

    #Shows the content of the fridge
    def show_fridge(self):
        print("----- Fridge contents -----")
        if not self.items:
            print("(empty)")
        for item in self.items:
            print(item)

    #I thought it would be easier to add or remove content from the list by using one function instead of two.
    def edit_fridge(self):
        add_or_remove = input("Add or remove [a/r]: ")

        if add_or_remove == "a":
            item = input("Item to add: ")
            self.items.append(item)

        elif add_or_remove == "r":
            item = input("Item to remove: ")
            if item in self.items:
                self.items.remove(item)
                print("Removed.")
            else:
                print("Item not found.")

        else:
            print("Invalid choice.")

    #Saves the fridge using write
    def save_fridge(self):
        with open("data.txt", "w") as data:
            for item in self.items:
                data.write(item + "\n")

#Initialize
MyFridge = Fridge()

#The main loop
while True:
    task = input(
        "\n1. Show fridge\n"
        "2. Edit fridge\n"
        "3. Save fridge\n"
        "4. Exit\n"
        "Choose: "
    )

    if task == "1":
        MyFridge.show_fridge()
    elif task == "2":
        MyFridge.edit_fridge()
    elif task == "3":
        MyFridge.save_fridge()
        print("Saved.")
    elif task == "4":
        break
    else:
        print("Invalid choice.")