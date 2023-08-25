class Person:
    """Personne."""

    def __init__(self, name):
        """Donne un nom."""
        self.name = name
    
    def walk(self):
        """Marche."""
        print(f"{self.name} marche.")


volunteers = [Person("Alice"), Person("Bob"), Person("Carol")]
for volunteer in volunteers:
    volunteer.walk()

# Ici, nous reprenons nos outils !
toolbox = {
    "screwdriver": Screwdriver(50),
    "hammer": Hammer(),
    "nails": [Nail(), Nail(), Nail()],
}