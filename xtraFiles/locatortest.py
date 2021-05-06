from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome(executable_path="C:\selenium browser driver\chromedriver_win32\chromedriver.exe")

driver.get("https://admin-demo.nopcommerce.com/")

driver.find_element_by_id("Email").clear()
driver.find_element_by_id("Password").clear()
driver.find_element_by_id("Email").send_keys("admin@yourstore.com")
driver.find_element_by_id("Password").send_keys("admin")
print(driver.title)
#driver.find_element_by_xpath("/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button").click()
driver.find_element_by_xpath("//button[contains(text(),'Log in')]").click()

print(driver.title)

#lnkCustomer_menu_xpath
#driver.find_element_by_xpath("/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p").click()
driver.find_element_by_xpath("//i[@class='nav-icon far fa-user']").click()

#lnkCustomer_menuitem_xpath
#driver.find_element_by_xpath("/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p").click()
driver.find_element_by_xpath("//a[@href='/Admin/Customer/List']").click()
print(driver.title)

#btnAddnew_xpath
#driver.find_element_by_xpath("/html/body/div[3]/div[1]/form[1]/div/div/a").click()
driver.find_element_by_xpath("//a[@href='/Admin/Customer/Create']").click()

#txtEmail_xpath
driver.find_element_by_xpath("//*[@id='Email']").send_keys("goe@yahoo.com")
print(driver.title)
#txtPassword_xpath
driver.find_element_by_xpath("//*[@id='Password']").send_keys("pass")
#txtFirstName_xpath
driver.find_element_by_xpath("//*[@id='FirstName']").send_keys("first")
#txtLastName_xpath
driver.find_element_by_xpath("//*[@id='LastName']").send_keys("last")
#rdMaleGender_id
driver.find_element_by_id("Gender_Male").click()
time.sleep(5)
#rdFemaleGender_id
driver.find_element_by_id("Gender_Female").click()
#txtDob_xpath
driver.find_element_by_xpath("//*[@id='DateOfBirth']").send_keys("02/25/1972")
#txtCompanyName_xpath
driver.find_element_by_xpath("//*[@id='Company']").send_keys("UHG")

#txtcutomerRoles_xpath
#driver.find_element_by_xpath("//*[@id='customer-info']/div[2]/div[10]/div[2]/div/div[1]/div/div").click()
#driver.find_element_by_xpath("//div[@class='k-multiselect-wrap k-floatwrap' and @xpath='1']").click()

driver.find_element_by_xpath("//div[@class='k-multiselect-wrap k-floatwrap']").click()

driver.find_element_by_xpath("//li[contains (text(),'Registered')]").click()
driver.find_element_by_xpath("//li [contains (text(),'Administrators')]").click()
driver.find_element_by_xpath("//li[contains (text(),'Guests')]").click()
driver.find_element_by_xpath("//li[contains (text(),'Guests')]").click()

#drpmgrOfVendor_xpath
driver.find_element_by_xpath("//*[@id='VendorId']").click()
#txtAdminContent_xpath
driver.find_element_by_xpath("//*[@id='AdminComment']").send_keys("testing")
#btnSave_xpath
driver.find_element_by_xpath("/html/body/div[3]/div[1]/form/div[1]/div/button[1]")