# AES Encryption Algorithm

This repository contains Python code that implements the Advanced Encryption Standard (AES) algorithm. AES is a widely used encryption algorithm that is used to secure data by performing encryption and decryption operations.
This is for training purposes only, not to be used in real encrytption apps, ever. 

## Introduction

AES is a symmetric encryption algorithm, meaning the same key is used for both encryption and decryption. It operates on blocks of data and uses a substitution-permutation network to perform its encryption and decryption operations.

## Code Description

The code in this repository is a Python implementation of the AES encryption algorithm. It includes the following main components:

### Key Expansion

AES uses a key expansion process to generate a series of round keys from the original encryption key. These round keys are used in each round of encryption and decryption. The `key_expansion` function in the code generates the round keys based on the original key.

### Rounds

AES encryption and decryption consist of multiple rounds, with the number of rounds depending on the key size (128, 192, or 256 bits). Each round involves several operations, including substitution (sub-byte), permutation (shift-rows and mix-columns), and adding the round key. The code includes functions to perform these operations in each round.

## Usage

To use this AES encryption algorithm, follow these steps:

1. Provide the original encryption key in the `key` variable.
2. Call the `key_expansion` function to generate the round keys.
3. Create a data block that you want to encrypt or decrypt as the `state` variable.
4. Call the `addRoundKey` function for each round, passing the `state`, round key, and round number as arguments.
5. Perform the sub-byte, shift-rows, and mix-columns operations for each round, as needed.
6. After all rounds are completed, the `state` variable will contain the encrypted or decrypted data.
