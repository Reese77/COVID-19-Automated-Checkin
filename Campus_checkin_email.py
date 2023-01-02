import imaplib
import email
from email.header import decode_header
import webbrowser
import os
import Campus_checkin_website
import Campus_checkin_info

username = Campus_checkin_info.get("emailuser")
password = Campus_checkin_info.get("emailpassword")

def clean(text):
    return "".join(c if c.isalnum() else "_" for c in text)

#login to email
imap = imaplib.IMAP4_SSL("imap.gmail.com")
imap.login(username, password)

#choose inbox
status, messages = imap.select("INBOX")

#counter for while loop
n = 0
#holds current link
link = ""
#subject
subjectline = "Welcome to Campus - Please complete COVID-19 screening".lower()
#gets number of emails
messages = int(messages[0])

#searches through all emails
while messages-n>0:
    # fetch the email message by ID
    res, msg = imap.fetch(str(messages-n), "(RFC822)")
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject, encoding = decode_header(msg["Subject"])[0]
            if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                subject = subject.decode(encoding)
            # decode email sender
            '''From, encoding = decode_header(msg.get("From"))[0]
            if isinstance(From, bytes):
                From = From.decode(encoding)'''
            #only look at email if it's a campus checkin
            if subject.lower().find(subjectline) != -1:
                for part in msg.walk():
                    # extract content type of email
                    content_type = part.get_content_type()
                    content_disposition = str(part.get("Content-Disposition"))
                    try:
                        # get the email body
                        body = part.get_payload(decode=True).decode()
                    except:
                        pass
                    if content_type == "text/plain" and "attachment" not in content_disposition:
                        # print text/plain emails and skip attachments
                        index = 0
                        #extracting the link
                        
                        for element in body:
                            #find where the link starts
                            if body[index:(index+15)] == "https://checkin":
                                new_index = index
                                #search until the end of the link
                                while body[new_index] != "\n":
                                    new_index += 1
                                link = body[index:new_index-1]
                                break;
                            index += 1
                            
                print(link);
                
                #fill out the form with this link
                Campus_checkin_website.fill_out(link)
                #marks email for deleting
                imap.store(str(messages-n), "+FLAGS", "\\Deleted")
            if subject.lower().find("completing") != -1:
                imap.store(str(messages-n), "+FLAGS", "\\Deleted")
                            
                        
    n += 1

#closes the browser
Campus_checkin_website.close_browser()

#Deleting marked emails 
imap.expunge()


#does checkin with general link requiring manual 2 factor authentification
#Campus_checkin_website.fill_out(True, link)
    
# close the connection and logout
imap.close()
imap.logout()
