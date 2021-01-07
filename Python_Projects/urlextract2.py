from urllib.request import urlopen


page=urlopen(input("Enter your URL here: "))
sourcecode=page.read()
print(sourcecode)
