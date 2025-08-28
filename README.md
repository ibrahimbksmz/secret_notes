# Secret Notes 

**Secret Notes** is a simple desktop application to securely store and manage your private notes. Notes are encrypted using **Base64** and can only be decrypted with the correct master key.  

---

## Features 
- Add note title and content 
- Encrypt and decrypt with master key
- Simple security using Base64 
- User-friendly interface with Tkinter
- All notes saved in `secret_notes.txt` 

---

## File Structure 
- `secret_notes.txt` → Stores the notes 
- `logo.png` → Application logo 

---

## Usage 

### 1. Create and Encrypt a Note 
1. Enter your title 
2. Enter your secret note 
3. Enter master key 
4. Click **Save & Encrypt** 

> The note is encrypted and saved to the file.  
> Format: `note title, encrypted text, encrypted master key`  

#### Encryption Logic 
- Text is encoded to UTF-8 
- Encoded text is encrypted with Base64 
- Master key is encrypted the same way 
- Saved as `encrypted_note, encrypted_master_key` 

---

### 2. Decrypt a Note 
1. Paste the encrypted note 
2. Enter the master key 
3. Click **Decrypt** 

> If the master key is correct, the note will be decrypted.  

#### Decryption Logic 
- Read encrypted note from file 
- Compare with master key 
- If correct, Base64 is decoded to original text 
- If wrong, shows an error 
