class Smartphone:
    def __init__(self, brand, model, price):
        """Initialize the smartphone with brand, model, and price."""
        self.brand = brand
        self.model = model
        self.price = price

    def make_call(self, number):
        """Simulate making a call."""
        return f"Calling {number} from {self.model}..."

    def send_message(self, number, message):
        """Simulate sending a message."""
        return f"Sending message to {number}: {message}"

    def get_info(self):
        """Return smartphone details."""
        return f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}"


class Smartwatch(Smartphone):
    def __init__(self, brand, model, price, battery_life):
        """Initialize the smartwatch with additional battery life attribute."""
        super().__init__(brand, model, price)
        self.battery_life = battery_life

    def track_steps(self, steps):
        """Simulate step tracking."""
        return f"{self.model} tracked {steps} steps today!"

    def get_info(self):
        """Override to include battery life."""
        return f"Brand: {self.brand}, Model: {self.model}, Price: ${self.price}, Battery Life: {self.battery_life} hours"


# Example usage
if __name__ == "__main__":
    phone = Smartphone("Apple", "iPhone 14", 999)
    watch = Smartwatch("Samsung", "Galaxy Watch 5", 299, 48)

    print(phone.get_info())
    print(phone.make_call("123-456-7890"))
    print(watch.get_info())
    print(watch.track_steps(5000))







