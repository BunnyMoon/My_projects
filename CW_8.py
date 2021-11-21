def introduction(first_name, last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

# Call the function here.
introduction("James", "Doe")

introduction("Henry")
introduction(first_name="William")

def introduction1(first_name="John", last_name="Smith"):
    print("Hello, my name is", first_name, last_name)

introduction1()
introduction1(last_name="Hopkins")
