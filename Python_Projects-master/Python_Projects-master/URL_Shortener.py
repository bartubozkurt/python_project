import pyshorteners
url = input("Enter your Url: ")
s = pyshorteners.Shortener().tinyurl.short(url)
print("Your  shorted url is --> ",s)
