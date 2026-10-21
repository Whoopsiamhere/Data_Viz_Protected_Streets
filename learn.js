
'use strict';
const answer=document.getElementById('answer'),answerText=document.getElementById('answerText'),toggle=document.getElementById('showAnswer');
function setExplanation(open){answer.hidden=!open;toggle.setAttribute('aria-expanded',String(open));document.getElementById('explanationIcon').textContent=open?'−':'+';document.getElementById('explanationLabel').textContent=open?'Hide explanation':'Show explanation';}
function reveal(choice){answerText.textContent=choice==='pavement'?'Yes. The protection is about the pavement.':choice?'Here, “protected” refers to the pavement.':'The protection is about the pavement.';setExplanation(true);}
document.querySelectorAll('[data-guess]').forEach(button=>button.addEventListener('click',()=>{document.querySelectorAll('[data-guess]').forEach(b=>b.setAttribute('aria-pressed',String(b===button)));reveal(button.dataset.guess);}));
toggle.addEventListener('click',()=>{if(!answerText.textContent)answerText.textContent='The protection is about the pavement.';setExplanation(answer.hidden);});
