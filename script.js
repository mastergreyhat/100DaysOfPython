const words = [
  "abruptly",
  "absurd",
  "abyss",
  "affix",
  "askew",
  "avenue",
  "awkward",
  "axiom",
  "azure",
  "bagpipes",
  "bandwagon",
  "banjo",
  "bayou",
  "beekeeper",
  "bikini",
  "blitz",
  "blizzard",
  "boggle",
  "bookworm",
  "boxcar",
  "boxful",
  "buckaroo",
  "buffalo",
  "buffoon",
  "buxom",
  "buzzard",
  "buzzing",
  "buzzwords",
  "caliph",
  "cobweb",
  "cockiness",
  "croquet",
  "crypt",
  "curacao",
  "cycle",
  "daiquiri",
  "dirndl",
  "disavow",
  "dizzying",
  "duplex",
  "dwarves",
  "embezzle",
  "equip",
  "espionage",
  "euouae",
  "exodus",
  "faking",
  "fishhook",
  "fixable",
  "fjord",
  "flapjack",
  "flopping",
  "fluffiness",
  "flyby",
  "foxglove",
  "frazzled",
  "frizzled",
  "fuchsia",
  "funny",
  "gabby",
  "galaxy",
  "galvanize",
  "gazebo",
  "giaour",
  "gizmo",
  "glowworm",
  "glyph",
  "gnarly",
  "gnostic",
  "gossip",
  "grogginess",
  "haiku",
  "haphazard",
  "hyphen",
  "iatrogenic",
  "icebox",
  "injury",
  "ivory",
  "ivy",
  "jackpot",
  "jaundice",
  "jawbreaker",
  "jaywalk",
  "jazziest",
  "jazzy",
  "jelly",
  "jigsaw",
  "jinx",
  "jiujitsu",
  "jockey",
  "jogging",
  "joking",
  "jovial",
  "joyful",
  "juicy",
  "jukebox",
  "jumbo",
  "kayak",
  "kazoo",
  "keyhole",
  "khaki",
  "kilobyte",
  "kiosk",
  "kitsch",
  "kiwifruit",
  "klutz",
  "knapsack",
  "larynx",
  "lengths",
  "lucky",
  "luxury",
  "lymph",
  "marquis",
  "matrix",
  "megahertz",
  "microwave",
  "mnemonic",
  "mystify",
  "naphtha",
  "nightclub",
  "nowadays",
  "numbskull",
  "nymph",
  "onyx",
  "ovary",
  "oxidize",
  "oxygen",
  "pajama",
  "peekaboo",
  "phlegm",
  "pixel",
  "pizazz",
  "pneumonia",
  "polka",
  "pshaw",
  "psyche",
  "puppy",
  "puzzling",
  "quartz",
  "queue",
  "quips",
  "quixotic",
  "quiz",
  "quizzes",
  "quorum",
  "razzmatazz",
  "rhubarb",
  "rhythm",
  "rickshaw",
  "schnapps",
  "scratch",
  "shiv",
  "snazzy",
  "sphinx",
  "spritz",
  "squawk",
  "staff",
  "strength",
  "strengths",
  "stretch",
  "stronghold",
  "stymied",
  "subway",
  "swivel",
  "syndrome",
  "thriftless",
  "thumbscrew",
  "topaz",
  "transcript",
  "transgress",
  "transplant",
  "triphthong",
  "twelfth",
  "twelfths",
  "unknown",
  "unworthy",
  "unzip",
  "uptown",
  "vaporize",
  "vixen",
  "vodka",
  "voodoo",
  "vortex",
  "voyeurism",
  "walkway",
  "waltz",
  "wave",
  "wavy",
  "waxy",
  "wellspring",
  "wheezy",
  "whiskey",
  "whizzing",
  "whomever",
  "wimpy",
  "witchcraft",
  "wizard",
  "woozy",
  "wristwatch",
  "wyvern",
  "xylophone",
  "yachtsman",
  "yippee",
  "yoked",
  "youthful",
  "yummy",
  "zephyr",
  "zigzag",
  "zigzagging",
  "zilch",
  "zipper",
  "zodiac",
  "zombie",
];

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
