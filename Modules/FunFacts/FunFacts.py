import random


def funfacts(region=None):
    general_facts = [
        "Honey never spoils.",
        "Bananas are berries, but strawberries aren't.",
        "Octopuses have three hearts.",
        "A day on Venus is longer than a year on Venus.",
        "The Eiffel Tower can be 15 cm taller during the summer.",
        "A group of flamingos is called a 'flamboyance'.",
        "Humans share about 60% of their DNA with bananas."
    ]
    texas_facts = [
        "Texas was once its own country.",
        "The King Ranch is bigger than Rhode Island.",
        "Dr Pepper was invented in Texas."
    ]
    facts = texas_facts if region == "Texas" else general_facts
    fact = random.choice(facts)
    index = facts.index(fact) + 1
    return fact, index


if __name__ == "__main__":
    fact, index = funfacts()
    print(f"Fun Fact #{index}: {fact}")
