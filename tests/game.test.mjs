import test from 'node:test';
import assert from 'node:assert/strict';
import {buildCharacter,newEncounter,takeTurn,actions,safeName} from '../demo/game.mjs';

test('character creation derives stats from two independent options',()=>{
 const guardian=buildCharacter({name:'Aerin',race:'Humano',profession:'Guardião'});
 const mystic=buildCharacter({name:'Aerin',race:'Elfo',profession:'Místico'});
 assert.equal(guardian.name,'Aerin');
 assert.equal(guardian.stats.strength,11);
 assert.ok(mystic.stats.intellect>guardian.stats.intellect);
 assert.ok(guardian.maxHp>0&&guardian.maxMana>0&&guardian.maxStamina>0);
 assert.notDeepEqual(mystic.stats,guardian.stats);
});

test('invalid character inputs are rejected',()=>{
 for(const data of [
  {name:'A',race:'Humano',profession:'Guardião'},
  {name:'hero',race:'Unknown',profession:'Guardião'},
  {name:'hero',race:'Humano',profession:'Unknown'}
 ]) assert.throws(()=>buildCharacter(data),RangeError);
 assert.equal(safeName('  Hero   Prime  '),'Hero Prime');
});

test('turn updates hit points and dice logs deterministically',()=>{
 const character=buildCharacter();
 const first=newEncounter(character);
 const next=takeTurn(first,'Atacar',()=>0.5);
 assert.equal(first.enemyHp,68);
 assert.ok(next.enemyHp<68);
 assert.equal(next.turn,2);
 assert.match(next.log.join(' '),/d20/);
 assert.ok(next.hp<=character.maxHp);
});

test('defend reduces enemy damage for the same dice',()=>{
 const base=newEncounter(buildCharacter());
 const defended=takeTurn(base,'Defender',()=>0.4);
 const attacked=takeTurn(base,'Atacar',()=>0.4);
 assert.ok(defended.hp>attacked.hp);
});

test('mana is spent only when magic can be cast',()=>{
 const char=buildCharacter();
 const first=newEncounter(char);
 const cast=takeTurn(first,'Usar magia',()=>0.6);
 assert.equal(cast.mana,first.mana-5);
 const depleted={...first,mana:1};
 const exhausted=takeTurn(depleted,'Usar magia',()=>0.6);
 assert.equal(exhausted.mana,1);
 assert.match(exhausted.log.join(' '),/insuficiente/);
});

test('invalid action fails and finished encounter cannot restart itself',()=>{
 const first=newEncounter(buildCharacter());
 assert.throws(()=>takeTurn(first,'Excluir arquivos'),RangeError);
 assert.deepEqual(actions,['Atacar','Defender','Usar magia']);
 const win={...first,enemyHp:1};
 const after=takeTurn(win,'Usar magia',()=>0.6);
 assert.equal(after.over,true);
 assert.equal(after.winner,'player');
 assert.equal(takeTurn(after,'Atacar'),after);
});
