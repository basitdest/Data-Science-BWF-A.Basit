class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

restaurant1 = Restaurant("The Food Place", "Italian")
restaurant2 = Restaurant("Sushi World", "Japanese")
restaurant3 = Restaurant("Spice Haven", "Indian")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
