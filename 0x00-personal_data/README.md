# Personal Data

This project covers examples of Personally Identifiable Information (PII), how to implement a log filter that will obfuscate PII fields, how to encrypt a password and check the validity of an input password, and how to authenticate to a database using environment variables.

## Examples of Personally Identifiable Information (PII)

Personally Identifiable Information (PII) refers to any data that could potentially identify a specific individual. Some examples of PII include:

- Name
- Social Security Number
- Date of Birth
- Biometric Records
- Financial Information (e.g., credit card numbers, bank account numbers)
- Medical Records
- IP Addresses

## Implementing a Log Filter to Obfuscate PII Fields

To protect sensitive information, it is important to obfuscate PII fields in log files. This can be achieved by implementing a log filter that replaces or masks the PII data with placeholders or dummy values.

## Encrypting and Validating Passwords

Passwords should never be stored in plain text. Instead, they should be encrypted using a secure hashing algorithm like bcrypt or Argon2. When a user attempts to log in, the input password should be hashed and compared with the stored hash to validate the user's credentials.

## Authenticating to a Database Using Environment Variables

To securely store and access sensitive database credentials, it is recommended to use environment variables. This way, the credentials are not hardcoded in the application code, reducing the risk of accidental exposure or leaks.
