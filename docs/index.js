//Current line
var CurrentId = undefined;
const word_list = [
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
stages = [
  `
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========
`,
  `
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========
`,
  `
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========
`,
  `
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========`,
  `
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
`,
  `
  +---+
  |   |
  O   |
      |
      |
      |
=========
`,
  `
  +---+
  |   |
      |
      |
      |
      |
=========
`,
];

const logo = `mastergreyhat
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \\ / _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                    __/ |                      
                   |___/
`;

var inputValues = [];
const inputPrompts = [];
let lives = 6;
let end_of_game = false;
let chosen_word;
let display = "";
let guessed_letters = new Set();

// Click Run
$(document).ready(function () {
  $("#run-button").click(function () {
    inputValues = [];
    guessed_letters = new Set(); // Reset guessed letters

    chosen_word = word_list[Math.floor(Math.random() * word_list.length)];
    end_of_game = false;
    lives = 6;
    display = "";
    for (let i = 0; i < chosen_word.length; i++) {
      display += "_";
    }

    $("#Content").empty();
    NewLine(logo, false);
    NewLine("Word to guess: " + display, false);
    NewLine("Guess a letter: ", true);
  });
});

// Enter key handler
$(document).on("keydown", function (e) {
  var x = event.which || event.keyCode;
  if (x === 13) {
    var consoleLine = $("#" + CurrentId + " input").val();
    inputValues.push({ id: CurrentId, val: consoleLine });

    const guess = consoleLine.toLowerCase().trim();

    if (guessed_letters.has(guess)) {
      NewLine("You've already guessed " + guess, false);
      $(".console-carrot").remove();
      NewLine("Guess a letter: ", true);
      return;
    }

    guessed_letters.add(guess); // Add to guessed letters

    if (!chosen_word.includes(guess)) {
      NewLine(`You guessed ${guess}, that's not in the word. You lose a life.`, false);
      lives -= 1;

      if (lives <= 0) {
        end_of_game = true;
        NewLine(stages[lives], false);
        NewLine(`***********************IT WAS ${chosen_word}! YOU LOSE**********************`, false);
        $(".console-carrot").remove();
        return;
      }
    } else {
      for (let i = 0; i < chosen_word.length; i++) {
        if (chosen_word[i] === guess) {
          display = display.substring(0, i) + guess + display.substring(i + 1);
        }
      }
      NewLine(display, false);
    }

    if (!display.includes("_")) {
      end_of_game = true;
      NewLine("You win.", false);
      $(".console-carrot").remove();
      return;
    }

    if (!end_of_game) {
      NewLine(stages[lives], false);
    }

    $(".console-carrot").remove();
    NewLine(`****************************${lives}/6 LIVES LEFT****************************`, false);
    NewLine("Word to guess: " + display, false);
    NewLine("Guess a letter: ", true);
  }
});

// Adjust input box size
$(document).on("keydown", function (e) {
  var x = event.which || event.keyCode;
  var line = $("#" + CurrentId + " input");
  var length = line.val().length;
  if (x != 8) {
    line.attr("size", 1 + length);
  } else {
    line.attr("size", length * 0.95);
  }
  if (length === 0) {
    $("#" + CurrentId + " input").attr("size", "1");
  }
});

// Focus input on click
$(document).on("click", function (e) {
  $("#" + CurrentId + " input").focus();
});

// Create a new terminal line
function NewLine(text, isPrompt) {
  $(".console-carrot").remove();
  if (CurrentId !== undefined) {
    $("#" + CurrentId + " input").prop("disabled", true);
  }
  CurrentId = "consoleInput-" + GenerateId();

  if (isPrompt) {
    $("#Content").append(
      '<div id="' +
        CurrentId +
        '">' +
        text +
        '<input autocomplete="off" autocorrect="off" autocapitalize="off" spellcheck="false" type="text" class="terminal-input" /><div class="console-carrot"></div></div>'
    );
    $("#" + CurrentId + " input").focus();
    $("#" + CurrentId + " input").attr("size", "1");
  } else {
    $("#Content").append('<div id="' + CurrentId + '">' + text + "</div>");
  }

  document.getElementById(CurrentId).scrollIntoView();
}

function GenerateId() {
  return Math.random().toString(16).slice(2);
}

// Optional utility
function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}
