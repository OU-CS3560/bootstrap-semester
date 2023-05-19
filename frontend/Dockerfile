FROM node:20-alpine3.17 AS builder
WORKDIR /app
COPY ./app/package.json ./
COPY ./app/package-lock.json ./
RUN npm i
COPY ./app ./
RUN npm run build
RUN find /app -type d -exec chmod 755 {} \; && \
    find /app -type f -exec chmod 644 {} \;

FROM nginx:1.23.4-bullseye
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /app/dist/ ./app
