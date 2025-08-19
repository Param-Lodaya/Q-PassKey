import os
import shutil
import getpass
import msvcrt

def masked_input(prompt=''):
    print(prompt, end='', flush=True)
    password = ''
    while True:
        ch = msvcrt.getch()
        if ch in {b'\r', b'\n'}:  # Enter key
            print('')
            break
        elif ch == b'\x08':  # Backspace
            if len(password) > 0:
                password = password[:-1]
                print('\b \b', end='', flush=True)
        elif ch in {b'\x03', b'\x1a'}:  # Ctrl+C or Ctrl+Z
            raise KeyboardInterrupt
        else:
            try:
                char = ch.decode('utf-8')
                password += char
                print('*', end='', flush=True)
            except:
                pass
    return password.strip()

def read_pass(password_path):
 try:
       with open(password_path, 'r') as file:
              return file.read().strip()
 except FileNotFoundError:
             print("Pass word file not found!")
             return None

def access_control():
 password_file_path = input("\nEnter full path of the password file: ").strip()
 stored_pass = read_pass(password_file_path)

 if not stored_pass:
           print("\nNo password found make sure password generated!")
           return

 entered_pass = masked_input("\nEnter password to access: ")

 if entered_pass == stored_pass:
    print("Access Granted!")
    source = input("\nEnter complete path file to be copied: ").strip()
    destination = input("\nEnter complete path file of destination folder: ").strip()
    try:
          if not os.path.exists(source):
                    print("\nSource file not found!!")
                    return
          if not os.path.exists(destination):
                    os.makedirs(destination)
          shutil.copy(source, destination)
          print("\nFile copied successfully")
    except Exception as e:
            print("\nFailed to copy the file")
 else:
         print("\nIncorrect password access denied!!")

def read_pass(path):
    with open(path, 'r') as file:
        return file.read().strip()

def copy_file(src, dest_folder):
    import shutil, os
    file_name = os.path.basename(src)
    dest_path = os.path.join(dest_folder, file_name)
    shutil.copy(src, dest_path)


if __name__ == "__main__":
       access_control()

