class Animal:
    def __init__(self, animal_id, name, species, age, enclosure):
        self.animal_id = animal_id
        self.name = name
        self.species = species
        self.age = age
        self.enclosure_id = enclosure


class Enclosure:
    def __init__(self, enclosure_id, name, size, species_allowed):
        self.enclosure_id = enclosure_id
        self.name = name
        self.size = size
        self.species_allowed = species_allowed
        self.animals = []

    def add_animal(self, animal):
        if animal.species in self.species_allowed:
            self.animals.append(animal)
            animal.enclosure = self
        else:
            raise ValueError(
                f"l'espèce {animal.species} n'est pas autorisée dans cet enclos")

    def remove_animal(self, animal):
        self.animals.remove(animal)


class Visit:
    def __init__(self, visit_id, date, start_time, end_time, enclosures):
        if len(enclosures) > 5:
            raise ValueError(
                "Un maximum de 5 enclos peut être visité en une seule visite")
        self.visit_id = visit_id
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.enclosures = enclosures


class ZooManager:
    def __init__(self):
        self.animals = {}
        self.enclosures = {}
        self.visits = {}

    def add_animal(self, animal):
        self.animals[animal.animal_id] = animal

    def update_animal(self, animal_id, **kwargs):
        animal = self.animals.get(animal_id)
        if animal:
            for key, value in kwargs.items():
                setattr(animal, key, value)

    def delete_animal(self, animal_id):
        animal = self.animals.pop(animal_id, None)
        if animal:
            enclosure = self.enclosures.get(animal.enclosure_id)
            if enclosure:
                enclosure.remove_animal(animal)

    def add_enclosure(self, enclosure):
        self.enclosures[enclosure.enclosure_id] = enclosure

    def update_enclosure(self, enclosure_id, **kwargs):
        enclosure = self.enclosures.get(enclosure_id)
        if enclosure:
            for key, value in kwargs.items():
                setattr(enclosure, key, value)

    def delete_enclosure(self, enclosure_id):
        enclosure = self.enclosures.get(enclosure_id)
        if enclosure and not enclosure.animals:
            del self.enclosures[enclosure_id]
        else:
            raise ValueError(
                "Vous ne pouvez pas supprimer un enclos avec des animaux à l'intérieur")

    def add_visit(self, visit):
        self.visits[visit.visit_id] = visit

    def update_visit(self, visit_id, **kwargs):
        visit = self.visits.get(visit_id)
        if visit:
            for key, value in kwargs.items():
                setattr(visit, key, value)

    def delete_visit(self, visit_id):
        self.visits.pop(visit_id, None)
