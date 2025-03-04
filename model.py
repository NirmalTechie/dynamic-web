import os

def greet_user(name):
    """Function to greet the user."""
    return f"Hello, {name}! Welcome to Python Basics."

def calculate_sum(a, b):
    """Function to add two numbers."""
    return a + b

def write_to_file(filename, content):
    """Function to write content to a file."""
    try:
        with open(filename, "w") as file:
            file.write(content)
        print(f"✅ Data written to {filename}")
    except Exception as e:
        print(f"❌ Error writing to file: {e}")

def read_from_file(filename):
    """Function to read content from a file."""
    if os.path.exists(filename):
        with open(filename, "r") as file:
            return file.read()
    else:
        return "❌ File not found."

# 🚀 Main Execution
if __name__ == "__main__":
    # User Input
    name = input("Enter your name: ")
    print(greet_user(name))

    # Simple Calculation
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"Sum: {calculate_sum(num1, num2)}")
    except ValueError:
        print("❌ Invalid number input.")

    # File Handling
    filename = "sample.txt"
    content = "This is a basic Python program demonstrating core features."
    
    write_to_file(filename, content) 
    print("\n📄 File Content:")
    print(read_from_file(filename))
