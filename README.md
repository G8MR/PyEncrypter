# PyEncrypter
PyEncrypter is a simple yet safe Python encryption/decryption library. In some time, the main release will be officialy published.

<br>

## Installation
All you need to do is just type the following code in your terminal to install, or you could copy and paste it as well.
```bash
pip install PyEncrypter
```
If it doesn't work, you could try the following:
```bash
python.exe -m pip install --user PyEncrypter
```
## Commands
```python
#Importing the package
import PyEncrypter
#Initializing the object
variable = PyEncrypter.ObjInit()
#Encryption command
variable.encrypt(data)
#Decryption command
variable.decrypt(data)
```
<br>
Note: It is strongly advisable to delete the object after usage of the command by the "del variable" command.
<br>

## Examples for usage
```python
import PyEncrypter
var = input("Enter your message: ")
secret_code = PyEncrypter.ObjInit()
secret_code.encrypt(var)
print("Your secret code is", secret_code)
del secret_code

var2 = input("Enter secret code: ")
message = PyEncrypter.ObjInit()
message.decrypt(var2)
print("Your message is", message)
del message
```
