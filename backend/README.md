# Backend

## Local Development

Copy `.env.sample` as `.env` and fill in the value for the variables.

The development server can then be started with

```console
$ ./scripts/start-local.sh
```

(Note that the `./scripts/start.sh` is tightly coupled with the container).

To unset the variable use the `unset NAME` command.

## Run tests

```console
$ rm -f test.db; ./scripts/test.sh
```

## Note

### Endpoint Testing Commands

Use the interactive API docs at `/docs` or curl.

```console
curl -X POST http://localhost:8000/classrooms/ \
  -H "Content-Type: application/json" \
  -d '{"name": "CS3560 Spring 2022-2023", "begin_date": "2023-01-01T00:00-0400", "end_date": "2023-05-05T00:00-0400"}'
```

### Manually inspect DB (sqlite)

```console
$ sqlite3 filename
> .headers on
> .mode column
> .tables
> select * from student;
> ...
> .q
```

### Create database migration revision

Create a revision.

```console
$ alembic revision --autogenerate -m "change type of datetime"
```

The `--autogenerate` can fail, so be sure to double check the generated file.

Upgrade the database to a revision `<id>`.

```console
$ alembic upgrade <id>
```

Use `--sql` to create "offline migration" (an sql file).

Resetting the database.

```console
$ alembic downgrade base
```
