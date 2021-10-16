import tkinter
from datetime import datetime
import time
import pytz


app_window = tkinter.Tk()
app_window.title("My Digital Time")
app_window.geometry("1500x1000")
app_window.resizable(None, None)

text = 'Local Time'
text_font= ("Boulder", 48, 'bold')
background = "#9deb91"
foreground= "#363529"
border_width = 25
time_live = time.strftime("%m %B %Y, %H:%M:%S")

timezones = ['Australia/Sydney', 'Israel', 'US/Eastern', 'US/Central', 'US/Mountain', 'US/Pacific']


label0 = tkinter.Label(app_window,  font=text_font, bg=background, fg=foreground, bd=border_width)
label0.grid(row=0, column=0)

label1 = tkinter.Label(app_window,  font=text_font, bg=background, fg=foreground, bd=border_width)
label1.grid(row=1, column=0)

label2 = tkinter.Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width)
label2.grid(row=2, column=0)

label3 = tkinter.Label(app_window,  font=text_font, bg=background, fg=foreground, bd=border_width)
label3.grid(row=0, column=1)

label4 = tkinter.Label(app_window,  font=text_font, bg=background, fg=foreground, bd=border_width)
label4.grid(row=1, column=1)

label5 = tkinter.Label(app_window,  font=text_font, bg=background, fg=foreground, bd=border_width)
label5.grid(row=2, column=1)


def digital_clock():
    label0.config(text='Sydney Australia \n' + datetime.now(pytz.timezone('Australia/Sydney')).strftime("%b %d %Y %H:%M:%S"))
    label1.config(text='New York \n' + datetime.now(pytz.timezone('US/Eastern')).strftime("%b %d %Y %H:%M:%S")) # 'US/Eastern'
    label2.config(text='Chicago \n' + datetime.now(pytz.timezone('US/Central')).strftime("%b %d %Y %H:%M:%S")) # 'US/Central'
    label3.config(text='Denver \n' + datetime.now(pytz.timezone('US/Mountain')).strftime("%b %d %Y %H:%M:%S")) # 'US/Mountain'
    label4.config(text='Reno/Seattle \n' + datetime.now(pytz.timezone('US/Pacific')).strftime("%b %d %Y %H:%M:%S"))
    label5.config(text='Tel Aviv \n' + datetime.now(pytz.timezone('Israel')).strftime("%b %d %Y %H:%M:%S"))
    label0.after(200, digital_clock)


digital_clock()
app_window.mainloop()


