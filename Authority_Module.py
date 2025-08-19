import AlphaNumeric_QRNG as ANQ
import BB84_Protocol as BBP

def pass_generation():
 try:
       n = int(input("Enter length of generation: "))
       raw_password = ANQ.generate_string(n)
       raw_password_bits = ANQ.bit_conversion(raw_password)
       print("Alphanumeric random generation:",''.join(raw_password))
       print("Bit conversion of the generation is:", raw_password_bits)
 except ValueError:
       print("Enter vaild positive integer!")
 else:
        shared_key, _ = BBP.sharing(raw_password_bits)
        shared_key_str = ''.join(map(str, shared_key))
        shared_password = ANQ.bits_to_password(shared_key_str)
        print("\nFinal common Password is:", shared_password)
        with open("Generated_Final_PassKey.txt","w") as f:
                 f.write(shared_password)

if __name__ == "__main__":
 pass_generation()
