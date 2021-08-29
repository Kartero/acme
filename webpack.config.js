const path = require('path');
const { VueLoaderPlugin } = require('vue-loader')

module.exports = {
    entry: './src/index.js',
    output: {
      filename: 'main.js',
      path: path.resolve(__dirname, 'acme/static/js/'),
    },
    mode: 'development',
    resolve: {
      alias: {
        vue: 'vue/dist/vue.esm-bundler.js'
      }
    },
    module: {
      rules: [
        {
          test: /\.vue$/,
          loader: 'vue-loader'
        }
      ]
    },
    plugins: [
      new VueLoaderPlugin()
  ]
  };