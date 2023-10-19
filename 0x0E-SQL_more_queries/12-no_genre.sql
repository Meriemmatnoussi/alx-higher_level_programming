-- Import the database dump from hbtn_0d_tvshows to your MySQL server: download (same as 11-genre_id_all_shows.sql)
SELECT tvs.title, tvsg.genre_id
FROM tv_shows AS tvs
LEFT JOIN tv_show_genres AS tvsg
ON tvs.id=tvsg.show_id
WHERE tvsg.genre_id IS NULL
ORDER BY tvs.title, tvsg.genre_id;
