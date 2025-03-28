const chai = require('chai');
const request = require('request');
const { expect } = chai;

describe('API Tests', function () {
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

  describe('GET /cart/:id', function() {
    it('should return status 200 when :id is a number', function(done) {
      request(`${url}/cart/123`, function(error, response, body) {
        expect(response.statusCode).to.equal(200);
        done();
      });
    });
    it('should return Payment methods for cart :id', function(done) {
      request(`${url}/cart/123`, function(error, response, body) {
        expect(body).to.equal('Payment methods for cart 123');
        done();
      });
    });
    it('should return status 404 when :id is NOT a number', function(done) {
      request(`${url}/cart/abc`, function(error, response, body) {
        expect(response.statusCode).to.equal(404);
        done();
      });
    });
    it('should return Not Found message when :id is NOT a number', function(done) {
      request(`${url}/cart/abc`, function(error, response, body) {
        expect(body).to.equal('Not Found');
        done();
      });
    });
  });

  describe('GET /available_payments', function() {
    it('should return status 200', function(done) {
      request(`${url}/available_payments`, function(error, response, body) {
        expect(response.statusCode).to.equal(200);
        done();
      });
    });
    it('should return the available payment methods', function(done) {
      request(`${url}/available_payments`, function(error, response, body) {
        const paymentMethods = JSON.parse(body);
        expect(paymentMethods).to.deep.equal({
          payment_methods: {
            credit_cards: true,
            paypal: false
          }
        });
        done();
      });
    });
  });

  describe('POST /login', function() {
    it('should return status 200 with valid username', function(done) {
      request.post(`${url}/login`, { json: { userName: 'testuser' } }, function(error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome testuser');
        done();
      });
    });
    it('should return status 400 without username', function(done) {
      request.post(`${url}/login`, { json: {} }, function(error, response, body) {
        expect(response.statusCode).to.equal(400);
        expect(body).to.equal('Bad Request: username is required');
        done();
      });
    });
  });
});