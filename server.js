const mongoose = require('mongoose') 
require("dotenv").config()
const connectDB = mongoose.connect(process.env.MONGODB,)
.then(() => {
    console.log("mongoose connected");
  })
  .catch((err) => {
    console.log("mongoose connect error");
    console.log(err);

  })


const express = require('express');
const http = require("http")
const app = express();
const path = require('path')
const concetDB = require("./config/config");
const randomstring = require('randomstring');
const nodemailer = require("nodemailer");
const multer = require('multer');
const morgan = require("morgan")

const server = http.createServer(app);

const userRoute = require('./router/userRoute')
const adminRoute = require('./router/adminRoute')

app.use(function (err, req, res, next) {
  console.error(err.stack)
  res.status(500).send('Something went wrong!')
})
// Define a route for the root URL
app.set("view engine", "ejs");
app.set('views',  [
  path.join(__dirname, 'views', 'admin'),
  path.join(__dirname, 'views', 'user'),

])

app.use(express.static(path.join(__dirname, 'public/user/user-assets')))
app.use(express.static(path.join(__dirname, 'public/admin')))

app.use(express.urlencoded({ extended: true }))
app.use(express.json());
app.use(express.static("public"))
app.use(morgan("dev"))
app.use('/', userRoute)
app.use('/admin', adminRoute)

const port = process.env.PORT || 3000
server.listen(port, () => {
  console.log("Listening to the server on http://localhost:" + port);
});

