const chai = require('chai');
const request = require('request');
const { expect } = chai;

describe('API Tests', function() {
  const url = 'http://localhost:7865';

  describe('GET /', function() {
    it('should return status 200', function(done) {
      request(url, function(error, response, body) {
        expect(response.statusCode).to.equal(200);
        done();
      });
    });

    it('should return Welcome to the payment system', function(done) {
      request(url, function(error, response, body) {
        expect(body).to.equal('Welcome to the payment system');
        done();
      });
    });

    it('should return content type text/html', function(done) {
      request(url, function(error, response, body) {
        expect(response.headers['content-type']).to.include('text/html');
        done();
      });
    });
  });
});