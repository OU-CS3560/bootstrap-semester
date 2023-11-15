# A Manangement System

A system designed primarily for managing term project checkpoints
of CS3560 class that is offered at [Ohio University](https://www.ohio.edu/).

## Deployment

### Traefik

If you alredy have a Traefik setup, you can skip this section.

Create a secure password for the Traefik's dashboard by running

```console
$ openssl passwd -apr1
```

You can then modify the password in the label of the traefik container in
`proxy.docker-compose.yml`. Please make sure that you escape `$` by using `$$`.


For example, here are the default accounts.

```yaml
- "traefik.http.middlewares.auth.basicauth.users=test:$$apr1$$/7fbNsNF$b9LFWJHm04.riZF007OLO.,test2:$$apr1$$d9hr9HBB$$4HxwgUir3HP4EsggP/QNo0"
```

which listed two accounts `test:test` and `test2:test2`.

Run the following command to start the Traefik container.

```console
$ docker compose -f proxy.docker-compose.yml up -d
```

If you need the debug container, run

```console
$ COMPOSE_PROFILES=debug docker compose -f proxy.docker-compose.yml up -d
```

### Application Servers

Create the `.env` file with the following content.

```plain
VITE_API_BASE_URL=http://mngt.docker.localhost/api
#SQLALCHEMY_DATABASE_URL=sqlite+aiosqlite:///./backend.db
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:example@db/postgres"
POSTGRES_PASSWORD=example
```

Replace the domain name in `http://mngt.docker.localhost/api` with the domain of your choice.
Keep in mind that the URL has to have the protocol (e.g. `http` or `https`). You can also
customize other variable if you want.

Then you can run

```console
$ docker compose up -d
```

to start the containers for the application.

Unless you change the domain name in the `-compose.yml` files, 
you can then visit [http://mngt.docker.localhost/](http://mngt.docker.localhost/) for a local
deployment or [http://mngt.daroka.kchusap.com/](http://mngt.daroka.kchusap.com/) for a production
deployment.

You can also visit [http://traefik.kchusap.com/dashboard/](http://traefik.kchusap.com/dashboard/)
for the Traefik's dashboard.

## Testing

