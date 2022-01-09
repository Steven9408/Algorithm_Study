while True:
    try:
        n = int(input())
        if n == 1:
            print(1)
            continue
        res = 1
        sol = 1
        while True:
            res = res*10 + 1
            sol += 1
            if res%n == 0:
                break
        print(sol)

    except:
        break