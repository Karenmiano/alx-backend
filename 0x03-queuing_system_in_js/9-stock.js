import express from "express";
import redis from "redis";
import util from "util";

const app = express();
const listProducts = [
  { Id: 1, name: "Suitcase 250", price: 50, stock: 4 },
  { Id: 2, name: "Suitcase 450", price: 100, stock: 10 },
  { Id: 3, name: "Suitcase 650", price: 350, stock: 2 },
  { Id: 4, name: "Suitcase 1050", price: 550, stock: 5 },
];

function getItemById(id) {
  return listProducts.find((item) => item.Id === id);
}

const client = redis.createClient();
const redisGet = util.promisify(client.get).bind(client);

function reserveStockById(itemId, stock) {
  client.set(itemId, stock);
}

async function getCurrentReservedStockById(itemId) {
  try {
    const stock = await redisGet(itemId);
    return stock;
  } catch (error) {
    throw error;
  }
}

app.get("/list_products", (req, res) => {
  const products = listProducts.map((product) => {
    return {
      itemId: product.Id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock,
    };
  });
  res.write(products);
  res.end();
});

app.get("/list_products/:itemId", (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(itemId);
  if (product === undefined) {
    res.write({ status: "Product not found" });
    res.end();
  }
  const stock = product.stock - getCurrentReservedStockById(itemId);
  const productWithStock = { ...product, currentQuantity: stock };
  res.write(productWithStock);
  res.end();
});

app.get("/reserve_product/:itemId", (req, res) => {
  const { itemId } = req.params;
  const product = getItemById(itemId);
  if (product === undefined) {
    res.write({ status: "Product not found" });
    res.end();
  }
});

app.listen(1245);
