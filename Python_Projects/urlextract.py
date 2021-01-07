from urllib.request import urlopen


page=urlopen(input("Enter or paste your url Here: "))
print(page.headers)
