def don():
    yield "homer: D,oh!"
    yield "lisa: D,oh!"
    yield "marge: D,oh!"

if __name__ == '__main__':
    for i in don():
        print(i)

    print()

    generator_obj = don()
    print(next(generator_obj))
    print(next(generator_obj))
    print(next(generator_obj))