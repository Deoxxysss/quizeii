def leaderboard():
    import csv
    from pathlib import Path
    BASE_DIR = Path(__file__).parent
    SCORE_FILE = BASE_DIR / "data" / "score.csv"
    
    with open(SCORE_FILE, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader)

        rows = list(reader)
        
        print("=====Leaderboard=====")
        print()
        print()
        print()
        print()

        for rank, row in enumerate(rows, start=1):
            print(f"{rank}. {row[0]} - {row[1]} pts ({row[2]})")