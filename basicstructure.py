def play_game():
    import random
    from pathlib import Path
    import json

    BASE_DIR = Path(__file__).parent

    def load_questions(category):
        path = BASE_DIR / "questions" / f"{category}.json"
        with open(path, "r", encoding="utf-8") as file:
            return json.load(file)

    all_questions = {
        "python": load_questions("python"),
        "science": load_questions("science"),
        "anime": load_questions("anime"),
        "history": load_questions("history"),
        "gaming": load_questions("gaming")
    }
        
    categories = list(all_questions.keys())

    print("Categories available:\n")

    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category.title()}")
    z = input("Choose a Category:").lower()
        
    if z in all_questions:
        questions = all_questions[z]
    else:
        print("Please enter one of the available categories.")
        exit()

    random.shuffle(questions)

    score = 0

    for q in questions:
        print("\n" + q["question"])

        for option in q["options"]:
            print(option)

        ans = input("Enter your answer (A/B/C/D): ").upper()

        if ans == q["answer"]:
            print("✅ Correct!")
            print()
            score += 1
        else:
            correct = ord(q["answer"]) - ord("A")
            print(f"❌ Wrong! Correct answer: {q['options'][correct]}")
            print()

    percentage = score / len(questions) * 100

    print(f"\n🎉 Final Score: {score}/{len(questions)}")
    print(f"Percentage: {percentage:.1f}%")
    if percentage == 100:
        print("🏆 Grade: S")
    elif percentage >= 90:
        print("🌟 Grade: A")
    elif percentage >= 80:
        print("✨ Grade: B")
    elif percentage >= 70:
        print("👍 Grade: C")
    elif percentage >= 60:
        print("🙂 Grade: D")
    else:
        print("📚 Grade: F")
    
    if __name__ == "__main__":
        play_game()