#calculate the person age
def calculate_age(year_born):
    """
    Calculate the age of a person based on the year born.
    """
    import datetime
    current_year = datetime.datetime.now().year
    age = current_year - year_born
    return age

def main():
    """
    Main function to get user input and display the calculated age.
    """
    year_born = int(input("Enter the year you were born: "))
    age = calculate_age(year_born)
    print(f"You are {age} years old.")
    