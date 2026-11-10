from pyscript import display, document

def get_non_metal_info(e):

    document.getElementById('output').innerHTML = "" 
    elementsymbol = document.getElementById('elementInput').value.strip()

    non_metal_data = {
        "H": ("Hydrogen", 1, 1.008),
        "He": ("Helium", 2, 4.0026),
        "C": ("Carbon", 6, 12.011),
        "N": ("Nitrogen", 7, 14.007),
        "O": ("Oxygen", 8, 16.00),
        "F": ("Fluorine", 9, 19.00),
        "Ne": ("Neon", 10, 20.18),
        "P": ("Phosphorus", 15, 30.97),
        "S": ("Sulfur", 16, 32.07),
        "Cl": ("Chlorine", 17, 35.45),
        "Ar": ("Argon", 18, 39.95),
        "Se": ("Selenium", 34, 78.96),
        "Br": ("Bromine", 35, 79.90),
        "Kr": ("Krypton", 36, 83.80),
        "I": ("Iodine", 53, 126.90),
        "Xe": ("Xenon", 54, 131.29),
        "Rn": ("Radon", 86, 222.00),
        "Ts": ("Tennessine", 117, 294.00),
        "Og": ("Oganesson", 118, 294.00)
    }

    # Check
    if elementsymbol in non_metal_data:
        data = non_metal_data[elementsymbol]
        result_message = (
            f"{elementsymbol} is a non-metal! Name: {data[0]}, Atomic Number: {data[1]}, Atomic Mass: {data[2]} u"
        )
    else:
        result_message = f"Sorry, '{elementsymbol}' is not a registered non-metal symbol."

    # 5. Display the message inside the target div (Indented inside the function)
    display(result_message, target="output")
