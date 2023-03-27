def full_emails(people):
    result=[]
    for email, name in people:
        result.append("{} <{}>".format(name, email))
        return result
        
        
        
        
        
        
print(full_emails([("malyaj@gmail.com", "Malyaj Singh"),("Ankit@example.com","Ankit")]))

          