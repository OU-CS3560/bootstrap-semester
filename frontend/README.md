# Frontend

The client-side of the system. The containerized version also
host the Nginx to serve the static files and act as a reverse proxy
for the API.

## Local Development

Copy `app/.env.sample` as `app/.env.development.local` and fill in the correct value
for `VITE_API_BASE_URL`.

```console
$ cd app
$ npm install
$ npm run dev
```

vite will only listen to loop back address of IPv6 if it is available, so
please use `http://[::1]:5173` if `http://localhost:5173` show error
(e.g. unable to connect)
