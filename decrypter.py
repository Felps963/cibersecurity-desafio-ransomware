import os
import pyaes

def descriptografar():
  try:
    file_name= "teste.txt.ransomwaretroll"
    key = b"testeransomwares"

    if not os.path.exists(file_name):
      print(f" -- Erro: O arquivo {file_name} não foi encontrado.")
      return 
    with open(file_name, "rb") as file:
      file_data = file.read()

        aes = pyaes.AESModeOfOperationCTR(key)
        decrypt_data = aes.decrypt(file_data)

        os.remove(file_name)
      
        new_file_name = "teste.txt"
        with open(new_file_name, "wb") as new_file:
            new_file.write(decrypt_data)

        print(f"-- Arquivo '{file_name}' recuperado com sucesso para '{new_file_name}'")

    except Exception as e:
        print(f"-- Erro na descriptografia: {e}")

if __name__ == "__main__":
    descriptografar()
