# contact_book.py - Contact Book Application
# Starter code for e003-exercise-data-structures

"""
Contact Book Application
------------------------
A simple contact management system using Python data structures.

Data Structure:
- Each contact is a dictionary with: name, phone, email, category, created_at
- All contacts are stored in a list

Complete the TODO sections below to finish the application.
"""

from datetime import datetime

# =============================================================================
# Initialize Contact Book
# =============================================================================
contacts = []


# =============================================================================
# DONE: Task 1 - Create the Contact Book
# =============================================================================

def add_contact(contacts: list, name: str, phone: str, email: str, category: str) -> dict:
    """
    Add a new contact to the contact book.
    
    Args:
        contacts: The list of all contacts
        name: Contact's full name
        phone: Contact's phone number
        email: Contact's email address
        category: One of: friend, family, work, other
    
    Returns:
        The created contact dictionary
    """
    # DONE: Create a contact dictionary with all fields
    new_contact = {
        "name" : name,
        "phone" : phone,
        "email" : email,
        "category" : category,
        "created_at" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    # DONE: Add created_at timestamp using datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # DONE: Append to contacts list
    contacts.append(new_contact)
    # DONE: Return the new contact
    return new_contact


# =============================================================================
# DONE: Task 2 - Display Contacts
# =============================================================================

def display_all_contacts(contacts: list) -> None:
    """
    Display all contacts in a formatted table.
    
    Output format:
    =============================================
                CONTACT BOOK (X contacts)
    =============================================
    #  | Name            | Phone         | Category
    ---|-----------------|---------------|----------
    1  | Alice Johnson   | 555-123-4567  | friend
    ...
    """
    # DONE: Print header with contact count
    print("=" * 50)
    s = "CONTACT BOOK (" + str(len(contacts)) + " contacts)" 
    print(f"{s:^50}")
    print("=" * 50)
    # DONE: Print table headers
    print(f"{'#':<3}| {' Name':<15}| {' Phone':<14}| {' Category':<10}")
    print(f"{"-" * 3}|{"-" * 16}|{"-" * 15}|{"-" * 11}")
    # DONE: Loop through contacts and print each row
    it = 1
    for c in contacts:
        print(f"{it:<3}| { c["name"]:<15}| { c["phone"]:<14}| { c["category"]}")
        it += 1
    # DONE: Print footer
    print("=" * 50)


def display_contact_details(contact: dict) -> None:
    """
    Display detailed information for a single contact.
    
    Output format:
    --- Contact Details ---
    Name:     [name]
    Phone:    [phone]
    Email:    [email]
    Category: [category]
    Added:    [created_at]
    ------------------------
    """
    # DONE: Print formatted contact details
    print(f"{' Contact Details ':-^23}")
    print(f"{"Name:":<13}{contact["name"]}")
    print(f"{"Phone:":<13}{contact["phone"]}")
    print(f"{"Email:":<13}{contact["email"]}")
    print(f"{"Category:":<13}{contact["category"]}")
    print(f"{"Added:":<13}{contact["created_at"]}")


# =============================================================================
# DONE: Task 3 - Search Functionality
# =============================================================================

def search_by_name(contacts, query):
    """
    Find contacts whose name contains the query string.
    Case-insensitive search.
    
    Returns:
        List of matching contacts
    """
    # DONE: Filter contacts where query is in name (case-insensitive)
    newlist = []
    name = query.lower()
    for x in contacts:
        if name in x["name"].lower():
            newlist.append(x)

    return newlist
    # Hint: Use list comprehension and .lower()


def filter_by_category(contacts, category):
    """
    Return all contacts in a specific category.
    
    Returns:
        List of contacts matching the category
    """
    # DONE: Filter contacts by category
    newlist = []
    for x in contacts:
        if category in x["category"]:
            newlist.append(x) 
    return newlist


def find_by_phone(contacts, phone):
    """
    Find a contact by exact phone number.
    
    Returns:
        The contact dictionary if found, None otherwise
    """
    # DONE: Search for contact with matching phone
    newlist = []
    for x in contacts:
        if phone in x["phone"]:
            newlist.append(x)
    if len(newlist) == 0:
        return None
    else:
        return newlist


# =============================================================================
# TODO: Task 4 - Update and Delete
# =============================================================================

def update_contact(contacts, phone, field, new_value):
    """
    Update a specific field of a contact.
    
    Args:
        contacts: The list of all contacts
        phone: Phone number to identify the contact
        field: The field to update (name, phone, email, or category)
        new_value: The new value for the field
    
    Returns:
        True if updated, False if contact not found
    """
    # DONE: Find contact by phone
    # DONE: Update the specified field
    # DONE: Return success/failure
    for x in contacts:
        if phone in x["phone"]:   # Found phone number
            x[field] = new_value  # Change the given field to new value
            return True
    return False                  # Return false when entire for loop runs


def delete_contact(contacts, phone):
    """
    Delete a contact by phone number.
    
    Returns:
        True if deleted, False if not found
    """
    # DONE: Find and remove contact with matching phone
    it = 0
    for x in contacts:
        if phone in x["phone"]:
            contacts.pop(it)        # remove from list
            return True
        it += 1
    return False


# =============================================================================
# TODO: Task 5 - Statistics
# =============================================================================

def display_statistics(contacts):
    """
    Display statistics about the contact book.
    
    Output:
    --- Contact Book Statistics ---
    Total Contacts: X
    By Category:
      - Friends: X
      - Family: X
      - Work: X
      - Other: X
    Most Recent: [name] (added [date])
    -------------------------------
    """
    # DONE: Count total contacts
    amt = 0
    famNum = 0
    friendNum = 0
    workNum = 0
    otherNum = 0
    for x in contacts:
        amt += 1
        if x["category"] == "family":
            famNum += 1
        elif x["category"] == "friend":
            friendNum += 1
        elif x["category"] == "work":
            workNum += 1
        else:
            otherNum += 1

    # DONE: Count contacts by category
    # TODO: Find most recently added contact
    print(f"{' Contact Book Statistics ':-^23}")
    print(f"{"Total Contacts:":<13}{amt}")
    print(f"{"By Category:":<13}")
    print(f"{"  - Friends:"} {friendNum}")
    print(f"{"  - Family:"} {famNum}")
    print(f"{"  - Work:"} {workNum}")
    print(f"{"  - Other:"} {otherNum}")
    pass


# =============================================================================
# STRETCH GOAL: Interactive Menu
# =============================================================================

def display_menu():
    """Display the main menu."""
    print("\n========== CONTACT BOOK ==========")
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Search contacts")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. View statistics")
    print("0. Exit")
    print("==================================")


