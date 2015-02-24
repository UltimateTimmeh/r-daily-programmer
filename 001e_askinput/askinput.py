# Ask user for information.
person = {}
person['name'] = input("Name? > ")
person['age'] = input("Age? > ")
person['reddit_username'] = input("Reddit Username? > ")

# Format and print output.
out = ("Your name is '{name}', you are {age} years old and your Reddit " +
       "username is '{reddit_username}'.").format(**person)
print(out)

# Append output to file.
with open('output.txt', 'a') as output_file:
    output_file.write(out+'\n')
