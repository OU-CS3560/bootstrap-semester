FROM node:alpine AS builder
WORKDIR /app
COPY ./app/package.json ./
COPY ./app/package-lock.json ./
RUN npm i
COPY ./app ./
RUN npm run build

FROM nginx:latest
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=builder /app/dist/ ./app
