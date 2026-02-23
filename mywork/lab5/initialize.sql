USE xak2wm_db;
CREATE TABLE artists (
    artist_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(40),
    home_country VARCHAR(20)
);

CREATE TABLE songs (
    songid INT PRIMARY KEY AUTO_INCREMENT,
    song_name TEXT,
    genre VARCHAR(30),
    artist_id INT
);

INSERT INTO artists (name, home_country) VALUES ('Taylor Swift', 'USA');
INSERT INTO artists (name, home_country) VALUES ('Role Model', 'USA');
INSERT INTO artists (name, home_country) VALUES ('Bad Bunny', 'Puerto Rico');
INSERT INTO artists (name, home_country) VALUES ('Adele', 'UK');
INSERT INTO artists (name, home_country) VALUES ('Peter McPoland', 'USA');
INSERT INTO artists (name, home_country) VALUES ('Shakira', 'Colombia');
INSERT INTO artists (name, home_country) VALUES ('Ed Sheeran', 'UK');
INSERT INTO artists (name, home_country) VALUES ('Rihanna', 'Barbados');
INSERT INTO artists (name, home_country) VALUES ('Bruno Mars', 'USA');
INSERT INTO artists (name, home_country) VALUES ('Billie Eilish', 'USA');

INSERT INTO songs (song_name, genre, artist_id) VALUES ('Love Story', 'Pop', 1);
INSERT INTO songs (song_name, genre, artist_id) VALUES ('Frances', 'Pop', 2);
INSERT INTO songs (song_name, genre, artist_id) VALUES ('Tití Me Preguntó', 'Reggaeton', 3);
INSERT INTO songs (song_name, genre, artist_id) VALUES ('Hello', 'Pop', 4);
INSERT INTO songs (song_name, genre, artist_id) VALUES ('I Love The Animals', 'Alternative', 5);
INSERT INTO songs (song_name, genre, artist_id) VALUES ('Hips Dont Lie', 'Latin Pop', 6);
INSERT INTO songs (song_name, genre, artist_id) VALUES ('Shape of You', 'Pop', 7);
INSERT INTO songs (song_name, genre, artist_id) VALUES ('Umbrella', 'R&B', 8);
INSERT INTO songs (song_name, genre, artist_id) VALUES ('Uptown Funk', 'Funk', 9);
INSERT INTO songs (song_name, genre, artist_id) VALUES ('Bad Guy', 'Pop', 10);

