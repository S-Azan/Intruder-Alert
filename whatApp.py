import pywhatkit
from keys import whatsApp_number

Msg = "Testing"
img = 'user.png'
caption = "Find him!"
wait_time = 15
close_tab = False
close_time = 3

def send_whatsapp():
    # pywhatkit.sendwhatmsg_instantly(whatsApp_number, Msg)

    pywhatkit.sendwhats_image(whatsApp_number, img, caption, wait_time, close_tab, close_time)
