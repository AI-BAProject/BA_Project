import time

class WasteManagementDrone:
    def _init_(self):
        self.battery_level = 100
        self.current_location = (0, 0)
        self.waste_collection_capacity = 0
        self.is_busy = False

    def move_to_location(self, destination):
        # Simulate drone movement to the destination
        time.sleep(2)  # Sleep for 2 seconds to simulate movement
        self.current_location = destination

    def collect_waste(self, waste_amount):
        # Simulate waste collection
        if self.is_busy:
            print("Drone is already busy. Cannot collect waste.")
            return

        if self.battery_level < 20:
            print("Low battery. Returning to base.")
            self.return_to_base()
            return

        self.is_busy = True
        time.sleep(3)  # Simulate waste collection for 3 seconds
        self.waste_collection_capacity += waste_amount
        self.is_busy = False

    def return_to_base(self):
        # Simulate returning to base for recharging
        self.move_to_location((0, 0))  # Return to the base (0, 0)
        self.battery_level = 100
        print("Drone has returned to base and recharged.")

    def display_status(self):
        print(f"Location: {self.current_location}")
        print(f"Battery Level: {self.battery_level}%")
        print(f"Waste Collection Capacity: {self.waste_collection_capacity} kg")

# Create a Waste Management Drone instance
drone = WasteManagementDrone()

# Simulate drone operations
drone.move_to_location((10, 10))
drone.collect_waste(5)
drone.display_status()
