# quiz_cantautorato.py

def show_question(question, choices, correct_answer):
    print("\n" + question)
    for i, choice in enumerate(choices, start=1):
        print(f"{i}) {choice}")

    scelta = input("Scegli un'opzione (1-4): ")
    if scelta == str(correct_answer):
        print("Corretto!\n")
        return True
    else:
        print(f"Sbagliato! La risposta corretta era: {choices[correct_answer - 1]}\n")
        return False

def quiz():
    print("Benvenuto al Quiz sul Cantautorato Italiano!")
    punteggio = 0

    questions = [
        {
            "question": "Chi ha scritto la canzone 'Dolcenera'?",
            "choices": ["Lucio Dalla", "Francesco De Gregori", "Fabrizio De André", "Rino Gaetano"],
            "answer": 3
        },
        {
            "question": "Quale cantautore ha scritto 'La casa in riva al mare'?",
            "choices": ["Franco Battiato", "Lucio Dalla", "Paolo Conte", "Antonello Venditti"],
            "answer": 3
        },
        {
            "question": "Chi canta 'Rimmel'?",
            "choices": ["Francesco De Gregori", "Claudio Baglioni", "Lucio Battisti", "Paolo Conte"],
            "answer": 1
        },
        {
            "question": "Quale artista è noto per la canzone 'Ma il cielo è sempre più blu'?",
            "choices": ["Lucio Battisti", "Rino Gaetano", "Edoardo Bennato", "Gianni Morandi"],
            "answer": 2
        },
        {
            "question": "Chi ha scritto 'Voglio vederti danzare'?",
            "choices": ["Franco Battiato", "Ivano Fossati", "Pino Daniele", "Eugenio Finardi"],
            "answer": 1
        }
    ]

    for d in questions:
        corretto = show_question(d["question"], d["choices"], d["answer"])
        if corretto:
            punteggio += 1

    print(f"Hai totalizzato {punteggio} su {len(questions)} punti.")

if __name__ == "__main__":
    quiz()