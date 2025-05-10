# from art import logo

# alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# print(logo)

# direction = input("Type encode to 'encrypt' and 'decode' to decrypt: ").lower()
# text = input("\nType your message: ").lower()
# shift = int(input("\nType the shift number: "))
 
# def encrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         ''' num = alphabets.index(letter) + shift --> find index of first letter in the text and add the shift to it (returns int)
#             print(alphabet(num)) --> prints the shifted digit
#             encrypted_string += alphabet(num) --> adds the shifted letter to empty string '''
           
#         shifted_position = alphabets.index(letter) + shift_amount # combined above steps
#         shifted_position %= len(alphabets) # index to 0, once it crosses 25 in this case. Index below 25, eg 4%25, will give 4
#         cipher_text += alphabets[shifted_position]
        
#         ''' In Python, lists and strings are zero-indexed, meaning the first element is at index 0. For a list of length n, 
#             valid indices are from 0 to n-1. If you try to access an index outside this range, Python raises an IndexError.
#             The modulus operator helps by mapping any integer index to a valid index within the range [0, n-1]. '''
#     print(cipher_text)

# def decrypt(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         ''' num = alphabets.index(letter) + shift --> find index of first letter in the text and add the shift to it (returns int)
#             print(alphabet(num)) --> prints the shifted digit
#             encrypted_string += alphabet(num) --> adds the shifted letter to empty string '''
           
#         shifted_position = alphabets.index(letter) - shift_amount # combined above steps
#         shifted_position %= len(alphabets) # index to 0, once it crosses 25 in this case. Index below 25, eg 4%25, will give 4
#         cipher_text += alphabets[shifted_position]
        
#         ''' In Python, lists and strings are zero-indexed, meaning the first element is at index 0. For a list of length n, 
#             valid indices are from 0 to n-1. If you try to access an index outside this range, Python raises an IndexError.
#             The modulus operator helps by mapping any integer index to a valid index within the range [0, n-1]. '''
#     print(cipher_text)

# def caesar(direction):
#     if direction == "encode":
#         encrypt(text, shift)
#     elif direction == "decode":
#         decrypt(text, shift)

# caesar(direction)

##################### better implementation than using two 3 function definitions #####################

from art import logo

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
proceed = "yes"
print(logo)

def caesar(original_text, shift_amount, encode_or_decode):
    
        cipher_text = ""
        # count = 0

        if encode_or_decode == "decode":
            shift_amount *= -1
        # simpler implementation compared to using count
    
        for letter in original_text:
    
            if letter not in alphabets:
                cipher_text += letter
            # else:    
            #     if count > 0:
            #         shift_amount *= 1 # logic fix to not make (- * - = +) from the second execution for decrypt
            #     elif encode_or_decode == "decode":
            #         shift_amount *= -1 # this makes the below line to subtract shift amount if the direction is to decode
                
            shifted_position = alphabets.index(letter) + shift_amount # combined above steps
            shifted_position %= len(alphabets) # index to 0, once it crosses 25 in this case. Index below 25, eg 4%25, will give 4
            cipher_text += alphabets[shifted_position]
                # count += 1
    
        print(f"\nHere is the {encode_or_decode}d text: {cipher_text}")
        print("\n############################## [END] ##############################")

while proceed == "yes":
    print("\n############################# [START] #############################")
    direction = input("\nType encode to 'encrypt' and 'decode' to decrypt: ").lower()
    text = input("\nType your message: ").lower()
    shift = int(input("\nType the shift number: "))    
    
    caesar(text, shift, direction)
    proceed = input("\nType 'yes' if you want to go again, otherwise type 'no': ").lower()
print("\nGoodbye...")
