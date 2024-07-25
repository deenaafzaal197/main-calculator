
import streamlit as st

# Dummy modules to simulate the operations
class sum:
    @staticmethod
    def addition(a, b):
        return a + b

class multiplication:
    @staticmethod
    def multiply(a, b):
        return a * b

class subtraction:
    @staticmethod
    def subtract(a, b):
        return a - b

class division:
    @staticmethod
    def division(a, b):
        if b != 0:
            return a / b
        else:
            return "Cannot divide by zero"
def main():
    st.title("Simple Calculator")

    option = st.selectbox(
        "Select an operation",
        ("Addition", "Subtraction", "Multiplication", "Division")
    )

    a = st.number_input("Enter number 1", value=0)
    b = st.number_input("Enter number 2", value=0)

    if st.button("Calculate"):
        if option == "Addition":
            result = sum.addition(a, b)
            st.write(f"The result of addition is {result}")

        elif option == "Multiplication":
            result = multiplication.multiply(a, b)
            st.write(f"The result of multiplication is {result}")

        elif option == "Subtraction":
            result = subtraction.subtract(a, b)
            st.write(f"The result of subtraction is {result}")

        elif option == "Division":
            result = division.division(a, b)
            st.write(f"The result of division is {result}")

if __name__ == "__main__":
    main()
