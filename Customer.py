# Author: David Van Vleet
# Date of Creation: 11/28/2021
# Course Number: Web Application Development 3900

import pandas as pd

class Customer:

    cust_num = 0
    fName = ""
    lName = ""
    company = ""
    street = ""
    city = ""
    state = ""
    zipcode = 0

    def __init__(self, cust_num, fname, lname, company, street, city, state, zipcode):
        self.cust_num = cust_num
        self.fname = fname
        self.lname = lname
        self.company = company
        self.street = street
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        return "{}\n{}".format(self.cust_name, self.cust_fullAddress)

    def cust_name(self):
        return "{} {}".format(self.fName, self.lName)

    def cust_fullAddress(self):
        if self.company is None:
            return "{} \n{}, {} {}".format(self.street, self.city, self.state, self.zipcode)
        else:
            return "{} \n{} \n{}, {} {}".format(self.company, self.street, self.city, self.state, self.zipcode)

    def cust_ID(self):
        return self.cust_ID

    def cust_company(self):
        return self.company
