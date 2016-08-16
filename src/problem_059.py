#   coding=UTF_8
#
#   problem_059.py
#   ProjectEuler
#
#   This file was created by Jens Kwasniok on 15.08.16.
#   Copyright (c) 2016 Jens Kwasniok. All rights reserved.
#

from problem_000 import *
from problem_059_cipher import cipher
from collections import Counter

class Problem_059(Problem):
    
    def __init__(self):
        self.problem_nr = 59
        self.description_str = '''Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt, a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.
'''
    
    def calculate(self, unused):
        
        sum = 0
        
        key_len = 3
        key = []
        
        for k in range(key_len):
            
            cs = Counter()
            i = k
            
            while i < len(cipher):
                cs[cipher[i]] += 1
                i += key_len
                
            cipher_value_for_e = cs.most_common(1)[0][0]
            
            key.append(cipher_value_for_e ^ ord(' '))
        
        i = 0
        while i < len(cipher):
            c = cipher[i] ^ key[i % key_len]
            sum += c
            i += 1
        
        self.last_result = sum
        self.last_result_details = key
        
    def details(self):
        key = self.last_result_details
        
        decipher = ""
        i = 0
        while i < len(cipher):
            c = cipher[i] ^ key[i % len(key)]
            decipher += chr(c)
            i += 1
        
        key_chr = ""
        for k in key:
            key_chr += chr(k)
            
        return "Original cipher:\n" + list_to_fancy_str(cipher, " ") + "\nDecoded text with key '" + list_to_fancy_str(key, ' ') + "' ('" + key_chr + "'):\n" + dye_highlight(decipher)
        
register_problem(Problem_059())
