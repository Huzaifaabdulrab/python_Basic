try:
    a = 10;
    b = 10;
    result = a / b;
    print(result)
except:
    print("An error occurred")


try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


def divide_number(a,b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    except TypeError:
        print("Both inputs must be numbers!")
    else:
        print(f"Division Succesful. result {result}")
    finally :
        print("Operation Complete .\n")