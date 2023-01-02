
emailuser = "fake@email.com"
emailpassword = "FaKepAsSwOrD"


def get(what):
    if what == "emailuser":
        return emailuser
    elif what == "emailpassword":
        return emailpassword
    else:
        return false
