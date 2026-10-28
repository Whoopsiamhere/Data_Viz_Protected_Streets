
'use strict';
const intro=document.getElementById('intro'),explorer=document.getElementById('explorer');
function showGuess(){document.getElementById('guessStep').hidden=false;document.getElementById('answerStep').hidden=true;document.getElementById('introTitle').focus({preventScroll:true});}
function reveal(choice){document.getElementById('guessStep').hidden=true;document.getElementById('answerStep').hidden=false;document.getElementById('guessFeedback').textContent=choice==='pavement'?'You got it.':choice==='safety'?'That was my first guess, too.':'Here’s what it means in this dataset.';document.getElementById('answerTitle').focus({preventScroll:true});}
function enterMap(){intro.hidden=true;explorer.hidden=false;window.scrollTo(0,0);document.getElementById('exploreTitle').focus({preventScroll:true});window.dispatchEvent(new Event('explorer:open'));}
document.querySelectorAll('[data-guess]').forEach(b=>b.onclick=()=>reveal(b.dataset.guess));
document.getElementById('enterMap').onclick=enterMap;
document.getElementById('skipIntro').onclick=enterMap;
document.getElementById('guessAgain').onclick=showGuess;
document.getElementById('revisitIntro').onclick=()=>{explorer.hidden=true;intro.hidden=false;window.scrollTo(0,0);reveal('pavement');document.getElementById('guessFeedback').textContent='Protected streets, explained.';};
