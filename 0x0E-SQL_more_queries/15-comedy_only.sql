-- a script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT s.title FROM tv_genres g LEFT JOIN tv_show_genres gs ON g.id=gs.genre_id LEFT JOIN tv_shows s ON s.id= gs.show_id WHERE g.name="Comedy" ORDER BY s.title ASC;
