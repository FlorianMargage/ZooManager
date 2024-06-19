import unittest
from Zoo import ZooManager, Enclosure, Animal, Visit
from datetime import datetime


class TestZooManager(unittest.TestCase):

    def setUp(self):
        self.zoo_manager = ZooManager()
        self.enclosure1 = Enclosure(1, "Lion's Den", "large", ["lion"])
        self.animal1 = Animal(1, "Simba", "lion", 5, None)

    def test_add_animal(self):
        self.zoo_manager.add_animal(self.animal1)
        self.assertIn(1, self.zoo_manager.animals)

    def test_update_animal(self):
        self.zoo_manager.add_animal(self.animal1)
        self.zoo_manager.update_animal(1, name="Nala")
        self.assertEqual(self.zoo_manager.animals[1].name, "Nala")

    def test_delete_animal(self):
        self.zoo_manager.add_animal(self.animal1)
        self.zoo_manager.delete_animal(1)
        self.assertNotIn(1, self.zoo_manager.animals)

    def test_add_enclosure(self):
        self.zoo_manager.add_enclosure(self.enclosure1)
        self.assertIn(1, self.zoo_manager.enclosures)

    def test_add_animal_to_enclosure(self):
        self.zoo_manager.add_enclosure(self.enclosure1)
        self.zoo_manager.add_animal(self.animal1)
        self.enclosure1.add_animal(self.animal1)
        self.assertIn(self.animal1, self.enclosure1.animals)

    def test_delete_enclosure_with_animals(self):
        self.zoo_manager.add_enclosure(self.enclosure1)
        self.zoo_manager.add_animal(self.animal1)
        self.enclosure1.add_animal(self.animal1)
        with self.assertRaises(ValueError):
            self.zoo_manager.delete_enclosure(1)

    def test_add_visit(self):
        visit = Visit(1, datetime.now().date(), datetime.now(
        ).time(), datetime.now().time(), [self.enclosure1])
        self.zoo_manager.add_visit(visit)
        self.assertIn(1, self.zoo_manager.visits)

    def test_add_visit_with_more_than_5_enclosures(self):
        with self.assertRaises(ValueError):
            Visit(1, datetime.now().date(), datetime.now().time(),
                  datetime.now().time(), [self.enclosure1]*6)


if __name__ == "__main__":
    unittest.main()
