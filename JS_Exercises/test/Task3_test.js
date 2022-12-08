import * as assert from 'assert';
import {canExecuteFastAttack} from '../Task3_methodes2/Spygame.js';
import {canSpy} from '../Task3_methodes2/Spygame.js';
import {canSignalPrisoner} from '../Task3_methodes2/Spygame.js';
import {canFreePrisoner} from '../Task3_methodes2/Spygame.js';



describe('canExecuteFastAttack', () => {

    const knightIsAwake = true;
    const expected = false;

    describe('Test', function () {
      it('can execute fast attack > when the knight is awake', function () {
        assert.equal(expected, canExecuteFastAttack(knightIsAwake));
      });
    });
  });

describe('canSpy', () => {

    const knightIsAwake = true;
    const archerIsAwake = false;
    const prisonerIsAwake = true;
    const expected = true;

    describe('Test', function () {
      it('can spy > when only the archer is asleep', function () {
        assert.equal(expected, canSpy(knightIsAwake, archerIsAwake, prisonerIsAwake));
      });
    });
  });


  describe('canSignalPrisoner', () => {

    const archerIsAwake = true;
    const prisonerIsAwake = false;
    const expected = false;

    describe('Test', function () {
      it('can signal prisoner > when only the archer is awake', function () {
        assert.equal(expected, canSignalPrisoner(archerIsAwake, prisonerIsAwake));
      });
    });
  });

  describe('canFreePrisoner', () => {

    const knightIsAwake = true;
    const archerIsAwake = false;
    const prisonerIsAwake = true;
    const petDogIsPresent = false;
    const expected = false;

    describe('Test', function () {
      it('can free prisoner > when only the archer is asleep and pet dog is not present', function () {
        assert.equal(expected, canFreePrisoner(
            knightIsAwake,
            archerIsAwake,
            prisonerIsAwake,
            petDogIsPresent));
      });
    });
  });
