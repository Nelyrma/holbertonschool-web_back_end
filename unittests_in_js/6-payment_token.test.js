const { expect } = require('chai');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function () {
    it('should return successful response when success is true', function (done) {
        getPaymentTokenFromAPI(true)
            .then(response => {
                expect(response).to.include({ data: 'Successful response from the API' });
                done(); // calling done to indicate that the test is finished
            })
            .catch(done); // if there is an error, pass the error to done to fail the test
    });
});