function getPaymentTokenFromAPI(success) {
    if (success) {
        return Promise.resolve({ data: 'Successful response from the API' });
    }
    // when success is false, the function is doing nothing
}

module.exports = getPaymentTokenFromAPI;