def calculate_dot_product_3(vector1, vector2, vector3):
    """Calculate and return the dot product of three vectors."""
    if len(vector1) != len(vector2) or len(vector2) != len(vector3):
        raise ValueError("All vectors must be of the same length to compute the dot product.")

    dot_product = sum(v1 * v2 * v3 for v1, v2, v3 in zip(vector1, vector2, vector3))
    return dot_product


def get_vector_input(prompt):
    """Prompt the user to enter a vector and return it as a list of integers."""
    try:
        vector = list(map(int, input(prompt).split()))
    except ValueError:
        raise ValueError("Please enter a list of integers separated by spaces.")
    return vector


def main():
    print("Dot Product Calculator for Three Vectors")

    # Get vector inputs from the user
    vector1 = get_vector_input("Enter the first vector (space-separated integers): ")
    vector2 = get_vector_input("Enter the second vector (space-separated integers): ")
    vector3 = get_vector_input("Enter the third vector (space-separated integers): ")

    try:
        result = calculate_dot_product_3(vector1, vector2, vector3)
        print(f"The dot product of {vector1}, {vector2}, and {vector3} is: {result}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
