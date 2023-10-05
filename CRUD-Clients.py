# Define an empty list to store clients
clients = []

# Function to create a new client
def create_client(first_name, last_name, email):
    client = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }
    clients.append(client)
    print("Client created successfully!")

# Function to display all clients
def show_clients():
    if not clients:
        print("No clients registered.")
    else:
        for i, client in enumerate(clients):
            print(f"Client {i + 1}:")
            print(f"First Name: {client['first_name']}")
            print(f"Last Name: {client['last_name']}")
            print(f"Email: {client['email']}")
            print()

# Function to update client information
def update_client(index, first_name, last_name, email):
    if 0 <= index < len(clients):
        clients[index]["first_name"] = first_name
        clients[index]["last_name"] = last_name
        clients[index]["email"] = email
        print("Client updated successfully!")
    else:
        print("Invalid client index.")

# Function to delete a client
def delete_client(index):
    if 0 <= index < len(clients):
        del clients[index]
        print("Client deleted successfully!")
    else:
        print("Invalid client index.")

# Menu of the application
while True:
    print("\n--- Menu ---")
    print("1. Create Client")
    print("2. Show Clients")
    print("3. Update Client")
    print("4. Delete Client")
    print("5. Exit")
    
    option = input("Select an option (1/2/3/4/5): ")
    
    if option == "1":
        first_name = input("Enter the client's first name: ")
        last_name = input("Enter the client's last name: ")
        email = input("Enter the client's email: ")
        create_client(first_name, last_name, email)
    elif option == "2":
        show_clients()
    elif option == "3":
        index = int(input("Enter the index of the client to update: "))
        first_name = input("Enter the new first name of the client: ")
        last_name = input("Enter the new last name of the client: ")
        email = input("Enter the new email of the client: ")
        update_client(index - 1, first_name, last_name, email)
    elif option == "4":
        index = int(input("Enter the index of the client to delete: "))
        delete_client(index - 1)
    elif option == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please select a valid option (1/2/3/4/5).")
        
# Watermark for the creator of the project
print("Created by John Zambrano")
