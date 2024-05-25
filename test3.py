from pykeepass import PyKeePass

kp = PyKeePass('db.kdbx', password='somePassw0rd')

entries = kp.find_entries(title='gmail')

# multi-element return is a list of <class 'pykeepass.entry.Entry'>

print(type(entries))
print(entries)

print("----------")

for entry in entries:
  print(type(entry))
  print("title:", entry.title)
  print("username:",entry.username)
  print("password:",entry.password)
  print("url:",entry.url)
  print("notes:",entry.notes)
  print("-----")