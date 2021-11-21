from patterns.objectmother import ferrari_objectmother


def main():

    benjamin_garage = [
        ferrari_objectmother(color='white'),
        ferrari_objectmother(color='green'),
        ferrari_objectmother(model='308 gtsi', color='blue'),
        ferrari_objectmother(model='308 gtsi', color='green'),
        ferrari_objectmother(model='308 gtsi', color='purple'),
        ferrari_objectmother(model='328 GTS'),
        ferrari_objectmother(model='3.2 Mondial GT'),
        ferrari_objectmother(model='F40 GT'),
        ferrari_objectmother(model='348 Spider'),
    ]

    for car in benjamin_garage:
        print('My awesome car is: %s' % car)


if __name__ == "__main__":
    main()