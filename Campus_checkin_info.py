
emailuser = "fake@email.com"
emailpassword = "FaKepAsSwOrD"
stuff = "e"

def get(what):
    if what == "emailuser":
        return emailuser
    elif what == "emailpassword":
        return emailpassword
    else:
        return false
