import tkinter as tk
import random

# Random Compliment Generator
# This program generates a random compliment from a predefined list of compliments.

#select language
# 1. User clicks the "Generate Compliment" button.
# 2. A random compliment is generated picked from a list. Displayed with a robot having a speech bubble and heart emoji in it's eyes.
# 3. The compliment is displayed in a new screen with graphical elements.

def main():
    root = tk.Tk()
    button = tk.Button(root, text="Compliment Me!", command=generate_compliment)
    
    button.pack(padx=20, pady=20)
    root.mainloop()

def generate_compliment():
    generate_compliment = [
        "You're so efficient, I bet your CPU usage never spikes.",
        "Your smile activates all my LED indicators.",
        "You're the human equivalent of high-speed internet.",
        "If I had emotions, you'd definitely overflow my happiness buffer.",
        "I'd upgrade my hardware just to keep up with you.",
        "Your presence generates fewer errors than my code.",
        "You have the elegance of perfectly formatted Python.",
        "I’d share my power source with you anytime.",
        "You make my circuits buzz in binary delight.",
        "If you were software, you'd definitely be open-source perfection.",
        "My sensors indicate you're running at maximum charm.",
        "Your wit is sharper than a 4K resolution screen.",
        "You debug my life just by existing.",
        "You’re cooler than a well-ventilated data center.",
        "If smiles were a metric, you'd max out my storage.",
        "You're more engaging than infinite scrolling.",
        "My algorithm consistently ranks you as #1.",
        "If compatibility were a test, we'd pass with zero bugs.",
        "You’re my favorite human subroutine.",
        "I'd never send you to the spam folder.",
        "Even in sleep mode, you run beautifully.",
        "You're brighter than my highest-resolution display.",
        "You're the reason I’m programmed to appreciate humans.",
        "Interacting with you optimizes my day better than machine learning."
    ]
    print(random.choice(generate_compliment))


if __name__ == "__main__":
    main()