import * as assert from 'assert'; 
import {hello} from '../Task1_Beginning/Beginning.js';


describe('hello', () => {
  describe('Test', function () {
    it('soll Hello World ausgeben', function () {
      assert.equal(hello(), "Hello, World!");
    });
  });
});

