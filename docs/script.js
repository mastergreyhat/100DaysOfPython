const words = ["python", "hangman", "javascript", "challenge", "browser"];
const stages = [
  `
     -----
     |   |
     O   |
    /|\\  |
    / \\  |
         |
  =========`,
  `
     -----
     |   |
     O   |
    /|\\  |
    /    |
         |
  =========`,
  `
     -----
     |   |
     O   |
    /|\\  |
         |
         |
  =========`,
  `
     -----
     |   |
     O   |
    /|   |
         |
         |
  =========`,
  `
     -----
     |   |
     O   |
     |   |
         |
         |
  =========`,
  `
     -----
     |   |
     O   |
         |
         |
         |
  =========`,
  `
     -----
     |   |
         |
         |
         |
         |
  =========`
];

let chosenWord, display, lives, guessedLetters;

function initializeGame() {
  chosenWord = words[Math.floor(Math.random() * words.length)];
  display = Array(chosenWord.length).fill("_");
  lives = 6;
  guessedLetters = [];

  document.getElementById("lives").textContent = lives;
  document.getElementById("word-display").textContent = display.join(" ");
  document.getElementById("hangman-stage").textContent = stages[6];
  document.getElementById("message").textContent = "";
  document.getElementById("guess-input").disabled = false;
  document.getElementById("guess-input").value = "";
}

function makeGuess() {
  const input = document.getElementById("guess-input");
  const guess = input.value.toLowerCase();

  if (!guess || guess.length !== 1 || guessedLetters.includes(guess)) {
    document.getElementById("message").textContent = "Invalid or repeated guess.";
    input.value = "";
    return;
  }

  guessedLetters.push(guess);
  let correct = false;

  for (let i = 0; i < chosenWord.length; i++) {
    if (chosenWord[i] === guess) {
      display[i] = guess;
      correct = true;
    }
  }

  if (!correct) {
    lives--;
  }

  document.getElementById("lives").textContent = lives;
  document.getElementById("word-display").textContent = display.join(" ");
  document.getElementById("hangman-stage").textContent = stages[lives];
  input.value = "";
  document.getElementById("message").textContent = "";

  if (display.join("") === chosenWord) {
    document.getElementById("message").textContent = "🎉 You won!";
    disableInput();
  } else if (lives === 0) {
    document.getElementById("message").textContent = `💀 Game Over! Word was "${chosenWord}"`;
    document.getElementById("word-display").textContent = chosenWord;
    disableInput();
  }
}

function disableInput() {
  document.getElementById("guess-input").disabled = true;
}

function restartGame() {
  initializeGame();
}

// Initialize the game when the page loads
initializeGame();
