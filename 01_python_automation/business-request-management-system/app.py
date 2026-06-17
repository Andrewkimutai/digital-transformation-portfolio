import json
import os

DATA_FILE = "requests.json"


def load_requests():
    if not os.path.exists(DATA_FILE):
        return []

    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_requests(requests):
    with open(DATA_FILE, "w") as file:
        json.dump(requests, file, indent=4)


def create_request():
    requests = load_requests()

    employee = input("Employee Name: ")
    request_type = input("Request Type: ")
    description = input("Description: ")

    new_request = {
        "id": len(requests) + 1,
        "employee": employee,
        "request_type": request_type,
        "description": description,
        "status": "Pending",
    }

    requests.append(new_request)
    save_requests(requests)

    print("Request submitted successfully!")


def view_requests():
    requests = load_requests()

    if not requests:
        print("No requests found.")
        return

    for request in requests:
        print("\n----------------")
        print(f"ID: {request['id']}")
        print(f"Employee: {request['employee']}")
        print(f"Type: {request['request_type']}")
        print(f"Description: {request['description']}")
        print(f"Status: {request['status']}")


def update_status():
    requests = load_requests()

    request_id = int(input("Enter Request ID: "))

    for request in requests:
        if request["id"] == request_id:
            print("1. Approve")
            print("2. Reject")

            choice = input("Choose option: ")

            if choice == "1":
                request["status"] = "Approved"

            elif choice == "2":
                request["status"] = "Rejected"

            save_requests(requests)

            print("Status updated successfully!")
            return

    print("Request not found.")


def main():
    while True:
        print("\n=== Business Request Management System ===")
        print("1. Create Request")
        print("2. View Requests")
        print("3. Update Request Status")
        print("4. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            create_request()

        elif choice == "2":
            view_requests()

        elif choice == "3":
            update_status()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
