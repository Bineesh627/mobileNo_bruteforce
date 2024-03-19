# Mobile Number Bruteforce

This project utilizes a Telegram chatbot to brute-force phone numbers and retrieve their details.

The main objective of this project is to generate a wordlist of phone numbers and use it to extract information from Truecaller. It employs a brute-force approach to gather user details associated with phone numbers.

## Setup

1. Clone the repository:

```sh
git clone https://github.com/Bineesh627/mobileNo_bruteforce.git
cd mobileNo_bruteforce
```

2. Install the required dependencies:

```sh
pip install -r requirements.txt
```

## Generating Wordlist

Modify the `numberGenerator.py` file to generate the desired wordlist:

```sh
nano numberGenerator.py
```

You can adjust the range of the list to specify the numbers you want to search for:

```python
for i in range(1000, 10000):
```

Modify the text to match your country code and target phone number pattern:

```python
text = f"+919281{number}34\n"
```

## Running the Program

Execute the main program to initiate the bruteforce process and retrieve phone number details in JSON format:

```python
python main.py
```

Please note that this project is in its initial stage, and we will continue to enhance its features.
