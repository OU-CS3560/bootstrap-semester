# Backend

## Local Development

Copy `.env.sample` as `.env` and fill in the value for the variables.

The development server can then be started with

```console
$ export $(cat .env)
$ python -m uvicorn app.main:app --host 0.0.0.0 --port 3000
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
