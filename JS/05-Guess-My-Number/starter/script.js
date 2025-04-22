/**
 * Number Guessing Game
 * 
 * Created by: YLL-0
 * Last updated: 2025-04-21 21:34:56
 * 
 * Game rules:
 * - Guess a number between 1-20
 * - Each incorrect guess reduces score by 1
 * - Try to achieve the highest score possible
 */

'use strict';

// --- Game Variables ---
// Random number between 1-20
let secretNumber = Math.trunc(Math.random() * 20) + 1;
// Starting score
let score = 20;
// Highscore (persists between games)
let highscore = 0;

/**
 * Helper function to display messages in the UI
 * @param {string} message - The message to display
 */
const displayMessage = function(message) {
  document.querySelector('.message').textContent = message;
};

// --- Event Handlers ---

/**
 * Check button click handler
 * Processes player's guess and updates game state
 */
document.querySelector('.check').addEventListener('click', function() {
  // Convert input value to number
  const guess = Number(document.querySelector('.guess').value);
  console.log(guess, typeof guess);

  // No input scenario
  if (!guess) {
    displayMessage('Not a number');
  }
  // Player wins scenario
  else if (guess === secretNumber) {
    displayMessage('Correct number');

    // Show the secret number
    document.querySelector('.number').textContent = secretNumber;

    // Apply winning visual styles
    document.querySelector('body').style.backgroundColor = '#60b347';
    document.querySelector('.number').style.width = '30rem';

    // Update highscore if current score is better
    if (highscore < score) {
      highscore = score;
      document.querySelector('.highscore').textContent = highscore;
    }
  }
  // When guess is wrong
  else if (guess !== secretNumber) {
    if (score > 1) {
      // Ternary operator to determine if guess is too high or too low
      displayMessage(guess > secretNumber ? 'Too high 📈' : 'Too low 📉');

      // Decrease score
      score--;
      document.querySelector('.score').textContent = score;
    }
    else {
      // Game over scenario
      displayMessage('You lost the game');
      document.querySelector('.score').textContent = 0;
    }
  }

  /* 
   * Original code (refactored above to be more DRY)
   * The below commented section had separate handlers for 'too high' and 'too low'
   * scenarios instead of using the ternary operator
   */
  // Guess too high 
  // else if (guess > secretNumber) {
  //   if (score > 1) {
  //     document.querySelector('.message').textContent = 'Too high 📈';
  //     score--;
  //     document.querySelector('.score').textContent = score;
  //   }
  //   else {
  //     document.querySelector('.message').textContent = 'You lost the game'
  //     document.querySelector('.score').textContent = 0;
  //   }
  // }
  // Guess too low 
  // else if (guess < secretNumber) {
  //   if (score > 1) {
  //     document.querySelector('.message').textContent = 'Too low 📉';
  //     score--;
  //     document.querySelector('.score').textContent = score;
  //   }
  //   else
  //     document.querySelector('.message').textContent = 'You lost the game'
  // };
});

/**
 * Again button click handler
 * Resets the game to initial state while preserving highscore
 */
document.querySelector('.again').addEventListener('click', function() {
  console.log('AGAIN');

  // Reset game variables
  score = 20;
  secretNumber = Math.trunc(Math.random() * 20) + 1;

  // Reset UI elements
  document.querySelector('.score').textContent = score;
  document.querySelector('.guess').value = '';
  document.querySelector('body').style.backgroundColor = '#222';
  document.querySelector('.number').style.width = '15rem';
  document.querySelector('.number').textContent = '?';
  displayMessage('Start guessing...');
});
