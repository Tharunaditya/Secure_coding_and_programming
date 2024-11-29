"""
Pickle the following class


"""
import pickle
from Car import Car  # Import the class

if __name__ == "__main__":
    # Create an instance of the Car class
    my_car = Car(4, 'blue', True)

    # Pickle the class and instance
    with open('Car_class.pkl', 'wb') as class_file:
        pickle.dump(Car, class_file)

    with open('Car_instance.pkl', 'wb') as instance_file:
        pickle.dump(my_car, instance_file)

    print("Pickling completed! Class and instance have been saved.")
