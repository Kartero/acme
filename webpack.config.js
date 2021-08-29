const path = require('path');
module.exports = {
    entry: './src/index.js',
    output: {
      filename: 'main.js',
      path: path.resolve(__dirname, 'acme/static/js/'),
    },
    mode: 'development'
  };