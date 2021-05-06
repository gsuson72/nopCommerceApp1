from selenium import webdriver
import time

class SearchCustomer:

    txtEmail_id = "SearchEmail"
    txtFirstName_id = "SearchFirstName"
    txtLastName_id = "SearchLastName"
    btnSearch_id = "search-customers"

    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath = "//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self, driver):
        self.driver = driver

    def setSEmail(self, email):
        self.driver.find_element_by_id(self.txtEmail_id).clear()
        self.driver.find_element_by_id(self.txtEmail_id).send_keys(email)

    def setFirstName(self, fname):
        self.driver.find_element_by_id(self.txtFirstName_id).clear()
        self.driver.find_element_by_id(self.txtFirstName_id).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_id(self.txtLastName_id).clear()
        self.driver.find_element_by_id(self.txtLastName_id).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element_by_id(self.btnSearch_id).click()

    def getNoOfRows(self):
        return len(self.driver.find_elements_by_xpath(self.tableRows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_elements_by_xpath(self.tableColumns_xpath))

    def searchCustomerByEmail(self, email):
        flag = False
        for r in range(1, self.getNoOfRows()+1):
            print(str(r))
            table = self.driver.find_element_by_xpath(self.table_xpath) #setting the table
            emailid = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            print(emailid)
            print(email)
            if emailid == email:
                flag = True
                print(flag)
                break
            else:
                flag = False
                print(flag)
        return flag

    def searchCustomerByName(self, name):
        flag = False
        for r in range(1, self.getNoOfRows() + 1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            custname = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            print(custname)
            print(name)
            if custname == name:
                flag = True
                print(flag)
                break
            else:
                flag = False
                print(flag)
        return flag















