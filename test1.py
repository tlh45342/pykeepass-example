from pykeepass import PyKeePass

kp = PyKeePass('db.kdbx', password='somePassw0rd')

# find any group by its name
group = kp.find_groups(name='General', first=True)

print(group)