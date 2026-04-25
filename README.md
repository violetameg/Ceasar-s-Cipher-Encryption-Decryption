# Caesar Cipher Encryption & Decryption Tool (Greek/English)

This application is a specialized Caesar Cipher tool designed to handle both English and Greek alphabets, featuring a custom graphical user interface for ease of use.

## 🌟 Key Features

* **Multi-Language Support**: The tool supports lowercase and uppercase characters for both English and Greek.
* **Greek Normalization**: It automatically converts accented Greek characters (like 'ά', 'έ', 'ώ') and special forms (like the terminal 'ς') to their base forms before encryption.
* **History Logging**: Every action is saved locally in `Cipher.txt` and `Decipher.txt` files located in the program's directory.
* **Clipboard Integration**: Users can paste text directly from their system clipboard into the application with a single click.
* **Real-time Error Feedback**: The UI provides immediate "Error" notifications if required fields (like the shift value) are left empty or invalid.

## 🚀 Installation & Usage

1. **Run the Program**: Execute the `team-57.py` script using Python.
2. **Input Text**: Enter your message into the entry boxes labeled 'Insert Text'.
3. **Set Movement**: Define the shift value (rotation) in the 'Insert Movement' entries.
4. **Execute**: 
    * Click **'Press to cipher'** for encryption.
    * Click **'Press to decipher'** for decryption.
5. **Check History**: View the saved history in the `cipher.txt` and `decipher.txt` files created in the same folder.

## 📁 Project Structure

* **`team-57.py`**: The primary application using the `tkinter` library for the GUI and core cipher logic.
* **`ui-pyqt.py`**: An alternative version of the application built using the `PyQt5` framework, which includes a more advanced layout and spin-box controls.
* **`οδηγίες εγκατάστασης.pdf`**: The official documentation and installation guide for the application (in Greek).
* **`requirements.txt`**: Installed python libraries needed to run the code properly. 

## 🛠 Technical Details

The core logic resides in the `Caesar` class, which manages character shifts using Unicode values. 
* **Greek Range**: Uses characters from range 945 to 970 (Unicode).
* **English Range**: Uses standard ranges (97-123 for lowercase, 65-91 for uppercase).
* **Safety**: Punctuation and numbers are preserved and remain unshifted during the process.

---
*Developed by Team 57 as part of a group programming project for "Introduction to Computers" subject.*
