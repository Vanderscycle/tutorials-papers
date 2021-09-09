module.exports = {
  devServer: {
    proxy: {
      '^/api': {
        target: 'http://localhost:4001',
        changeOrigin: true,
        logLevel: 'debug',
        pathRewrite: {'^/api': ''}
      }
    }
  }
}
