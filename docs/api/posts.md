# Posts
Create, retrieve, update and delete operations for Post

## Get all posts information

**Request**:

`GET` `/api/v1/posts/`

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
    "count": 3,
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

## Get specific post data

**Request**:

`GET` `/api/v1/posts/:id/`

*Note:*
- **[Authorization Protected](authentication.md)**

**Response**:

```json
HTTP 200 OK
Allow: GET, PUT, PATCH, DELETE, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "id": 2,
    "created": "2020-03-31T13:33:26+0000",
    "modified": "2020-03-31T13:33:26+0000",
    "description": "asdasd",
    "is_draft": false,
    "thread": 1,
    "publisher": 2
}
```
