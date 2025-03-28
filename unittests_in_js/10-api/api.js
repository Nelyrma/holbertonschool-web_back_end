const express = require('express');
const bodyParser = require('body-parser');
const app = express();
const port = 7865;

app.use(bodyParser.json());

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
});

app.get('/cart/:id', (req, res) => {
    const cartId = req.params.id;
    if (!isNaN(cartId)) {
      res.send(`Payment methods for cart ${cartId}`);
    } else {
      res.status(404).send('Not Found');
    }
});

app.get('/available_payments', (req, res) => {
  res.json({
    payment_methods: {
      credit_cards: true,
      paypal: false
    }
  });
});

app.post('/login', (req, res) => {
  const username = req.body.userName;
  if (username) {
    res.send(`Welcome ${username}`);
  } else {
    res.status(400).send('Bad Request: username is required');
  }
});

app.listen(port, () => {
    console.log(`API available on localhost port ${port}`)
});