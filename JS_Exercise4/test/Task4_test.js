import * as assert from 'assert';
import {dayRate} from '../Task4_FreelancerRates.js';



describe('dayRate', () => {

    const actual = dayRate(16);

    describe('Test', function () {
      it('day rate > at 16/hour', function () {
        assert.equal(actual, dayRate(128));
      });
    });
  });