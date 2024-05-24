-- a script that uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter.
SELECT g.name
FROM tv_genres g
WHERE NOT EXISTS (
    SELECT 1
    FROM tv_show_genres gs
    JOIN tv_shows s ON s.id = gs.show_id
    WHERE g.id = gs.genre_id
      AND s.title = 'Dexter'
)
ORDER BY g.name ASC;
