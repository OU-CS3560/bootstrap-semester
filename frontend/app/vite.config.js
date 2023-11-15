import { defineConfig, splitVendorChunkPlugin } from "vite";
import react from "@vitejs/plugin-react";

// https://vitejs.dev/config/
export default defineConfig({
  build: {
    sourcemap: "inline",
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.includes("react-router-dom") || id.includes("react-router")) {
            return '@react-router';
          } else if (id.includes("bootstrap") || id.includes("popperjs")) {
            return "@bootstrap";
          } else if (id.includes("axios")) {
            return "@axios";
          } else if (id.includes("react")) {
            return "@react";
          }
        }
      }
    }
  },
  plugins: [react(), splitVendorChunkPlugin()],
});
