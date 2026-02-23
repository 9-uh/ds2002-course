USE xak2wm_db;

SELECT artists.name, songs.song_name, songs.genre
FROM artists LEFT JOIN songs ON artists.artist_id = songs.artist_id
WHERE songs.genre = 'Pop';
