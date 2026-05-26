# rec2_9.py — Handle exceptions for division of a given numer by user inputed denominator.

def div_by_input():
    denom = float(input("Enter a number to divide 9 by: "))
    result= 9 / denom
    return denom, result
       

def main():
    try:
      denom, result =div_by_input()  
    except ZeroDivisionError:
        print("An exception occurred: Division by zero is not allowed. Please provide a non-zero number.")
        main()  # Retry
    except ValueError:
        print("An exception occurred: invalid numeric input.")
    else:
        print(f"9 / {denom} = {result}")

if __name__ == "__main__":
    main()

#main()