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
let chosenWord = words[Math.floor(Math.random() * words.length)];
let display = Array(chosenWord.length).fill("_");
let lives = 6;
let guessedLetters = [];

document.getElementById("word-display").textContent = display.join(" ");
document.getElementById("hangman-stage").textContent = stages[6];

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