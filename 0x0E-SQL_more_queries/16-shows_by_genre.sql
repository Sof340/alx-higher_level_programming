-- a script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
SELECT s.title,IF(g.genre_id IS NULL, NULL, r.name) AS genre FROM tv_shows s LEFT JOIN tv_show_genres g ON s.id=g.show_id LEFT JOIN tv_genres r ON r.id=g.genre_id ORDER BY s.title, genre ASC;
