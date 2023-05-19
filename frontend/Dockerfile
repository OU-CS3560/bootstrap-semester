FROM node:20-alpine3.17 AS builder
WORKDIR /app
COPY ./app/package.json ./
COPY ./app/package-lock.json ./
RUN npm i
COPY ./app ./
RUN npm run build

FROM nginx:1.23.4-bullseye
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist/ ./app
