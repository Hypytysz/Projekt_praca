# Status online, offline

def count_status():
    online = 0
    offline = 0
    niezydentyfikowany = 0
    for i in statuses:
        if statuses[i] == "online":
           online += 1
        elif statuses[i] == "offline":
            offline += 1
        else:
            niezydentyfikowany += 1
    print(f"Obecnie aktywnych użytkowników: {online}, użytkownicy offline: {offline}, niezidentyfikowany status: {niezydentyfikowany}.")


statuses = {
"Alice": "online",
"Bob": "offline",
"Eve": "online",
"Charlie": "offline",
"Simon": "online",
"Edward": "online",
"Sahra" : "offline",
"Charlotte": "xxx",
}

count_status()