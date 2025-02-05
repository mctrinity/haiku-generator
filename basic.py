from openai import OpenAI
import pyttsx3
import time

client = OpenAI()

# Ask the user for a haiku topic
topic = input("Enter a topic for your haiku: ")

def speak_haiku(haiku, is_first=False):
    """ Convert text to speech and read the haiku aloud """
    text = " ".join(haiku.splitlines())  # Convert multiline haiku into a single sentence

    if is_first:
        print("\n🔄 Restarting voice engine for the first haiku...\n")
        engine = pyttsx3.init()  # Reinitialize the engine before the first haiku
        engine.say(" ")  # Say a short silent phrase to force the engine to start
        engine.runAndWait()
        time.sleep(0.5)  # Give time to process before reading the first haiku
    else:
        engine = pyttsx3.init()  # Normal engine initialization for subsequent haikus

    time.sleep(0.2)  # Small delay before speaking
    engine.say(text)
    engine.runAndWait()  # Ensure full speech execution
    engine.stop()  # Properly stop the engine after each haiku

haikus = []  # Store new haikus in a list

# Open file to check if the topic is already written
with open("haikus.txt", "r") as file:
    file_content = file.read()

# Only write the topic if it hasn't been written already
if f"Topic: {topic}" not in file_content:
    with open("haikus.txt", "a") as file:
        file.write(f"\n\nTopic: {topic}\n")

# Generate 3 unique haikus
for i in range(3):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a poetic AI that writes haikus."},
            {"role": "user", "content": f"Write a unique haiku about {topic}, ensuring it differs from any previous one."}
        ],
        temperature=1.0,
        max_tokens=30
    )

    haiku = completion.choices[0].message.content.strip()  # Remove extra spaces
    haikus.append(haiku)  # Store in list for later use

    print(f"\nHaiku {i+1}:\n")
    print(haiku)

    # Save each haiku to file
    with open("haikus.txt", "a") as file:
        file.write(haiku + "\n\n")  # Adds space between haikus

# Speak all haikus aloud 🎙️
print("\n🎙️ Reading all haikus aloud...\n")
for i, haiku in enumerate(haikus):
    speak_haiku(haiku, is_first=(i == 0))  # Restart engine only for the first haiku

# Print all saved haikus just once at the end
with open("haikus.txt", "r") as file:
    print("\n🌸 Your Saved Haikus 🌸\n")
    print(file.read())

print("\n🌸 Haikus saved to haikus.txt! 📂")
