import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  logLevel: 'info',

  server: {
    port:4000,
    proxy: {
      '^/api': {
        //idk why this works ??
        target: 'http://localhost:4001/tasks',
        changeOrigin: true,
        rewrite: (path) => path.replace('^/api', '/')
      }
    },
  },
  plugins: [vue()]

})

