const sinon = require('sinon');
const assert = require('assert');
const Utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');

describe('sendPaymentRequestToApi', function () {
    let consoleLogSpy;

    beforeEach(function () {
        consoleLogSpy = sinon.spy(console, 'log');
    });
    afterEach(function () {
        consoleLogSpy.restore();
    });

    it('should log "The total is: 120" when calling with 100 and 20', function () {
        sendPaymentRequestToApi(100, 20);
        assert(consoleLogSpy.calledOnceWithExactly('The total is: 120'));
    });
    it('should log "The total is: 20" when calling with 10 and 10', function () {
        sendPaymentRequestToApi(10, 10);
        assert(consoleLogSpy.calledOnceWithExactly('The total is: 20'));
    });
});