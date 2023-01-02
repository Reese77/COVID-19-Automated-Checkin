
emailuser = "fake@email.com"
emailpassword = "FaKepAsSwOrD"
stuff = "g"

def get(what):
    if what == "emailuser":
        return emailuser
    elif what == "emailpassword":
        return emailpassword
    else:
        return false
