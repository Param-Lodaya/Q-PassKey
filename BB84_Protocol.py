import qiskit
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from qiskit.visualization import plot_histogram
import random


def encoding(bit, bases):
 circuit =QuantumCircuit(1,1)
 if bit ==1:
  circuit.x(0)
 if bases ==1:
  circuit.h(0)
 return circuit

def sharing(password):
 num = len(password)
 sender_bits = [int(bit) for bit in password]
 sender_bases = [random.randint(0,1) for _ in range(num)]
 reciever_bases = [random.randint(0,1) for _ in range(num)]
 reciever_bits = []
 shared_key = []
 for s_bit, s_base, r_base in zip(sender_bits, sender_bases, reciever_bases):
  if s_base == r_base:
   reciever_bits.append(s_bit)
   shared_key.append(s_bit)
  else:
          reciever_bits.append(random.randint(0,1))


 remainder = len(shared_key)%8
 if remainder != 0:
  padding_needed = 8 - remainder
  shared_key.extend([0]*padding_needed)

 print("\nSender  Bits:", sender_bits)
 print("\nReceiverBits:", reciever_bits)
 print("\nSender  Basis:", sender_bases)
 print("\nReceiverBasis:", reciever_bases)
 print("\nBB84 shared key (bits):", shared_key)
 return shared_key, []
