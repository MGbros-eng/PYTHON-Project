# Concepts used: Dictionaries, Lists, Functions, Search
# A parcel's status can only move forward:
# Booked -> Picked Up -> In Transit -> Out for Delivery -> Delivered

# ---------------------------------------------------------
# Global data

# The only allowed order of statuses (a list, so we can use index)
STATUS_FLOW = ["Booked", "Picked Up", "In Transit", "Out for Delivery", "Delivered"]

# Main storage: key = tracking ID, value = dictionary of parcel details
parcels = {}

# Counter used to generate IDs automatically (CT1001, CT1002, ...)
next_id_number = 1001
#--------------------------------------------------------------------------------------
# Helper functions
def generate_tracking_id():
    """Create a new unique tracking ID like CT1001 and increase the counter."""
    global next_id_number
    tracking_id = "CT" + str(next_id_number)
    next_id_number += 1
    return tracking_id


def get_non_empty_input(message):
    """Keep asking until the user types something (not blank)."""
    while True:
        value = input(message).strip()
        if value != "":
            return value
        print("Input cannot be empty. Please try again.")


def find_parcel(tracking_id):
    """Return the parcel dictionary if the ID exists, otherwise None."""
    tracking_id = tracking_id.strip().upper()
    if tracking_id in parcels:
        return parcels[tracking_id]
    return None

#------------------------------------------------------------------------------------------

# Main features
def book_parcel():
    """Option 1 - Book a new parcel."""
    sender = get_non_empty_input("Sender: ")
    receiver = get_non_empty_input("Receiver: ")
    destination = get_non_empty_input("Destination: ")

    tracking_id = generate_tracking_id()

    # Each parcel is a dictionary; history is a list of statuses
    parcels[tracking_id] = {
        "id": tracking_id,
        "sender": sender,
        "receiver": receiver,
        "destination": destination,
        "status": "Booked",
        "history": ["Booked"]
    }

    print("Parcel booked. Tracking ID:", tracking_id, "| Status: Booked")


def update_status():
    """Option 2 - Move a parcel to its next status."""
    tracking_id = get_non_empty_input("Tracking ID: ").upper()
    parcel = find_parcel(tracking_id)

    if parcel is None:
        print("Tracking ID", tracking_id, "not found.")
        return

    current = parcel["status"]

    # Status can only move forward, so stop if already delivered
    if current == "Delivered":
        print("Parcel", tracking_id, "is already delivered. No further updates allowed.")
        return

    # Find the next status using the position in the STATUS_FLOW list
    position = STATUS_FLOW.index(current)
    new_status = STATUS_FLOW[position + 1]

    parcel["status"] = new_status
    parcel["history"].append(new_status)

    print("Status updated:", current, "->", new_status)


def track_parcel():
    """Option 3 - Show full details and history of one parcel."""
    tracking_id = get_non_empty_input("Tracking ID: ").upper()
    parcel = find_parcel(tracking_id)

    if parcel is None:
        print("Tracking ID", tracking_id, "not found.")
        return

    print("Tracking ID:", parcel["id"], "| Receiver:", parcel["receiver"],
          "| Destination:", parcel["destination"])
    print("History:", " -> ".join(parcel["history"]))
    print("Current status:", parcel["status"])


def search_by_receiver():
    """Option 4 - Search all parcels using the receiver's name."""
    name = get_non_empty_input("Receiver name to search: ").lower()

    found = False
    # Loop through every parcel (linear search)
    for tracking_id in parcels:
        parcel = parcels[tracking_id]
        if name in parcel["receiver"].lower():
            print(parcel["id"], "| Receiver:", parcel["receiver"],
                  "| Destination:", parcel["destination"],
                  "| Status:", parcel["status"])
            found = True

    if not found:
        print("No parcels found for receiver:", name)


def show_menu():
    """Print the main menu."""
    print()
    print("===== COURIER TRACKING SYSTEM =====")
    print("1. Book parcel")
    print("2. Update status")
    print("3. Track parcel")
    print("4. Search by receiver")
    print("5. Exit")

# Program starts here

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            book_parcel()
        elif choice == "2":
            update_status()
        elif choice == "3":
            track_parcel()
        elif choice == "4":
            search_by_receiver()
        elif choice == "5":
            print("Thank you for using Courier Tracking System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")


main()
