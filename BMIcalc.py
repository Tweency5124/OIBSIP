def calculate_bmi(weight, height):
    """Calculates the Body Mass Index (BMI) from weight and height."""
    return weight / (height ** 2)

def classify_bmi(bmi):
    """Classifies BMI into categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def main():
    """Main function to run the BMI calculator."""
    print("Welcome to the BMI Calculator!")
    
    try:
        weight = float(input("Please enter your weight in kilograms: "))
        height = float(input("Please enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive values.")
            return
        
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"Your BMI category is: {category}")
    
    except ValueError:
        print("Error: Invalid input. Please enter numerical values for weight and height.")

if __name__ == "__main__":
    main()
