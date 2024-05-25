from pykeepass import PyKeePass

kp = PyKeePass('db.kdbx', password='somePassw0rd')

entry = kp.find_entries(title='gmail', first=True)

# First singular entry is of type <class 'pykeepass.entry.Entry'>

print("entry type:",type(entry))
print(entry)

print("class of password:",type(entry.password))
print("password",entry.password)

print("class of notes:",type(entry.notes))
print("notes:",entry.notes)