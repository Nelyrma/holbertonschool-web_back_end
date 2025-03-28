const chai = require('chai');
const { expect } = chai;
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function() {
  it('Checks 1 + 3', function() {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
  });
  it('Checks 1 + 3.7', function() {
    expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
  });
  it('Checks 1.2 + 3.7', function() {
    expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5)
  });
  it('Checks 1.4 + 4.5', function() {
    expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
  });
  it('Checks -3 + 1.2', function() {
    expect(calculateNumber('SUM', -3, 1.2)).to.equal(-2);
  });
  it('Checks 3 - 1', function() {
    expect(calculateNumber('SUBTRACT', 3, 1)).to.equal(2);
  });
  it('Checks 1.4 - 4.5', function() {
    expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
  });
  it('Checks 1.2 - 3.7', function() {
    expect(calculateNumber('SUBTRACT', 1.2, 3.7)).to.equal(-3);
  });
  it('Checks 3.7 - 1.5', function() {
    expect(calculateNumber('SUBTRACT', 3.7, 1.5)).to.equal(2);
  });
  it('Checks 0.1 - 0.1', function() {
    expect(calculateNumber('SUBTRACT', 0.1, 0.1)).to.equal(0);
  });
  it('Checks 3 / 1', function() {
    expect(calculateNumber('DIVIDE', 3, 1)).to.equal(3);
  });
  it('Checks 3.5 / 2.1', function() {
    expect(calculateNumber('DIVIDE', 3.5, 2.1)).to.equal(2);
  });
  it('Checks 1.4 / 4.5', function() {
    expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
  });
  it('Checks 1.4 / 0', function() {
    expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
  });
  it('Checks 0.1 / 0.1', function() {
    expect(calculateNumber('DIVIDE', 0.1, 0.1)).to.equal('Error');
  });
});