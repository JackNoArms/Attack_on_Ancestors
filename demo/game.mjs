/**
 * Attack on Ancestors — sandbox fantasy encounter for portfolio visitors.
 * Classes, species and enemy below are illustrative, not canonical game data.
 * No user accounts, save files or external requests are used here.
 */
export const species = Object.freeze({
  Humano: {strength:2,agility:2,intellect:2,constitution:2},
  Elfo: {strength:1,agility:4,intellect:3,constitution:0},
  Anão: {strength:3,agility:1,intellect:1,constitution:3}
});
export const professions=Object.freeze({
  Guardião: {strength:4,agility:1,intellect:0,constitution:3},
  Caçador: {strength:2,agility:4,intellect:1,constitution:1},
  Místico: {strength:0,agility:1,intellect:6,constitution:1}
});
export const actions=Object.freeze(['Atacar','Defender','Usar magia']);
export function safeName(name){
  return String(name??'').trim().replace(/\s+/g,' ').slice(0,32);
}
export function buildCharacter({name='Aventureiro',race='Humano',profession='Guardião'}={}){
  const displayName=safeName(name);
  if(!displayName||displayName.length<2||!species[race]||!professions[profession]){
    throw new RangeError('Escolha um nome, uma raça e uma classe válidos.');
  }
  const raceBonus=species[race],classBonus=professions[profession];
  const stats=Object.fromEntries(Object.keys(raceBonus).map(key=>[key,5+raceBonus[key]+classBonus[key]]));
  return Object.freeze({
    name:displayName,race,profession,stats,
    maxHp:45+stats.constitution*3,maxMana:12+stats.intellect*2,maxStamina:20+stats.agility*2
  });
}
export function newEncounter(character){
  return {character,hp:character.maxHp,mana:character.maxMana,stamina:character.maxStamina,
    enemyHp:68,enemyMaxHp:68,defending:false,turn:1,over:false,winner:null,
    log:['Você encontra uma Sentinela de Pedra no caminho. Qual será sua estratégia?']};
}
function dice(random){
  const value=Number(random());
  if(!Number.isFinite(value))throw new Error('RNG inválido');
  return Math.max(1,Math.min(20,Math.floor(Math.max(0,Math.min(0.999999999,value))*20)+1));
}
export function takeTurn(original,action,random=Math.random){
  if(original.over)return original;
  if(!actions.includes(action))throw new RangeError('Ação inválida.');
  const s={...original,log:[...original.log],turn:original.turn+1,defending:false};
  const player=original.character;
  if(action==='Atacar'){
    const roll=dice(random),damage=Math.max(3,roll+Math.floor(player.stats.strength*1.2)-6);
    s.enemyHp=Math.max(0,s.enemyHp-damage);
    s.stamina=Math.max(0,s.stamina-2);
    s.log.push(`Você atacou (d20: ${roll}) e causou ${damage} de dano.`);
  }else if(action==='Defender'){
    s.defending=true;
    s.stamina=Math.min(player.maxStamina,s.stamina+3);
    s.log.push('Você assume uma postura defensiva para absorver o próximo golpe.');
  }else{
    if(original.mana<5){s.log.push('Mana insuficiente. Você recupera o fôlego.');s.stamina=Math.min(player.maxStamina,s.stamina+2);}
    else{
      const roll=dice(random),damage=Math.max(6,roll+player.stats.intellect-3);
      s.enemyHp=Math.max(0,s.enemyHp-damage);
      s.mana=Math.max(0,s.mana-5);
      s.log.push(`Você conjura uma magia (d20: ${roll}) e causa ${damage} de dano.`);
    }
  }
  if(s.enemyHp<=0){s.over=true;s.winner='player';s.log.push('Vitória! A Sentinela de Pedra foi derrotada.');return s;}
  const enemyRoll=dice(random);
  const enemyDamage=Math.max(1,Math.floor((enemyRoll+5)*(s.defending?0.35:1)));
  s.hp=Math.max(0,s.hp-enemyDamage);
  s.log.push(`A Sentinela reage e causa ${enemyDamage} de dano.`);
  if(s.hp<=0){s.over=true;s.winner='enemy';s.log.push('Você caiu em combate. Tente novamente com outra estratégia.');}
  return s;
}
