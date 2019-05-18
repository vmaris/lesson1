a = {
    "city": "Moscow", 
    "temperature": 20
    }
print(a['city'])
# Short for operation with variance
a["temperature"] -= 5 
print(a["temperature"])
print(a.get("country","not found"))
print(a.get("country","Russia"))
a["date"] = "27.05.2019"
print(a)
print(len(a))
