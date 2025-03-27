const { expect } = require('chai');
const calculateNumber = require('./2-calcul_chai');

describe('calculateNumber', function() {
    describe('SUM operation', function() {
      it('should return the rounded sum of two numbers', function() {
        expect(calculateNumber('SUM', 1.4, 4.5)).to.equal(6);
      });
    });
  
    describe('SUBTRACT operation', function() {
      it('should return the rounded difference of two numbers', function() {
        expect(calculateNumber('SUBTRACT', 1.4, 4.5)).to.equal(-4);
      });
    });
  
    describe('DIVIDE operation', function() {
      it('should return the rounded quotient of two numbers', function() {
        expect(calculateNumber('DIVIDE', 1.4, 4.5)).to.equal(0.2);
      });
  
      it('should return Error if the rounded divisor is 0', function() {
        expect(calculateNumber('DIVIDE', 1.4, 0)).to.equal('Error');
      });
    });
  });