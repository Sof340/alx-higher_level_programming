-- a script that lists all shows from hbtn_0d_tvshows_rate by their rating
SELECT s.title,SUM(sg.rate) AS rating FROM tv_shows s LEFT JOIN tv_show_ratings sg ON s.id=sg.show_id GROUP BY s.title ORDER BY rating DESC;
