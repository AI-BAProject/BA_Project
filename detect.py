import cv2
import numpy as np
import drone_api 
import path_planning 
import database  
import user_interface

# Initialize the drone
drone = drone_api.initialize()

# Main loop
while True:
    # Capture an image from the drone's camera
    image = drone.get_camera_image()

    # Process the image to detect waste using OpenCV or a deep learning model
    detected_waste = cv2.detectWaste(image)

    # Plan a path to collect detected waste
    waste_locations = path_planning.plan_path(detected_waste)

    # Fly the drone to the waste locations
    for location in waste_locations:
        drone.fly_to(location)

        # Collect waste and update the database
        collected_waste = drone.collect_waste(location)
        database.update(collected_waste)

    # Update the user interface with drone status and waste data
    user_interface.update(drone.get_status(), database.get_waste_data())

    # Check for user commands from the UI and execute them
    user_command = user_interface.get_command()
    if user_command == "emergency_stop":
        drone.emergency_stop()

# Function to analyze waste data and calculate statistics
def analyze_waste_data(waste_data):
    # Calculate the total weight of collected waste
    total_weight = sum(waste['weight'] for waste in waste_data)

    # Calculate the number of waste items collected
    num_items_collected = len(waste_data)

    # Calculate the average weight per waste item
    average_weight_per_item = total_weight / num_items_collected if num_items_collected > 0 else 0

    # Calculate the most common waste type
    waste_types = [waste['type'] for waste in waste_data]
    most_common_waste_type = max(set(waste_types), key=waste_types.count) if waste_types else None

    # Print the statistics
    print(f"Total Weight of Collected Waste: {total_weight} grams")
    print(f"Number of Waste Items Collected: {num_items_collected}")
    print(f"Average Weight per Waste Item: {average_weight_per_item} grams")
    print(f"Most Common Waste Type: {most_common_waste_type}")

# Retrieve waste data from the database
waste_data = database.get_waste_data()

# Analyze the collected waste data
analyze_waste_data(waste_data)

# Close the drone connection and cleanup
drone.disconnect()
