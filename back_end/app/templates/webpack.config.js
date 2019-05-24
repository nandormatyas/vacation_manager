const path = require('path')
const BundleTracker  = require('webpack-bundle-tracker');

module.exports = {
  mode: 'development',
  entry: {
    calendar: './src/example.js'
  },
  resolve: {
    extensions: [ '.js' ]
  },
  output: {
    filename: 'example.js',
    path: path.join(__dirname, 'dist')
  },
  plugins: [
    new BundleTracker({path: __dirname, filename: './assets/webpack-stats.json'})
  ],
  devtool: 'sourcemap'
}
