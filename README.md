# PyEncrypter
PyEncrypter is a simple yet safe Python encryption package. It is still developing, and the encryption level is 1 as of now. I have planned to bring the final encryption level upto 3, which could take some time.

<br>

## Installation
All you need to do is just type the following code in your terminal to install, or you could copy and paste it as well.
```bash
pip install PyEncrypter
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
Note: It is strongly advisable to delete the object after usage of command by the "del variable" command.
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
