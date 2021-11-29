# Author: David Van Vleet
# Date of Creation: 11/28/2021
# Course Number: Web Application Development 3900

import pandas as pd
import csv
import Customer

def check_Customer():

    custID = 0

    col_list = ["cust_id", "first_name", "last_name", "company_name", "address", "city", "state", "zip"]
    #col_list_two = ["cust_id", "first_name", "last_name"]

    df = pd.read_csv("customers.csv", usecols=col_list)
    #dg = pd.read_csv("customers.csv", usecols=col_list_two)

    try:
        custID = int(input("Enter Customer ID: "))
        #cust = Customer("cust_id", "first_name", "last_name", "company_name", "address", "city", "state", "zip")
    except:
        print("")

    id = df["cust_id"].tolist()
    first = df["first_name"].tolist()
    last = df["last_name"].tolist()
    print(last[0])
    comp = df["company_name"].tolist()
    address = df["address"].tolist()
    city = df["city"].tolist()
    state= df["state"].tolist()
    zip = df["zip"].tolist()

    for row in id:
        #customer = Customer(df["cust_id"][], df["first_name"], df["last_name"], df["company_name"], df["address"], df["city"], df["state"], df["zip"])
        customer = Customer(id[row], first[row], last[row], comp[row], address[row], city[row], state[row], zip[row])

    print("CUSTOMER VIEW\n")

    print("ALL CUSTOMERS\n")

    print("--------------------------")

    display = "{} : {}".format(customer.cust_ID(), customer.cust_name())

    print(display + "\n")

    try:
        custID = int(input("Enter Customer ID: "))
        #cust = Customer("cust_id", "first_name", "last_name", "company_name", "address", "city", "state", "zip")
    except:
        print("")

    if custID in id:
        print("The customer ID {} exists!".format(custID))
    else:
        print("The customer ID {} doesn't exist!".format(custID))

    cust_address = customer.cust_fullAddress()

    print(cust_address + "\n")

def main():
    choice = True

    while choice:

        check_Customer()

        user = input("Would you like to continue? y/n: ")

        if user == 'n' or user == 'N' or user == 'no' or user == 'No':
            choice = False

if __name__ == "__main__":
    main()