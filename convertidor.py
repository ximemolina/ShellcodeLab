def hex_a_shellcode(hex_str):
    """
    Convierte un string de código máquina en hexadecimal (ej. "4831c050")
    al formato de bytes escapados usado en exploits (ej. "\\x48\\x31\\xc0\\x50").
    """
    # Elimina espacios, saltos de línea, "0x", comas, etc.
    hex_str = hex_str.replace(" ", "").replace("\n", "")
    hex_str = hex_str.replace("0x", "").replace(",", "").replace("\\x", "")

    if len(hex_str) % 2 != 0:
        raise ValueError("La cadena hexadecimal tiene un número impar de caracteres.")

    bytes_list = [hex_str[i:i+2] for i in range(0, len(hex_str), 2)]
    formateado = "".join(f"\\x{b}" for b in bytes_list)
    return formateado


if __name__ == "__main__":
    entrada = input("Ingresa el código máquina en hex: ").strip()
    try:
        resultado = hex_a_shellcode(entrada)
        print("\nResultado:")
        print(resultado)
    except ValueError as e:
        print(f"Error: {e}")
