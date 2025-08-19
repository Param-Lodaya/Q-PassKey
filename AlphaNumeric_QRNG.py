import qiskit
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram, circuit_drawer, plot_state_city
import numpy as np

characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz@#!$%^&*?_'

def generate_qchar():
 theta = np.random.uniform(0,np.pi)
 phi = np.random.uniform(0,2*np.pi)
 circuit = QuantumCircuit(1,1)
 circuit.ry(theta,0)
 circuit.rz(phi,0)
 circuit.save_statevector()
 simulator = AerSimulator(method='statevector')
 compiled_circuit = transpile(circuit,simulator)
 job = simulator.run(compiled_circuit, shots=1)
 result = job.result()
 state = result.get_statevector(compiled_circuit)
 alpha , beta = state[0],state[1]
 prob_1 =np.abs(beta)**2
 index = int(prob_1*len(characters))%len(characters)
 return characters[index]

def generate_string(n_qubits):
 q_string = ''.join(generate_qchar() for _ in range(n_qubits))
 
 return q_string
 
def char_to_bit(char):
 try:
       index = characters.index(char)
       return format(index, '08b')
 except ValueError:
       print("Character not in the set.")
       return '00000000' 

def bit_conversion(text):
 bits = []
 for char in text:
  bits.extend([int(b) for b in format(ord(char), '08b')])
 return bits

def bits_to_password(bit_list):
    final_pass = ""
    n = len(bit_list)
    for i in range(0, n, 8):
        chunk_bits = bit_list[i:i + 8]
        chunk_str = ''.join(str(b) for b in chunk_bits)
        if len(chunk_str) == 8:
            index = int(chunk_str, 2)
            if 0 <= index < len(characters):
                final_pass += characters[index]
            else:
                index = index % len(characters)
                final_pass += characters[index]
        elif len(chunk_str) > 0:
            print(f"Warning: Incomplete 8-bit chunk: {chunk_str}")
    return final_pass

if __name__ == "__main__":
 try:
       n = int(input("Enter length of password: "))
       password = generate_string(n)
       password_bits = bit_conversion(password)
       print("Alphanumeric QRNG Password is:",''.join(password))
       print("Bit conversion of the password is:", password_bits)
 except ValueError:
       print("Enter vaild positive integer!")