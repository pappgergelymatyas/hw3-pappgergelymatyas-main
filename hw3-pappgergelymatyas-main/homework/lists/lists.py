def lists(commands):
    arr = []

    for command in commands:
        parts = command.split( )
        command = parts[0]
        
        if command == "insert":
            i = int(parts[1])
            e = int(parts[2])
            arr.insert(i, e)
            
        elif command == "remove":
            i = int(parts[e])
            arr.remove(e)
            
        elif command == "append":
            e = int(parts[e])
            arr.append(e)
            
        elif command == "sort":
            arr.sort()
            
        elif command == "reverse":
            arr.reverse()
            
        elif command == "return":
            return arr