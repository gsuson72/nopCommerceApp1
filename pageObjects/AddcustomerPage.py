import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver


class AddCustomer:
    # Add customer Page

    def __init__(self, driver):
        self.driver = driver

    lnkCustomers_menu_xpath = "//i[@class='nav-icon far fa-user']"
    lnkCustomers_menuitem_xpath = "//a[@href='/Admin/Customer/List']"
    btnAddnew_xpath = "//a[@href='/Admin/Customer/Create']"
    txtEmail_xpath = "//*[@id='Email']"
    txtPassword_xpath = "//*[@id='Password']"
    txtFirstName_xpath = "//*[@id='FirstName']"
    txtLastName_xpath = "//*[@id='LastName']"
    rdMaleGender_id = "//*[@id='Gender_Male']"
    rdFemaleGender_id = "//*[@id='Gender_Female']"
    txtDob_xpath = "//*[@id='DateOfBirth']"
    txtCompanyName_xpath = "//*[@id='Company']"

    #txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']"
    txtcustomerRoles_xpath = "//ul[@id='SelectedCustomerRoleIds_taglist']/.."
    lstitemAdministrators_xpath = "//li [contains (text(),'Administrators')]"
    lstitemRegistered_xpath = "//li[contains (text(),'Registered')]"
    lstitemGuests_xpath = "//li[contains (text(),'Guests')]"
    lstitemVendors_xpath = "//li[contains (text(),'Vendors')]"

    txtNewletter_xpath = "//ul[@id='SelectedNewsletterSubscriptionStoreIds_taglist']/.."
    lstitemStoreName_xpath = "//li [contains (text(),'Your store name')]"
    lstitemTestStore_xpath = "//li [contains (text(),'Test store 2')]"

    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    txtAdminContent_xpath = "//*[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']"

    def clickOnCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.btnAddnew_xpath).click()

    def setEmail(self, email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lname)

    def setDob(self,Dob):
        self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(Dob)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_xpath(self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_xpath(self.rdFemaleGender_id).click()
        else:
            self.driver.find_element_by_xpath(self.rdMaleGender_id).click()

    def setCompanyName(self, comname):
        self.driver.find_element_by_xpath(self.txtCompanyName_xpath).send_keys(comname)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.txtAdminContent_xpath).send_keys(content)

    def setNewsletter(self, news):
        self.driver.find_element_by_xpath(self.txtNewletter_xpath).click()
        time.sleep(3)
        if news == 'Your store name':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemStoreName_xpath)
        elif news == 'Test store 2':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemTestStore_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemTestStore_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();", self.listitem)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
        elif role == 'Guests':
            # choose b/w Registered and Guest
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        elif role == 'Registered':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemRegistered_xpath)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.lstitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()

























