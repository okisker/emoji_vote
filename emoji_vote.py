#Thank you to https://gist.github.com/robulouski/7441883 for the gmail API!
#IMPORT MODULES
import sys
import imaplib
import getpass
import email
import email.header
import datetime
import re
import plotly
import plotly.graph_objs as go
plotly_username = input("Plotly username: ")
plotly_api = input("Plotly API key: ")
plotly.tools.set_credentials_file(username= plotly_username, api_key= plotly_api)
import plotly.plotly as py
from plotly.graph_objs import *

#MAKE LISTS
y_list=[] #money
x_list=[] #emoji

#GMAIL API
gmail = input("Gmail address: ")
EMAIL_ACCOUNT = gmail
EMAIL_FOLDER = "INBOX"

#OPEN FILES FUNCTION
def open_file(file):
    with open (file, 'r') as f:
        string = f.read()
        words = string.split()
    return words

#PROCESS MAILBOX FUNCTION 
def process_mailbox(M):
    rv, data = M.search(None, "ALL")
    if rv != 'OK':
        print("No messages found!")
        return

    for num in data[0].split():
        rv, data = M.fetch(num, '(RFC822)')
        if rv != 'OK':
            print("ERROR getting message", num)
            return

        #FIND SUBJECT AND MESSAGE
        msg = email.message_from_bytes(data[0][1])
        hdr = email.header.make_header(email.header.decode_header(msg['Subject']))
        subject = str(hdr)
        #print('Subject:', subject)
        message = str(msg)
        #print('Message:', message)
        
        #SPLIT SUBJECT AND MESSAGE
        if '$' in subject:
            s_string = subject
            subject = s_string.split()
            #print (subject)
        if '$' in message:
            m_string = message
            message = m_string.split()
            #print (message)
        
        #FIND MONEY
        try:
            for m_word in message:
                for s_word in subject:
                    if m_word == s_word:
                        if s_word.startswith('$'):
                            money = float(s_word[1:])
                            #print(money)
                            y_list.append(money)
                            #print(y_list)
            #FIND EMOJI
            for m_word in message:
                if m_word.startswith('<p>='):
                    utf8_emoji = m_word
                    
            #TRANSLATE EMOJI
            filename = "utf8_emoji.txt"
            with open (filename,"r") as f:
                for line in f.readlines():
                    global x 
                    global y
                    if utf8_emoji in line:
                        utf8 = line.split(',')[0]
                        emoji1 = line.split(',')[1]
                        emoji = emoji1.rstrip('\n')
                        #print(emoji)
                        x_list.append(emoji)
                        #print(x_list)
                        
                        #MAKE DICTIONARY
                        dictionary = {}
                        dictionary.clear()
                        for i in range(len(x_list)):
                            if x_list[i] in dictionary.keys():
                                dictionary[x_list[i]] += y_list[i]
                            else:
                                dictionary[x_list[i]] = y_list[i]
                        #print (dictionary)
                        x=list(dictionary.keys())
                        #print(x)
                        y=list(dictionary.values())
                        #print(y)
                        break
                        
        except FileNotFoundError:
            print("Could not find data file '%s'" % (filename))
                
#GMAIL API                            
M = imaplib.IMAP4_SSL('imap.gmail.com')
try:
    print("Gmail password: ")
    rv, data = M.login(EMAIL_ACCOUNT, getpass.getpass())
except imaplib.IMAP4.error:
    print ("Gmail login failed! ")
    sys.exit(1)
rv, mailboxes = M.list()
rv, data = M.select(EMAIL_FOLDER)
if rv == 'OK':
    process_mailbox(M)

    #TURN INTO BAR GRAPH
    trace = Bar(
    x=x, #emoji
    y=y #amount of money
    )
    data = Data([trace])
    layout = go.Layout(
    title='Vote on Emoji',
    font=dict(family='Courier New, monospace', size=50, color='#7f7f7f'),
    yaxis=dict(tickfont=dict(family='Courier New, monospace', size=20, color='#7f7f7f'))
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='emoji_new')
    
    #GMAIL API
    M.close()
else:
    print("ERROR: Unable to open mailbox ", rv)
M.logout()