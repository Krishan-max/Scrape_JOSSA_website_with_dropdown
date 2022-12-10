import time
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
class dropdown_scraper():

    def get_table_data(self,dropdown_comb):
        driver=webdriver.Chrome(executable_path=ChromeDriverManager().install())
        driver.get("https://josaa.admissions.nic.in/applicant/seatmatrix/OpeningClosingRankArchieve.aspx")
        for step in range(0,len(dropdown_comb)):
            try:
                for var in range(1,7):
                    drop = driver.find_element(By.XPATH,"(//a[@class='chosen-single'])[%s]"%var)
                    WebDriverWait(driver,20).until(expected_conditions.element_to_be_clickable(drop))
                    time.sleep(1)
                    drop.click()
                    fill=driver.find_element(By.XPATH,'(//input[@type="text"])[%s]'%var)
                    fill.send_keys(dropdown_comb[step][var-1])
                    fill.send_keys(Keys.ENTER)

                driver.find_element(By.XPATH,'//input[@type="submit"]').click()
                time.sleep(1)
                Institute=driver.find_elements(By.XPATH,'//td[@align="left"][1]')
                APN=driver.find_elements(By.XPATH,'//td[@align="left"][2]')
                Quota=driver.find_elements(By.XPATH,'//td[@align="left"][3]')
                ST=driver.find_elements(By.XPATH,'//td[@align="left"][4]')
                Gender=driver.find_elements(By.XPATH,'//td[@align="left"][5]')
                OR=driver.find_elements(By.XPATH,'//td[@align="left"][6]')
                CR=driver.find_elements(By.XPATH,'//td[@align="left"][7]')
                tabledata = []

                for i in range(0,len(Institute)):
                    temp_dic={"Year":dropdown_comb[step][0],"Round":dropdown_comb[step][1],"Institute Type":dropdown_comb[step][2],"Institute":Institute[i].text,"Academic Program Name":APN[i].text,"Quota":Quota[i].text,"Seat Type":ST[i].text,"Gender":Gender[i].text,"Opening Rank":OR[i].text,"Closing Rank":CR[i].text}
                    tabledata.append(temp_dic)
                alldata = pd.DataFrame(tabledata)
                alldata.to_csv("NI1%s.csv" %step)
            except:
                continue

dropdown_comb=[[2016,4,"Indian Institute of Information Technology","ALL","ALL","ALL"]]
table_data_object=dropdown_scraper()
table_data_object.get_table_data(dropdown_comb)