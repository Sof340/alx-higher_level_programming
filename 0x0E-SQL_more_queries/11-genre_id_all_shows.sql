-- a script that lists all shows contained in the database hbtn_0d_tvshows.
SELECT s.title,IF(g.genre_id IS NULL, NULL, g.genre_id) AS genre_id FROM tv_shows s LEFT JOIN tv_show_genres g ON s.id=g.show_id ORDER BY s.title, g.genre_id ASC;
