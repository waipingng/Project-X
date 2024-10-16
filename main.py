import random

def prompt_ai():
    options=["r", "p", "s"]
    choice=random.choice(options)
    return choice

if __name__ == "__main__":
    print(prompt_ai()) 