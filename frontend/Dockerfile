ARG vite_api_base_url

FROM node:18-alpine3.17 AS builder
ARG vite_api_base_url
ENV VITE_API_BASE_URL=$vite_api_base_url
WORKDIR /app
COPY ./app/package.json ./
COPY ./app/package-lock.json ./
RUN npm i
COPY ./app ./
RUN npm run build

FROM nginx:1.23.4-bullseye
COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=builder /app/dist/ ./app
RUN find /app -type d -exec chmod 755 {} \; && \
    find /app -type f -exec chmod 644 {} \;
