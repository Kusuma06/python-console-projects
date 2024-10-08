import pywhatkit
import pyautogui as pg
from datetime import datetime

now = datetime.now()

chour = now.strftime("%H")
"""mobile = input('Enter Mobile No of Receiver : ')
message = input('Enter Message you wanna send : ')
hour = int(input('Enter hour : '))
minute = int(input('Enter minute : ')) """

pywhatkit.sendwhatmsg_instantly("+918919048144", "msz from chatbot of kusuma adari")

pg.click()
