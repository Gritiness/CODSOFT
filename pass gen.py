import random
import string

def generate_simple_password(length):
  """
  Generates a simple password of the specified length using only characters and digits.

  Args:
      length (int): The desired length of the password (minimum 3 characters).

  Returns:
      str: The generated simple password.
  """

  # Define character sets for alphanumeric characters
  alphanumeric = string.ascii_lowercase + string.ascii_uppercase + string.digits

  # Handle invalid lengths
  if length < 3:
    print("Password length must be at least 3 characters.")
    return None

  # Generate the password with random characters from the alphanumeric set
  password = ''.join(random.choices(alphanumeric, k=length))

  return password

if __name__ == "__main__":
  while True:
    try:
      length = int(input("Enter desired password length (minimum 3 characters): "))
      if length < 3:
        continue
      break
    except ValueError:
      print("Invalid input. Please enter a number.")

  password = generate_simple_password(length)
  if password:  # Check if password was generated successfully
    print("Your generated simple password:", password)

