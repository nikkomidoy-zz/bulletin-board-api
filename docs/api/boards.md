# Boards
Create, retrieve, update and delete operations for Board

## Get all boards information

**Request**:

`GET` `/api/v1/boards/`

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
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 1,
            "threads": [
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
            ],
            "posts": [
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
                },
                {
                    "id": 4,
                    "created": "2020-03-31T13:34:17+0000",
                    "modified": "2020-03-31T13:34:17+0000",
                    "description": "This is a post",
                    "is_draft": false,
                    "thread": 2,
                    "publisher": 2
                }
            ],
            "created": "2020-03-31T13:14:07+0000",
            "modified": "2020-03-31T13:14:07+0000",
            "name": "Board 1",
            "description": "",
            "is_draft": false
        }
    ]
}

```

## Get specific board data

**Request**:

`GET` `/api/v1/boards/:id/`

*Note:*
- **[Authorization Protected](authentication.md)**

**Response**:

```json
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "name": "Board 1",
    "description": "",
    "is_draft": false,
    "threads": [
        {
            "id": 1,
            "created": "2020-03-31T13:20:53+0000",
            "modified": "2020-03-31T16:02:05+0000",
            "is_draft": false,
            "is_sticky": true,
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
    ],
    "posts": [
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
        },
        {
            "id": 4,
            "created": "2020-03-31T13:34:17+0000",
            "modified": "2020-03-31T13:34:17+0000",
            "description": "This is a post",
            "is_draft": false,
            "thread": 2,
            "publisher": 2
        }
    ]
}
```

## Get all threads in a specific board

**Request**:

`GET` `/api/v1/boards/:id/threads/`

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
            "modified": "2020-03-31T16:02:05+0000",
            "is_draft": false,
            "is_sticky": true,
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

## Add a thread in a board

**Request**:

`POST` `/api/v1/boards/:id/threads/`

*Note:*
- **[Authorization Protected](authentication.md)**

**Response**:

```json
HTTP 201 Created
Allow: GET, POST, HEAD, OPTIONS
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
