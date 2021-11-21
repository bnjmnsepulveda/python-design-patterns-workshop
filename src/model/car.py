class Car:

    def __init__(self, name, model, country, color):
        self.name = name
        self.model = model
        self.country = country
        self.color = color


    def __str__(self):
        return 'Car(name="%s",model="%s",country="%s",color="%s")' % (
            self.name,
            self.model,
            self.country,
            self.color
        )
