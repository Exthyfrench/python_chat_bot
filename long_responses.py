import random

R_EATING = "I dont like to eat anything, nor can I because im a bot!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"

def unknown():
    response = ['Could you please say that again?',
                "...",
                "Sounds like you dont know what your talking about!",
                "Are you okay?",
                "What does that even mean"][random.randrange(5)]
    return response          