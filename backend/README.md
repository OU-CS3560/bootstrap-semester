# Backend

## Local Development

```console
$ uvicorn app.main:app --reload
```

## Run tests

```console
$ PYTHONPATH=. pytest
```

## Endpoint Testing Commands

```console
curl -X POST http://localhost:8000/classrooms/ \
  -H "Content-Type: application/json" \
  -d '{"name": "CS3560 Spring 2022-2023", "begin_date": "2023-01-01T00:00-0400", "end_date": "2023-05-05T00:00-0400"}'
```