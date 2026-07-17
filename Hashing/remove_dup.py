# Removing duplicates from a set of list -- Checking exact number of online users removing multiple logins
emails=["vaibhavi811@gamil.com","renubansal123@gamail.com","vaibhavi811@gamil.com","renubansal123@gamail.com"]

unique=[]
people= set()

for email in emails:
    if email not in people:
        unique.append(email)
    people.add(email)

print(unique)
print(people)