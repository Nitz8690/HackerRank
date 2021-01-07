from googlesearch import search
query=input("Search Your Query Here: ")
for i in search(query,start=0,pause=2,stop=5):
    print(i)
