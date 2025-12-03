FROM node:22-alpine

WORKDIR /app

# package.jsonとpackage-lock.jsonをコピー
COPY package*.json ./

# Install all dependencies (including devDependencies) so the build step has vite/vue-tsc available
RUN npm ci

# アプリケーションコードのコピー
COPY . .

# ビルド
RUN npm run build

# ポートの公開
EXPOSE 3000

# アプリケーションの起動: bind to 0.0.0.0 and use port 3000 so Docker port mapping works
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0", "--port", "3000"]