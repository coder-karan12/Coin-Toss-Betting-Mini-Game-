# 🪙 Coin Toss Betting Game

A simple terminal-based **Coin Toss Betting Game** built using Python. The player starts with a virtual balance, places bets, predicts the outcome of a coin toss, and either wins or loses money based on their guess.

## 📌 Features

* 💰 Starting balance of ₹100
* 🎲 Random coin toss using Python's `random` module
* 🎯 Guess **Heads** or **Tails**
* 💵 Bet any valid amount within your balance
* ✅ Balance increases on a correct guess
* ❌ Balance decreases on an incorrect guess
* 🛡️ Input validation for:

  * Insufficient balance
  * Zero betting amount
  * Negative betting amount
* 🔁 Continuous gameplay until the balance reaches ₹0

## 🛠️ Technologies Used

* Python 3
* `random` module

## 🚀 How to Run

1. Clone this repository.
2. Open the project in VS Code or any Python IDE.
3. Run the Python file.

```bash
python coin_toss_betting.py
```

## 🎮 How to Play

1. Start with a balance of **₹100**.
2. Enter your bet amount.
3. Choose **Heads** or **Tails**.
4. The computer randomly tosses a coin.
5. If your guess is correct:

   * Your balance increases by your bet amount.
6. If your guess is incorrect:

   * Your balance decreases by your bet amount.
7. The game continues until your balance becomes **₹0**.

## 📷 Sample Gameplay

```text
====================
 Coin Toss Betting
====================

Current Balance: ₹100

Enter Bet Amount: 20
Choose Heads or Tails: Heads

Coin Landed On: Heads

Congratulations! You guessed it right.

Current Balance: ₹120
```

## 📚 Concepts Practiced

* Variables
* User Input
* Conditional Statements (`if`, `elif`, `else`)
* `while` Loops
* Lists
* String Methods
* Random Module
* Input Validation
* Basic Game Logic

## 🔮 Future Improvements

* Play Again option
* Multiple difficulty levels
* Betting history
* Win/Loss statistics
* High score system
* Save game progress using file handling
* Better input validation using `try` and `except`

## 👨‍💻 Author

Developed as a Python mini project to practice programming fundamentals and improve problem-solving skills.

If you found this project interesting, feel free to ⭐ the repository!
