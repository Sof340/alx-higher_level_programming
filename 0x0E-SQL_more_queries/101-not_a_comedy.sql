-- a script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT s.title
FROM tv_shows s
WHERE NOT EXISTS (
    SELECT 1
    FROM tv_show_genres gs
    JOIN tv_genres g ON g.id = gs.genre_id
    WHERE s.id = gs.show_id
      AND g.name = 'Comedy'
)
ORDER BY s.title ASC;
