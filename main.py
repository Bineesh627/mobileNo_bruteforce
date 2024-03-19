from telethon_bot import TelethonBot
import time
import sys

def check_file():
    # Wordlist of phone numbers to search Truecaller data
    file_path = 'wordlists/contacts.txt'
    with open(file_path, "r") as file:
        for line in file:
            yield line.strip()  # Using yield to return lines one by one

def main():
    print("Data capturing started...")
    bot = TelethonBot()

    while True:
        try:
            for message in check_file():
                print(message)
                try:
                    bot.message = message
                    bot.run()
                except Exception as e:
                    print(f"An error occurred: {e}")
                    print("Waiting for 10 seconds before retrying...")
                    time.sleep(10)
                    continue
                print("waiting..")
                time.sleep(5)
        except KeyboardInterrupt:
            print("Data capturing stopped by the user.")
            break  # Exit the loop if the user interrupts the program
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Attempting to continue...")
            time.sleep(10)  # Wait before retrying
            continue
        finally:
            print("Data capturing finished..")
            time.sleep(10)  # Optional delay before restarting the loop

if __name__ == "__main__":
    main()
