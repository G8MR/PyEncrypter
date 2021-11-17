# PyEncrypter
A simple yet safe Python encryption package. It is still developing, and the encryption level is 1 as of now. I have planned to bring the final encryption level upto 3.

<br>
<br>

## Installation
Just type the following code in your terminal to install, or you could copy and paste it as well.
```bash
pip install PyEncrypter
```
## Commands
```python
#Encryption command
variable = encrypt("data_goes_here")

#Decrypting command
variable = decrypt("data goes here")
```
<br>

## Examples for usage
```python
var = input("Enter your message: ")
secret_code = encrypt(var)
print("Your secret code is", secret_code)

var2 = input("Enter secret code: ")
message = decrypt(var2)
print("Your message is", message)
```
