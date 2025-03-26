const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('calculateNumber', function() {
    it('Checks 1 + 3', function() {
      assert.equal(calculateNumber(1, 3), 4);
    });
    it('Checks 1 + 3.7', function() {
      assert.equal(calculateNumber(1, 3.7), 5);
    });
    it('Checks 1.2 + 3.7', function() {
      assert.equal(calculateNumber(1.2, 3.7), 5);
    });
    it('Checks 1.5 + 3.7', function() {
      assert.equal(calculateNumber(1.5, 3.7), 6);
    });
    it('Checks -3 + 1.2', function() {
      assert.equal(calculateNumber(-3, 1.2), -2);
    });
});
