import {buildCharacter,newEncounter,takeTurn} from './game.mjs';

const $=id=>document.getElementById(id);
const labelMap={
  strength:'Força',agility:'Destreza',intellect:'Inteligência',constitution:'Constituição'
};
let encounter=null;

function value(name){
  return document.querySelector('input[name="'+name+'"]:checked')?.value||'';
}
function preview(){
  const name=$('name').value.trim()||'Aventureiro';
  const character=buildCharacter({
    name:name.length<2?'Aventureiro':name,
    race:value('race'),profession:value('profession')
  });
  $('preview-name').textContent=character.name;
  $('preview-type').textContent=character.race+' · '+character.profession;
  const area=$('preview-stats');area.replaceChildren();
  for(const [key,label] of Object.entries(labelMap)){
    const row=document.createElement('div');row.className='stat-line';
    const name=document.createElement('span');name.textContent=label;
    const total=document.createElement('strong');total.textContent=character.stats[key];
    row.append(name,total);area.append(row);
  }
}

function fillProgress(label,current,total){
  $(label+'-text').textContent=current+' / '+total;
  $(label+'-bar').style.width=(total>0?Math.max(0,Math.min(100,current/total*100)):0)+'%';
}
function renderBattle(){
  if(!encounter)return;
  const {character}=encounter;
  $('player-title').textContent=character.name+' · '+character.profession;
  fillProgress('health',encounter.hp,character.maxHp);
  fillProgress('mana',encounter.mana,character.maxMana);
  fillProgress('stamina',encounter.stamina,character.maxStamina);
  fillProgress('enemy',encounter.enemyHp,encounter.enemyMaxHp);
  const log=$('log');log.replaceChildren();
  encounter.log.slice(-6).forEach(message=>{
    const item=document.createElement('p');item.textContent=message;log.append(item);
  });
  $('result').hidden=!encounter.over;
  if(encounter.over){
    $('result').textContent=encounter.winner==='player'?'Você venceu! A sentinela foi derrotada.':'A sentinela venceu o duelo. Você pode tentar novamente.';
  }
  document.querySelectorAll('[data-action]').forEach(b=>b.disabled=encounter.over);
}

$('name').addEventListener('input',preview);
document.querySelectorAll('input[name=race],input[name=profession]').forEach(input=>input.addEventListener('change',preview));
$('form').addEventListener('submit',event=>{
  event.preventDefault();
  try{
    const character=buildCharacter({name:$('name').value,race:value('race'),profession:value('profession')});
    encounter=newEncounter(character);
    $('form-error').hidden=true;
    $('encounter-empty').hidden=true;
    $('battle').hidden=false;
    renderBattle();
    $('encounter').scrollIntoView({behavior:window.matchMedia('(prefers-reduced-motion: reduce)').matches?'auto':'smooth'});
  }catch(error){
    $('form-error').hidden=false;
    $('form-error').textContent=error.message;
  }
});
document.querySelectorAll('[data-action]').forEach(button=>button.addEventListener('click',()=>{
  if(encounter){
    encounter=takeTurn(encounter,button.dataset.action);
    renderBattle();
  }
}));
$('restart').addEventListener('click',()=>{
  if(encounter){encounter=newEncounter(encounter.character);renderBattle();}
});
document.querySelectorAll('.sidebar nav a').forEach(link=>{
  link.addEventListener('click',()=>{
    document.querySelectorAll('.sidebar nav a').forEach(item=>item.classList.toggle('active',item===link));
  });
});
preview();
