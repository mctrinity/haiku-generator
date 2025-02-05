# 🌸 Haiku Generator 🎧

A Python-based **Haiku Generator** that uses OpenAI's GPT API to create beautiful haikus and reads them aloud using `pyttsx3` text-to-speech.

---

## 🚀 Features
✅ Generates **3 unique haikus** based on a user-provided topic  
✅ **Reads the haikus aloud** using `pyttsx3`  
✅ **Saves all generated haikus** to a text file (`haikus.txt`)  
✅ Ensures **proper speech handling** to avoid missing words  
✅ **Error handling & file management** for smooth operation  

---

## ⚙️ Setup Instructions

### **1️⃣ Install Python (if not installed)**
Ensure you have **Python 3.7+** installed. Check with:
```sh
python --version
```
or
```sh
python3 --version
```
If Python is missing, [Download Python](https://www.python.org/downloads/).

---

### **2️⃣ Clone This Repository**
If you haven’t already pushed it to GitHub, you can do so first:
```sh
git clone https://github.com/YOUR_GITHUB_USERNAME/haiku-generator.git
cd haiku-generator
```

---

### **3️⃣ Install Required Dependencies**
Run the following command:
```sh
pip install -r requirements.txt
```
If `requirements.txt` does not exist, manually install:
```sh
pip install openai pyttsx3
```

---

### **4️⃣ Set Up OpenAI API Key**
1. **Get an API key** from [OpenAI](https://platform.openai.com/signup).
2. Create a `.env` file or set the API key manually:
   ```sh
   export OPENAI_API_KEY="your_api_key_here"
   ```
   Or, inside the script:
   ```python
   import os
   os.environ["OPENAI_API_KEY"] = "your_api_key_here"
   ```

---

## 🎯 Usage Guide

### **Run the Haiku Generator**
Simply run:
```sh
python haiku_generator.py
```
or
```sh
python3 haiku_generator.py
```

### **What Happens?**
1️⃣ You **enter a topic** (e.g., "summer", "winter", "space").  
2️⃣ The script **generates 3 unique haikus** using OpenAI's GPT.  
3️⃣ The AI **reads each haiku aloud** using text-to-speech (`pyttsx3`).  
4️⃣ The haikus **get saved** in `haikus.txt` for later reference.

---

## 📂 File Structure
```
📆 haiku-generator
 └─└─ haiku_generator.py  # Main script
 └─└─ haikus.txt          # Saved haikus
 └─└─ requirements.txt    # Required dependencies
 └─└─ README.md           # Project documentation
```

---

## ✅ Current Status
✔️ **Haiku generation**: Working  
✔️ **Text-to-speech (TTS)**: Working (sometimes skips the first word, in testing)  
✔️ **File saving**: Working  
⚠️ **Minor bug:** First word of the first haiku may be skipped in some environments.  

---

## 🔮 Future Improvements
🔹 **Fix first-word skipping issue in TTS**  
🔹 **Allow real-time streaming of haikus**  
🔹 **Add GUI (Tkinter or Streamlit) for easy use**  
🔹 **Generate haiku-themed images using DALL·E**  
🔹 **Make it a web app with Flask**  

