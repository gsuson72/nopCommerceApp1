import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("-------- Test_002_DDT_Login --------")
        self.logger.info("-------- Verifying Login DDT test ---------")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Number of Rows in the Excel", self.rows)
        lst_status = []  # empty list variable

        for r in range(2, self.rows + 1):
            self.user = XLUtils.readData(self.path,'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            #self.logger.info(r)
            #self.logger.info(self.user)
            #self.logger.info(self.password)
            #self.logger.info(self.exp)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)



            act_title = self.driver.title
            #self.logger.info(act_title)
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("*** Failed ***")
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title != exp_title:  # can also be if statement
                if self.exp == "Pass":
                    self.logger.info("*** Failed ***")
                    lst_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*** Passed1 ***")
                    lst_status.append("Pass")

        self.logger.info(lst_status)

        if "Fail" not in lst_status:
            self.logger.info("*** Login DDT test passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Login DDT test failed ***")
            self.driver.close()
            assert False
        self.logger.info("-------- End of Test_002_DDT_Login --------")
        self.logger.info("-------- Completed Login DDT test ---------")







