import * as assert from 'assert';
import 'chai/register-expect'; 
import {remainingMinutesInOven} from '../Task2_methodes/Lasagna.js';
import {preparationTimeInMinutes} from '../Task2_methodes/Lasagna.js';
import {totalTimeInMinutes} from '../Task2_methodes/Lasagna.js';

/* const lasagna = new Lasagna();
lasagna.EXPECTED_MINUTES_IN_OVEN = 40;  */

describe('remainingMinutesInOven', () => {
  describe('Test', function () {
    it('return expected minutes', function () {
      assert.equal(40, remainingMinutesInOven(0));
    });
  });
});

describe('prepTime', () => {
    describe('Test', function () {
      it('return prepTime per Layer', function () {
        assert.equal(2, preparationTimeInMinutes(1));
      });
    });
  });

  describe('totalTimeInMinutes', () => {
    describe('Test', function () {
      it('return total time of lasagna cooking', function () {
        assert.equal(7, totalTimeInMinutes(1, 5));
      });
    });
  });