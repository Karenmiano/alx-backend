const util = require("util");

const person = {
  name: "John",
  sayName() {
    console.log(`My name is ${this.name}`);
  },
};

// Promisify the sayName method
const sayNameAsync = util.promisify(person.sayName).bind(person);

// Call the promisified method
sayNameAsync().catch((err) => console.error(err));
