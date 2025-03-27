const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('calculateNumber', function() {
  describe('SUM', function() {
    it('Checks 1 + 3', function() {
      assert.equal(calculateNumber('SUM', 1, 3), 4);
    });
    it('Checks 1 + 3.7', function() {
      assert.equal(calculateNumber('SUM', 1, 3.7), 5);
    });
    it('Checks 1.2 + 3.7', function() {
      assert.equal(calculateNumber('SUM', 1.2, 3.7), 5);
    });
    it('Checks 1.4 + 4.5', function() {
      assert.equal(calculateNumber('SUM', 1.4, 4.5), 6);
    });
    it('Checks -3 + 1.2', function() {
      assert.equal(calculateNumber('SUM', -3, 1.2), -2);
    });
  });

  describe('SUBTRACT', function() {
    it('Checks 3 - 1', function() {
      assert.equal(calculateNumber('SUBTRACT', 3, 1), 2);
    });
    it('Checks 1.4 - 4.5', function() {
      assert.equal(calculateNumber('SUBTRACT', 1.4, 4.5), -4);
    });
    it('Checks 1.2 - 3.7', function() {
      assert.equal(calculateNumber('SUBTRACT', 1.2, 3.7), -3);
    });
    it('Checks 3.7 - 1.5', function() {
      assert.equal(calculateNumber('SUBTRACT', 3.7, 1.5), 2);
    });
    it('Checks 0.1 - 0.1', function() {
      assert.equal(calculateNumber('SUBTRACT', 0.1, 0.1), 0);
    });
  });

  describe('DIVIDE', function() {
    it('Checks 3 / 1', function() {
      assert.equal(calculateNumber('DIVIDE', 3, 1), 3);
    });
    it('Checks 3.5 / 2.1', function() {
      assert.equal(calculateNumber('DIVIDE', 3.5, 2.1), 2);
    });
    it('Checks 1.4 / 4.5', function() {
      assert.equal(calculateNumber('DIVIDE', 1.4, 4.5), 0.2);
    });
    it('Checks 1.4 / 0', function() {
      assert.equal(calculateNumber('DIVIDE', 1.4, 0), 'Error');
    });
    it('Checks 0.1 / 0.1', function() {
      assert.equal(calculateNumber('DIVIDE', 0.1, 0.1), 1);
    });
  });
});
