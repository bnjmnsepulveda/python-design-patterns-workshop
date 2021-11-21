from model.car import Car


def ferrari_objectmother(name='Ferrari', model='365 California GT', country='italy', color='red'):
    return Car(name=name, model=model, country=country, color=color)


def tesla_cars_objectmother(name='Tesla', model='Model S', country='EEUU', color='black'):
    return Car(name=name, model=model, country=country, color=color)
