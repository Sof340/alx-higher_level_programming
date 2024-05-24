-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
SELECT g.name,SUM(rate) AS rating FROM tv_genres g LEFT JOIN tv_show_genres gr ON g.id=gr.genre_id LEFT join tv_shows s ON gr.show_id=s.id LEFT JOIN tv_show_ratings gs ON s.id=gs.show_id GROUP BY g.name ORDER BY ratin
g DESC;
