def trip_route(item):
    reverseInput ={} 
    for k,v in item.items():
        reverseInput[v] = k
    
    start = None
    
    for k,v in item.items():
        if k not in reverseInput:
            start = k 
            break
    if start == None:
        print("你输入的行程单怕是个假东西")
        return 
    else: 
        to = item[start]
        print(start + "-> "+ to)
        start = to
        to = item[to]

        while to != None:
            print(start + "-> "+ to)
            start = to 
            if to in item: 
                to = item[to]
            else:
                break



if __name__ == "__main__":
    item = {}
    item["北京"] = "上海"
    item["上海"] = "大连"
    item["西安"] = "成都" 
    item["大连"] = "西安" 
    
    trip_route(item)