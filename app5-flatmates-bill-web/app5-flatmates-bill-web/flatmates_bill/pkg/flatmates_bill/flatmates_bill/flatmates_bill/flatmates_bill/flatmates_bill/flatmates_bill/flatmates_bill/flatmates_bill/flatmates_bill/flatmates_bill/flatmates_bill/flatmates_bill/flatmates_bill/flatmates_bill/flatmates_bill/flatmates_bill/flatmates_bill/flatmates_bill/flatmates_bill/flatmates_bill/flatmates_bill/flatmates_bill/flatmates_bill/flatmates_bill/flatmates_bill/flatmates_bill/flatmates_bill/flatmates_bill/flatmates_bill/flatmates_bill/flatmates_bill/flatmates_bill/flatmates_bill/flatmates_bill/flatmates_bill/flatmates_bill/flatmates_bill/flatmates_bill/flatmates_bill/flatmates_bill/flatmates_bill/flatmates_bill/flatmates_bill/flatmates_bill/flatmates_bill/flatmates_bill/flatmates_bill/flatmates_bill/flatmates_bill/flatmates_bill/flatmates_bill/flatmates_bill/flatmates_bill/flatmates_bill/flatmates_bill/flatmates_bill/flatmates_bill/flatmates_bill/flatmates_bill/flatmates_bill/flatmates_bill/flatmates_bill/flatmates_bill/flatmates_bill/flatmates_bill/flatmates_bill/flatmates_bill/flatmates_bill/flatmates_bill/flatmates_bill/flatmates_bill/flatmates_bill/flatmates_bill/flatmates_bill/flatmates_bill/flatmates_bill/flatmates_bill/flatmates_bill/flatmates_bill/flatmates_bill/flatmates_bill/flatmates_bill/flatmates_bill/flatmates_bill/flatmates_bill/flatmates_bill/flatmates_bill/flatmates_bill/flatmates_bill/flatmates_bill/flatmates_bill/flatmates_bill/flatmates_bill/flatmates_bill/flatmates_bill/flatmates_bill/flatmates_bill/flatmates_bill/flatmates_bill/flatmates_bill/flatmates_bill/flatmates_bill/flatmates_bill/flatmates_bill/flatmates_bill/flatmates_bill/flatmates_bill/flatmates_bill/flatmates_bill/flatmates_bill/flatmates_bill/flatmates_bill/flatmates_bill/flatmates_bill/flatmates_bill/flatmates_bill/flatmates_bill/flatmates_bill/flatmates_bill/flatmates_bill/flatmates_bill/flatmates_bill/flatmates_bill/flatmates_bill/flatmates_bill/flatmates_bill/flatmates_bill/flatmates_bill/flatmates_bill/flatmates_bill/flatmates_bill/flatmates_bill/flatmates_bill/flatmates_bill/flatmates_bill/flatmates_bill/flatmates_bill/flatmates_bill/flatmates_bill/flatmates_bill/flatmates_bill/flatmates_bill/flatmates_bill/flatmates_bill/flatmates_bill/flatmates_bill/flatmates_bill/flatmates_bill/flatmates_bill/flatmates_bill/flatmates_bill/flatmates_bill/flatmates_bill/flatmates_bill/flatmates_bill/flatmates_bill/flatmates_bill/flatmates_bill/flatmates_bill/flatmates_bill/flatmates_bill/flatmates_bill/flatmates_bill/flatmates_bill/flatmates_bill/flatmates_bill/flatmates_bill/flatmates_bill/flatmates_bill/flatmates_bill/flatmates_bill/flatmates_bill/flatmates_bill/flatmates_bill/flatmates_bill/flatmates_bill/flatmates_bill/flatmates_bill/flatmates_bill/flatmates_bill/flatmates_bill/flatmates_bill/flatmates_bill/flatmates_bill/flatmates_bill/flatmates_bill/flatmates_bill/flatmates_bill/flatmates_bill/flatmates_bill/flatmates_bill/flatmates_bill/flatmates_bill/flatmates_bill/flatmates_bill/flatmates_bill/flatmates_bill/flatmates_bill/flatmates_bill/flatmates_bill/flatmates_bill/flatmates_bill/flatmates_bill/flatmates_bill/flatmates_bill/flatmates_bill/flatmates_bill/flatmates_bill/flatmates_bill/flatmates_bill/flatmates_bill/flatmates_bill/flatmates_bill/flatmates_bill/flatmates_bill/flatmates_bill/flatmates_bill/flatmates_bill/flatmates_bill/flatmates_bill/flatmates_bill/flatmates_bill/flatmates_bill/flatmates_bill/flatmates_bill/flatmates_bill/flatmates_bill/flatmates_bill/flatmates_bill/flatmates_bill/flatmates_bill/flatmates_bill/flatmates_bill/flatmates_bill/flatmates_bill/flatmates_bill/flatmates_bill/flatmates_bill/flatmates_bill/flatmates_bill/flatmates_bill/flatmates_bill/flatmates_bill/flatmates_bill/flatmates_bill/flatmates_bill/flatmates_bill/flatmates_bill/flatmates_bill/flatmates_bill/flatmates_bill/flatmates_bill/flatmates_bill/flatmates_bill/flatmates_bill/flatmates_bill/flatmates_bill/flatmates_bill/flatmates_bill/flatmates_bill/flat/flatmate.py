class Flatmate:
    """
    Contains information about flatmates who share the bill,
    including name and days in house
    """
    def __init__(self, name: str, days = 30) -> None:
        self.name = name
        self.days = days
