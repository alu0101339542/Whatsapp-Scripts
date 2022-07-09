from selenium import webdriver
from datetime import datetime
from threading import Timer

#Time
x=datetime.today() #Should probably refresh x and y after the event happens Poner dentro del while 1 quizas
y=x.replace(day=x.day+1, hour=21, minute=32, second=30, microsecond=0)
delta_t=y-x

secs=delta_t.seconds+1

###Driver###
def tosend():
  for i in range(count):
    msg_box.send_keys(msg)
    driver.find_element_by_class_name('tvf2evcx.oq44ahr5.lb5m6g5c.svlsagor.p2rjqpw5.epia9gcq').click()

driver = webdriver.Chrome('/home/dani/Documents/chromedriver')
driver.get('https://web.whatsapp.com/')
name = "Sergio"
msg = "Hola"
count = 200
#Scan the code before proceeding further
input('Enter anything after scanning QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('p3_M1')


t = Timer(secs, tosend)
t.start()




  