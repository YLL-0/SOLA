'use strict';
// # selecta ID, . izbere CLASSE
const score0EL = document.querySelector('#score--0');
//enaka funkcija: 
const score1EL = document.getElementById('score--1');
const diceEL = document.querySelector('.dice');
const btnNew = document.querySelector('.btn--new');
const btnRoll = document.querySelector('.btn--roll');
const btnHold = document.querySelector('.btn--hold');

score0EL.textContent = 0;
score1EL.textContent = 0;
diceEL.classList.add('hidden');


//Rolling dice func:
btnRoll.addEventListener('click', function() {
  //1. generate rnd dice roll
  const dice = Math.trunc(Math.random() * 6) + 1;

  //2. disply the rolled dice
  diceEL.classList.remove('hidden');
  diceEL.src = `dice-${dice}.png`

  //3. check if roll = 1, if shithc player  


})
