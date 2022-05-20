# py -2 bcbar.py

# Web Scraping Prerequisites
import requests
import json
# LED Matrix Prerequisites
import re
import time
import argparse
# from luma.led_matrix.device import max7219
# from luma.core.interface.serial import spi, noop
# from luma.core.render import canvas
# from luma.core.virtual import viewport
# from luma.core.legacy import text, show_message
# from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT


while(True):
    channelinfo = requests.get("https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UC78ZVrFPY37EdjyqG6Aj4fQ&key=AIzaSyB7aSNfwx7Z5UQswqLma3ZZoNeawVidsg8")
    subCount = channelinfo.json()['items'][0]['statistics']['subscriberCount']
    show_message(device, subCount, fill="white", font=proportional(LCD_FONT),scroll_delay = 0.02)
    time.sleep(300)



    # disp = [0]*38   #38 is the length of the list data
    # for x in range(len(data)):
    #     if x % 2 == 0:
    #         disp.append(data[x])
    #         if data[x+1] == None:
    #             disp.append(data[x+1])
    #         else:                
    #             disp.append((data[x+1]).replace(',',''))    #Each element of disp is the Name of the parameter & its value. The commas present in the values have been removed for better displaying asthetics


    # disp = list(filter(lambda a:a != 0, disp)) #For some reason every odd element of the list 'disp' is '0'. This removes all occurences of '0' from the list 'disp'
    # #Remove 'list' in Python2.7


    # serial = spi(port=0, device=0, gpio=noop())
    # device = max7219(serial, cascaded=4 , block_orientation=-90, rotate=2)

    # for i in range(len(disp)):
    #     show_message(device, disp[i], fill="white", font=proportional(LCD_FONT),scroll_delay = 0.02) #Change the value of 'scroll_delay' to change the Scrolling Speed

    #show_message(device, disp[4], fill="white", font=proportional(LCD_FONT),scroll_delay = 0.02) # '4' indicates Displays the number of Bitcoins left to mine.
    #Change this value according to the table to display various data parameters
