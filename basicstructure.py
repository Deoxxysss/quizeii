import random
import time
categories = ["Python", "Science", "Anime", "History", "Gaming"]

print("Categories available:-")

for i, category in enumerate(categories, start=1):
    print(f"{i}. {category}")
z = input("Choose a Category:").lower()
    
    
python_questions = [
    {
        "question": "Who created Python?",
        "options": ["A. James Gosling", "B. Guido van Rossum", "C. Dennis Ritchie", "D. Bjarne Stroustrup"],
        "answer": "B"
    },
    {
        "question": "Which keyword is used to define a function?",
        "options": ["A. function", "B. define", "C. def", "D. fun"],
        "answer": "C"
    },
    {
        "question": "Which data type is immutable?",
        "options": ["A. List", "B. Dictionary", "C. Set", "D. Tuple"],
        "answer": "D"
    },
    {
        "question": "Which symbol starts a comment in Python?",
        "options": ["A. //", "B. #", "C. /*", "D. --"],
        "answer": "B"
    },
    {
        "question": "What is the output of len('Python')?",
        "options": ["A. 5", "B. 6", "C. 7", "D. 8"],
        "answer": "B"
    },
    {
        "question": "Which loop is used to iterate over a sequence?",
        "options": ["A. for", "B. do", "C. repeat", "D. until"],
        "answer": "A"
    },
    {
        "question": "Which function converts a string to an integer?",
        "options": ["A. float()", "B. str()", "C. int()", "D. bool()"],
        "answer": "C"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": ["A. ^", "B. **", "C. //", "D. %"],
        "answer": "B"
    },
    {
        "question": "Which keyword exits a loop?",
        "options": ["A. stop", "B. break", "C. exit", "D. quit"],
        "answer": "B"
    },
    {
        "question": "Which collection stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C"
    }
]
science_questions = [
    {
        "question": "What planet is known as the Red Planet?",
        "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Mercury"],
        "answer": "B"
    },
    {
        "question": "What is H2O?",
        "options": ["A. Oxygen", "B. Hydrogen", "C. Water", "D. Helium"],
        "answer": "C"
    },
    {
        "question": "What is the largest organ in the human body?",
        "options": ["A. Heart", "B. Brain", "C. Skin", "D. Liver"],
        "answer": "C"
    },
    {
        "question": "Which gas do plants absorb?",
        "options": ["A. Oxygen", "B. Carbon Dioxide", "C. Nitrogen", "D. Hydrogen"],
        "answer": "B"
    },
    {
        "question": "How many bones does an adult human have?",
        "options": ["A. 206", "B. 201", "C. 212", "D. 198"],
        "answer": "A"
    },
    {
        "question": "What is the speed of light approximately?",
        "options": ["A. 300,000 km/s", "B. 150,000 km/s", "C. 30,000 km/s", "D. 3,000 km/s"],
        "answer": "A"
    },
    {
        "question": "Which is the nearest star to Earth?",
        "options": ["A. Sirius", "B. Alpha Centauri", "C. The Sun", "D. Polaris"],
        "answer": "C"
    },
    {
        "question": "Which blood cells fight infections?",
        "options": ["A. Red Blood Cells", "B. White Blood Cells", "C. Platelets", "D. Plasma"],
        "answer": "B"
    },
    {
        "question": "What is the chemical symbol for Gold?",
        "options": ["A. Gd", "B. Ag", "C. Au", "D. Go"],
        "answer": "C"
    },
    {
        "question": "Which force keeps planets in orbit?",
        "options": ["A. Magnetism", "B. Friction", "C. Gravity", "D. Electricity"],
        "answer": "C"
    }
]
anime_questions = [
    {
        "question": "Who is the captain of the Straw Hat Pirates?",
        "options": ["A. Zoro", "B. Luffy", "C. Sanji", "D. Ace"],
        "answer": "B"
    },
    {
        "question": "What is Naruto's last name?",
        "options": ["A. Senju", "B. Uzumaki", "C. Uchiha", "D. Hyuga"],
        "answer": "B"
    },
    {
        "question": "Who wrote Death Note?",
        "options": ["A. Eiichiro Oda", "B. Hajime Isayama", "C. Tsugumi Ohba", "D. Masashi Kishimoto"],
        "answer": "C"
    },
    {
        "question": "Which anime features Titans?",
        "options": ["A. Bleach", "B. One Piece", "C. Attack on Titan", "D. Fairy Tail"],
        "answer": "C"
    },
    {
        "question": "What is Goku's Saiyan name?",
        "options": ["A. Bardock", "B. Kakarot", "C. Vegeta", "D. Broly"],
        "answer": "B"
    },
    {
        "question": "Who is the main character of Bleach?",
        "options": ["A. Naruto", "B. Ichigo Kurosaki", "C. Luffy", "D. Gon"],
        "answer": "B"
    },
    {
        "question": "Which anime has the Elric brothers?",
        "options": ["A. Fullmetal Alchemist", "B. Demon Slayer", "C. Jujutsu Kaisen", "D. Spy x Family"],
        "answer": "A"
    },
    {
        "question": "Who is known as the Pirate Hunter?",
        "options": ["A. Sanji", "B. Zoro", "C. Usopp", "D. Law"],
        "answer": "B"
    },
    {
        "question": "Who inherits the Attack Titan first in the series?",
        "options": ["A. Eren Yeager", "B. Armin Arlert", "C. Grisha Yeager", "D. Erwin Smith"],
        "answer": "C"
    },
    {
        "question": "Which anime features Tanjiro Kamado?",
        "options": ["A. Jujutsu Kaisen", "B. Demon Slayer", "C. Black Clover", "D. Chainsaw Man"],
        "answer": "B"
    }
]
history_questions = [
    {
        "question": "Who discovered America in 1492?",
        "options": ["A. Vasco da Gama", "B. Christopher Columbus", "C. Ferdinand Magellan", "D. Marco Polo"],
        "answer": "B"
    },
    {
        "question": "Who was the first Emperor of Rome?",
        "options": ["A. Julius Caesar", "B. Augustus", "C. Nero", "D. Constantine"],
        "answer": "B"
    },
    {
        "question": "In which year did World War II end?",
        "options": ["A. 1943", "B. 1944", "C. 1945", "D. 1946"],
        "answer": "C"
    },
    {
        "question": "Who was known as the Iron Lady?",
        "options": ["A. Margaret Thatcher", "B. Queen Elizabeth II", "C. Joan of Arc", "D. Indira Gandhi"],
        "answer": "A"
    },
    {
        "question": "Which wall fell in 1989?",
        "options": ["A. Great Wall", "B. Berlin Wall", "C. Hadrian's Wall", "D. Wailing Wall"],
        "answer": "B"
    },
    {
        "question": "Who was the first President of the United States?",
        "options": ["A. Abraham Lincoln", "B. Thomas Jefferson", "C. George Washington", "D. John Adams"],
        "answer": "C"
    },
    {
        "question": "Which civilization built the pyramids of Giza?",
        "options": ["A. Romans", "B. Greeks", "C. Egyptians", "D. Persians"],
        "answer": "C"
    },
    {
        "question": "Who was assassinated in 1963 in Dallas?",
        "options": ["A. Martin Luther King Jr.", "B. John F. Kennedy", "C. Winston Churchill", "D. Richard Nixon"],
        "answer": "B"
    },
    {
        "question": "Who was the first man to walk on the Moon?",
        "options": ["A. Yuri Gagarin", "B. Neil Armstrong", "C. Buzz Aldrin", "D. Michael Collins"],
        "answer": "B"
    },
    {
        "question": "The French Revolution began in?",
        "options": ["A. 1776", "B. 1789", "C. 1812", "D. 1804"],
        "answer": "B"
    }
]
gaming_questions = [
    {
        "question": "Which company created Minecraft?",
        "options": ["A. Valve", "B. Mojang", "C. Rockstar", "D. Ubisoft"],
        "answer": "B"
    },
    {
        "question": "Which game features the character Master Chief?",
        "options": ["A. Halo", "B. Call of Duty", "C. Doom", "D. Fortnite"],
        "answer": "A"
    },
    {
        "question": "Which company develops the Grand Theft Auto series?",
        "options": ["A. Rockstar Games", "B. Ubisoft", "C. EA", "D. Nintendo"],
        "answer": "A"
    },
    {
        "question": "Which battle royale game introduced the building mechanic?",
        "options": ["A. PUBG", "B. Apex Legends", "C. Fortnite", "D. Warzone"],
        "answer": "C"
    },
    {
        "question": "What does NPC stand for?",
        "options": ["A. New Player Character", "B. Non-Playable Character", "C. Next Play Character", "D. Non-Power Character"],
        "answer": "B"
    },
    {
        "question": "Which game series features Link?",
        "options": ["A. Final Fantasy", "B. Zelda", "C. Pokémon", "D. Elden Ring"],
        "answer": "B"
    },
    {
        "question": "Which company makes the PlayStation?",
        "options": ["A. Microsoft", "B. Sony", "C. Nintendo", "D. Sega"],
        "answer": "B"
    },
    {
        "question": "Which game popularized the battle royale genre in 2017?",
        "options": ["A. PUBG", "B. Fortnite", "C. Apex Legends", "D. Free Fire"],
        "answer": "A"
    },
    {
        "question": "In Minecraft, which material is stronger than iron?",
        "options": ["A. Stone", "B. Gold", "C. Diamond", "D. Wood"],
        "answer": "C"
    },
    {
        "question": "Which game franchise features Kratos?",
        "options": ["A. Assassin's Creed", "B. God of War", "C. Dark Souls", "D. Diablo"],
        "answer": "B"
    }
]
try:
    if z == "python":
        questions = python_questions
    elif z == "science":
        questions = science_questions
    elif z == "anime":
        questions = anime_questions
    elif z == "history":
        questions = history_questions
    elif z == "gaming":
        questions = gaming_questions
    else:
        print("Please enter from the options:")
        
except ValueError:
    print("Please enter from the options:")

random.shuffle(questions)

score = 0

for q in questions:
    print("\n" + q["question"])

    for option in q["options"]:
        print(option)

    ans = input("Enter your answer (A/B/C/D): ").upper()

    if ans == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was {q['answer']}.")

print(f"\n🎉 Final Score: {score}/{len(questions)}")