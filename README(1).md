
# Keylogger Program

## Overview

This program is a simple keylogger implemented in Python. It captures keystrokes and sends them via email to a specified recipient. The program uses the `pynput` library to monitor keyboard events and the `smtplib` library to send emails. This tool is intended for educational purposes only and should be used responsibly.

## Features

- Captures keystrokes including special keys (Enter, Backspace, Tab, etc.)
- Saves keystrokes to a file (`keylogger.txt`)
- Sends the captured keystrokes to a specified email address
- Opens the saved keystrokes file in the web browser after exiting the program

## Requirements

- Python 3.x
- Required libraries:
  - `pynput`
  - `smtplib`
  - `ssl`

### Install Required Libraries

You can install the required libraries using pip:

```bash
pip install pynput
```

## Configuration

1. Open the script and configure the following variables:
   - `sender_mail`: Enter the sender's email address.
   - `receiver_mail`: Enter the recipient's email address.
   - `password`: Enter the sender's email password (ensure that less secure app access is enabled for the account).
   - `port`: Set to `25` (or use the appropriate SMTP port for your email provider).

2. Make sure to adjust the email message if needed.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script using Python:

   ```bash
   python keylogger.py
   ```

4. The keylogger will start capturing keystrokes until you press the **Esc** key combined with **Tab**. 
5. After stopping the keylogger, it will open the `keylogger.txt` file in your web browser and send the keystrokes to the specified email address.

## Example Output

- **When the program is running**, it captures keystrokes and writes them to `keylogger.txt`.

- **Email Sent Notification**:

   ```
   Email Sent to sender_email@example.com
   ```

## Notes

- This program is for educational purposes only. Ensure you have permission to monitor keystrokes on the device where you run this script.
- Be cautious when handling sensitive information, such as email passwords.
- Ensure you comply with local laws and regulations regarding keylogging and monitoring.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
