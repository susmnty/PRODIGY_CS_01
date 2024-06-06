# PRODIGY_CS_01
Here the Task given by Prodigy - 

Implementing Caser Cipher - which works as Encryption and Decryption by using shift value to perform here by using the Python Program the code.

For more information for Caesar Chip - https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/ 
to know where its used and how the basic knowledge for it in the link above.

The provided Caesar Cipher program is designed to encrypt and decrypt text based on a user-specified shift value. It consists of two primary functions: encrypt and decrypt. 
The encrypt function shifts each letter in the input text by a specified amount, preserving the case of each letter and leaving non-alphabetic characters unchanged. 
For alphabetic characters, it calculates the new character by converting it to a zero-based index, applying the shift with modulo arithmetic to ensure it wraps around within the alphabet, and then converting it back to a character. 
The decrypt function simply calls the encrypt function with the negative of the shift value, effectively reversing the encryption process.

The main function manages the user interface, repeatedly prompting the user to choose whether they want to encrypt or decrypt a message, enter the message, and provide a shift value. It ensures the shift value is an integer and handles invalid inputs. After processing the message, it displays the result and asks if the user wants to continue with another message. The program continues this loop until the user decides to exit. By incorporating input validation and handling both uppercase and lowercase letters, the program provides a robust and user-friendly implementation of the Caesar Cipher.


