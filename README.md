# Youtube Videos API using Django


### 1. Get Videos API

```
GET 'http://127.0.0.1:8000/youtube/getVideos?page_limit=15'
```

### 2. Search Videos API

```
GET 'http://127.0.0.1:8000/youtube/searchVideos?query=cricket'
```

### 3. Add Auth Key API

```
POST 'http://127.0.0.1:8000/youtube/addAuthKey'
Body:
{
    "auth_key": "your_key"
}
```

# To run the Project
- Install the required packages from requirements.txt
- Setup Postgres locally
- Install and run Celery for background tasks

# Dashboard to see all the stored videos
You can use the Django admin portal for viewing the videos list, filtering, sorting, etc.#   f a m  
 #   f a m  
 