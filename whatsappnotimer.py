from selenium import webdriver
from threading import Timer
import random

# prints a random value from the list


###Driver###
driver = webdriver.Chrome('/home/dani/Documents/chromedriver')
driver.get('https://web.whatsapp.com/')
name = "Name"
message_list = ["hola", "Como estas", "Buenos dias", "Que tal", name, "Eyyyy"]
message_apology = ["Lo siento", "Por favor, perdoname", "Perdoname", "Perdon", "No fue mi intencion", name, "Estouy profundamente arrepentido", "No va a volve a pasar", "Voy a cambiar"]
count = 500
#Scan the code before proceeding further
input('Enter anything after scanning QR code a string')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('p3_M1')
for i in range(count):
    msg_box.send_keys(random.choice(message_apology))
    #print(random.choice(message_list))
    driver.find_element_by_class_name('tvf2evcx.oq44ahr5.lb5m6g5c.svlsagor.p2rjqpw5.epia9gcq').click()






  