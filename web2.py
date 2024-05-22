from selenium import webdriver
from selenium.webdriver.common.by import By
import datetime
import sqlite3

driver = webdriver.Chrome()
driver.get("https://www.ephemeride.com/home/1/")


texte = driver.find_element(By.XPATH, '/html/body/table[3]/tbody/tr[2]/td[2]/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td[3]/table/tbody/tr[6]/td/table/tbody/tr[2]/td/table/tbody/tr[2]/td[3]')
#texte = driver.find_element(By.PARTIAL_LINK_TEXT, '<td bgcolor="#FFFFFF" class="dBox1">«')
auteur = driver.find_element(By.CLASS_NAME, 'cita')




x = datetime.datetime.now()
ci = texte.text
ca = ci.split("\n")
#print(x.strftime("%d-%m-%Y\n"))
ci_d = x.strftime("%d-%m-%Y")
print(ca[1])
print(ca[0])
print(ci_d)

with open("citation2.txt", "a+", encoding="utf-8") as file:
    file.write(ca[0])
    file.write("\n")
    file.write(ca[1])
    file.write("\n")
    file.write(ci_d)
    file.write("\n")
    file.close()


conn = sqlite3.connect("citations.db")

c = conn.cursor()
#c.execute("""CREATE TABLE citations (
 #   id_citation INTEGER PRIMARY KEY ,
 # citation TEXT,
 # auteur TEXT,
 #   date TEXT
#)""")

citat= [(ca[0], ca[1], ci_d)]


c.executemany("INSERT INTO citations (citation, auteur, date) VALUES (?,?,?)",citat)




conn.commit()
conn.close()