def megszamlalas():
    db = 0
    for i in range (10, 100, 1):
        if i % 2 == 0:
            db += 1
    print(db)