import pickle
from Car import Car  # Import the class

if __name__ == "__main__":
    try:
        # Load the pickled Car class
        with open('Car_class.pkl', 'rb') as class_file:
            Car = pickle.load(class_file)

        # Load the pickled Car instance
        with open('Car_instance.pkl', 'rb') as instance_file:
            my_car = pickle.load(instance_file)

        print("Successfully loaded pickled class and instance!")

        # Create a new instance using the loaded class
        new_car = Car(2, "green", False)
        print(f"New car created: Color={new_car.color}, Tires={new_car.num_tires}, Gas={new_car.is_gas()}")

        # Interact with the unpickled instance
        print(f"Loaded car instance details: Color={my_car.color}, Tires={my_car.num_tires}, Gas={my_car.is_gas()}")
        print("Honking horn of the loaded car:")
        my_car.honk_horn()

    except FileNotFoundError as e:
        print(f"File not found: {e}. Ensure the files exist in the same directory.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
