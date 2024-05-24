-- a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT g.name AS genre,COUNT(*) AS number_of_shows FROM tv_genres g LEFT JOIN tv_show_genres gs ON g.id=gs.genre_id LEFT JOIN tv_shows s ON s.id= gs.show_id GROUP BY genre ORDER BY number_of_shows DESC;
