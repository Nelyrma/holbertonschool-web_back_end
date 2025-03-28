const sinon = require('sinon');
const assert = require('assert');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('sendPaymentRequestToApi', function() {
  it('should call Utils.calculateNumber with correct arguments', function() {
    const calculateNumberStub = sinon.stub(Utils, 'calculateNumber').returns(10);
    const consoleLogSpy = sinon.spy(console, 'log');
    sendPaymentRequestToApi(100, 20);
    assert(calculateNumberStub.calledOnceWithExactly('SUM', 100, 20));
    assert(consoleLogSpy.calledOnceWithExactly('The total is: 10'))
    consoleLogSpy.restore();
  });
});