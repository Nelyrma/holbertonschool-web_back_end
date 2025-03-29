import express from 'express';
import  { createClient } from 'redis';
import { promisify } from 'util';

const listProducts = [
    {
        id: 1,
        name: 'Suitcase 250',
        price: 50,
        stock: 4
    },
    {
        id: 2,
        name: 'Suitcase 450',
        price: 100,
        stock: 10
    },
    {
        id: 3,
        name: 'Suitcase 650',
        price: 350,
        stock: 2
    },
    {
        id: 4,
        name: 'Suitcase 1050',
        price: 550,
        stock: 5
    }
];

function getItemById(id) {
    return (listProducts.find((item) => item.id === id));
}

const client = createClient();

client.on('error', (error) => console.log('Redis client not connected to the server: ' + error.toString()));

function reserveStockById(itemId, stock) {
    client.set(getItemById(itemId).id, stock, (error, reply) => {
        if (error) throw error;
    });
}

const get = promisify(client.get).bind(client);

async function getCurrentReservedStockById(itemId) {
    const result = await get(itemId);
    return (result);
}

const app = express();
const port = 1245;

app.get('/list_products', (req, res) => {
    const availableProducts = listProducts.map((item) => {
        return {
          itemId: item.id,
          itemName: item.name,
          price: item.price,
          initialAvailableQuantity: item.stock
        }
    });
    res.send(availableProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
    const { itemId } = req.params;
    const item = getItemById(Number(itemId));
    if (item === undefined) {
        res.status(404);
        res.send({"status":"Product not found"});
    } else {
        let stock = await getCurrentReservedStockById(itemId);
        if (stock === null) stock = item.stock;
        const result = {
          itemId: item.id,
          itemName: item.name,
          price: item.price,
          initialAvailableQuantity: item.stock,
          currentQuantity: stock
        }
        res.send(result);
    }
});

app.get('/reserve_product/:itemId', async (req, res) => {
    const { itemId } = req.params;
    const item = getItemById(Number(itemId));
    if (item === undefined) {
        res.status(404);
        res.send({"status":"Product not found"});
    } else {
        let stock = await getCurrentReservedStockById(itemId);
        if (stock === null) stock = item.stock;
        if (stock < 1) {
            res.send({"status":"Not enough stock available","itemId":item.id})
        } else {
            reserveStockById(item.id, stock - 1);
            res.send({"status":"Reservation confirmed","itemId":item.id});
        }
    }
});

app.listen(port, () => {
    console.log('API available on localhost port 1245');
});