# Requirement

## Instagram Data API Structure

### Posting Data
```json
{
    "timestamp_added": timestamp,
    "like_count": int,
    "comment_count": int,
    "comment_data": [
        {
            "user_id": id_1,
            "comments" : "this is example of comment"
        },
        ...
        {
            "user_id": id_n,
            "comment" : "this is example of comment"
        }
    ]
}
```

## Data Requirement

1. Followers growth
2. Profile visit
3. Like
4. Comment

## Data Characteristic

- Historis (time-series)

## Data Flow Diagram

### Level 0 DFD

- Sosial Media Instagram Dashboard

### Level 1 DFD

- Melihat data historis followers growth dalam periode tertentu
- Melihat data historis like dan comment dalam periode tertentu
- Melihat daftar post yang memiliki jumlah like terbanyak
- Melihat daftar post yang memiliki jumlah comment terbanyak
- Mendapatkan daftar kata pada komentar di sebuah post
- Melakukan cron scheduler untuk mendapatkan data terkait perkembangan sebuah postin
- Melakukan training data pada data historis follower, like dan/atau comment