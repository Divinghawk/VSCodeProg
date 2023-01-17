import * as assert from 'assert';
import {twoFer} from './two-fer.ts';

const expected = 'One for you, one for me.'
expect(twoFer()).toEqual(expected)