// * Endpoint => The resource you're trying to access

// * Request method => GET, POST, PUT, DELETE, OPTIONS, PATCH, HEAD...

// * GET => Retrieves data from the server
// * POST => Send data to the server
// * DELETE => Deletes an item from the database/server
// * PUT/PATCH => Update an item on the server

// create a base url

const baseURL = "https://jsonplaceholder.typicode.com";

// Get all users

const getUsers = () => {
  fetch(`${baseURL}/users`)
    .then((response) => response.json())
    .then((data) => {
      const users = data;

      console.log(users[0].username);
      console.log(users[0].address.city);
    })
    .catch((error) => console.error(error?.message));
};

getUsers();

// Get a single user

/**
 * @param {number} userId id of the user to return
 * @returns {User} A single entity of the user object
 */

const getUser = (userId) => {
  fetch(`${baseURL}/users/${userId}`)
    .then((response) => response.json())
    .then((data) => {
      console.log(data);
    })
    .catch((error) => console.error(error));
};

getUser(8);
