# Threads
Create, retrieve, update and delete operations for Thread

## Get all threads information

**Request**:

`GET` `/api/v1/threads/`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "created": "2020-03-31T13:20:53+0000",
            "modified": "2020-03-31T13:33:26+0000",
            "is_draft": false,
            "is_sticky": false,
            "board": 1
        },
        {
            "id": 2,
            "created": "2020-03-31T13:34:17+0000",
            "modified": "2020-03-31T13:34:17+0000",
            "is_draft": false,
            "is_sticky": false,
            "board": 1
        }
    ]
}
```

## Get specific thread data

**Request**:

`GET` `/api/v1/threads/:id/`

*Note:*
- **[Authorization Protected](authentication.md)**

**Response**:

```json
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 1,
    "created": "2020-03-31T13:20:53+0000",
    "modified": "2020-03-31T16:02:05+0000",
    "is_draft": false,
    "is_sticky": true,
    "board": 1
}
```

## Get all posts in a specific thread

**Request**:

`GET` `/api/v1/threads/:id/posts/`

*Note:*
- **[Authorization Protected](authentication.md)**

**Response**:

```json
HTTP 200 OK
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "count": 2,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 2,
            "created": "2020-03-31T13:33:26+0000",
            "modified": "2020-03-31T13:33:26+0000",
            "description": "asdasd",
            "is_draft": false,
            "thread": 1,
            "publisher": 2
        },
        {
            "id": 3,
            "created": "2020-03-31T13:33:34+0000",
            "modified": "2020-03-31T13:33:34+0000",
            "description": "test",
            "is_draft": true,
            "thread": 1,
            "publisher": 2
        }
    ]
}
```

## Add a post in a thread

**Request**:

`POST` `/api/v1/threads/:id/posts/`

*Note:*
- **[Authorization Protected](authentication.md)**

**Response**:

```json
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 3,
    "created": "2020-03-31T13:33:34+0000",
    "modified": "2020-03-31T13:33:34+0000",
    "description": "test",
    "is_draft": true,
    "thread": 1,
    "publisher": 2
}
```

## Mark thread as sticky

**Request**:

`POST` `/api/v1/threads/:id/mark_as_sticky/`

*Note:*
- **[Authorization Protected](authentication.md)**
- **[Administrator Protected]()**

**Response**:

```json
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "status": "Thread - 1 marked as sticky"
}
```