def main():
    """Main function with interactive menu."""
    # TODO: Implement menu loop
    # Use while True and break on exit choice
    display_menu()
    while (True):
        choice = int(input())
        if (choice == 1):
            display_all_contacts(contacts)
        elif (choice == 2):
            add_contact(contacts, input("Enter Name: "), input("Enter Phone Number: "), input("Enter Email: "), input("Enter Category: "))
        elif (choice == 3):
            search_by_name(contacts, input("Enter Name: "))
        elif (choice == 4):
            update_contact(contacts, input("Enter Phone Number: "), input("Enter Field to be updated: "), input("Enter new value: "))
        elif (choice == 5):
            delete_contact(contacts, input("Enter Phone Number to be deleted: "))
        elif (choice == 6):
            display_statistics(contacts)
        elif (choice == 0):
            break
        print(choice)


# =============================================================================
# Test Code - Add sample data and test functions
# =============================================================================

if __name__ == "__main__":
    print("Contact Book Application")
    print("=" * 50)
    
    # TODO: Add at least 5 sample contacts
    add_contact(contacts, "Alice Johnson", "555-123-4567", "alice@example.com", "friend")
    add_contact(contacts, "Bob Smith", "555-987-6543", "bob@work.com", "work")
    add_contact(contacts, "Carol White", "555-456-7890", "carol@family.net", "family")
    add_contact(contacts, "Alice B", "555-123-4561", "aliceB@example.com", "friend")
    
    # TODO: Test your functions
    display_all_contacts(contacts)
    display_contact_details(contacts[0])
    results = search_by_name(contacts, "alice")
    print(results)
    results = filter_by_category(contacts, "family")
    print(results)
    results = find_by_phone(contacts, "555-98-6543")
    print(results)
    results = update_contact(contacts, "555-987-6543", "name", "Bob Bob")
    print(results)
    results = search_by_name(contacts, "bob")
    print(results)
    results = delete_contact(contacts, "555-987-6543")
    print(results)
    display_all_contacts(contacts)
    display_statistics(contacts)
    # etc.
    
    # STRETCH: Uncomment to run interactive menu
    main()
