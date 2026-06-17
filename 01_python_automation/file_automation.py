import datetime

requests = []

def add_request(name, request_type):
    request = {
        "name": name,
        "type": request_type,
        "status": "Pending",
        "time": datetime.datetime.now()
    }
    requests.append(request)
    print("Request added successfully!")

def show_requests():
    for r in requests:
        print(r)

add_request("Andrew", "Leave Request")
add_request("Finance Dept", "Expense Approval")

show_requests()