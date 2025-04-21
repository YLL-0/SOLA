'use strict';
// console.log(document.querySelector('.message').textContent);
// document.querySelector('.number').textContent = 13;
// = 10;

// document.querySelector('.guess').value = 23;
// console.log(document.querySelector('.guess').value);
//ko izbiramo razrede je .razred drugace pa ni .
let secretNumber = Math.trunc(Math.random() * 20) + 1;

let score = 20;
let highscore = 0;
document.querySelector('.check').addEventListener('click', function() {
  const guess = Number(document.querySelector('.guess').value);
  console.log(guess, typeof guess);


  //No imput
  if (!guess) {
    document.querySelector('.message').textContent = 'Not a number';

    //Player win
  } else if (guess === secretNumber) {
    document.querySelector('.message').textContent = 'Correct number';

    document.querySelector('.number').textContent = secretNumber;
    //Igranje s css
    document.querySelector('body').style.backgroundColor = '#60b347';
    document.querySelector('.number').style.width = '30rem';

    if (highscore < score) {
      highscore = score;
      document.querySelector('.highscore').textContent = highscore;
    }


  }//Guess to high 
  else if (guess > secretNumber) {
    if (score > 1) {

      document.querySelector('.message').textContent = 'Too high 📈';
      score--;
      document.querySelector('.score').textContent = score;
    }
    else
      document.querySelector('.message').textContent = 'You lost the game'

  }//Guess to low 
  else if (guess < secretNumber) {
    if (score > 1) {
      document.querySelector('.message').textContent = 'Too low 📉';
      score--;
      document.querySelector('.score').textContent = score;
    }
    else
      document.querySelector('.message').textContent = 'You lost the game'

  };


});

document.querySelector('.again').addEventListener('click', function() {
  console.log('AGAIN');

  score = 20;
  secretNumber = Math.trunc(Math.random() * 20) + 1;
  document.querySelector('.score').textContent = score;
  document.querySelector('.guess').value = '';
  document.querySelector('body').style.backgroundColor = '#222';
  document.querySelector('.number').style.width = '15rem';
  document.querySelector('.number').textContent = '?';
  document.querySelector('.message').textContent = 'Start guessing...';
  //restore the score, secrt number and guess imput field
  //restore the background color #222 and number = 15 rem 


});

