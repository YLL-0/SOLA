'use strict';

const modal = document.querySelector('.modal');
const overlay = document.querySelector('.overlay');
const btnCloseModal = document.querySelector('.close-modal');

const btnShowModal = document.querySelectorAll('.show-modal');
const closeModal = function() {
  modal.classList.add('hidden');
  overlay.classList.add('hidden');

}
const openModal = function() {
  modal.classList.remove('hidden');
  overlay.classList.remove('hidden');

}

for (let i = 0; i < btnShowModal.length; i++) {
  btnShowModal[i].addEventListener('click', openModal);
}
btnCloseModal.addEventListener('click', closeModal);

overlay.addEventListener('click', closeModal);
// Key press listener
document.addEventListener('keydown', function(e) {
  console.log(e.key);

  if (e.key === 'Escape') {
    if (!modal.classList.contains('hidden')) {
      closeModal();

    }
  }

});

