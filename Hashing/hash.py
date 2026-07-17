# Using list
# Time complexity O(n)
emails=["vaibhavi811@gmail.com","renubansal173@gmail.com", "anant2709@gmail.com"]

def find_email(emails,target):
    for email in emails:
        if target==email:
            return "Email Found"
    return "Not Found"

print(find_email(emails, "renubansal173@gmail.com"))

# using dictionary
# Time complexity O(1)
username={"Vaibhavi08":"vaibhavi811@gmail.com", "Renu17":"renubansal173@gmail.com","Anant27":"anant2709@gmail.com"}

print("Vaibhavi08" in username)

# Using Set
# Time complexity O(1)
people=set()

people.add("vaibhavi811@gmail.com")
people.add("renubansal173@gmail.com")
people.add( "anant2709@gmail.com")

print(people)

print( "anant2709@gmail.com" in people)