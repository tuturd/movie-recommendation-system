CREATE TABLE IF NOT EXISTS user (
    id INTEGER PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL,
    birthDate TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS genre (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS director (
    id INTEGER PRIMARY KEY,
    firstname VARCHAR(50) NOT NULL,
    lastname VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS movie (
    id INTEGER PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    releaseDate TIMESTAMP NOT NULL,
    genreId INT NOT NULL,
    directorId INT NOT NULL,
    price INT NOT NULL,
    FOREIGN KEY (genreId) REFERENCES genre(id),
    FOREIGN KEY (directorId) REFERENCES director(id)
);

CREATE TABLE IF NOT EXISTS userMovie (
    id INTEGER PRIMARY KEY,
    userId INT NOT NULL,
    movieId INT NOT NULL,
    rating INT NOT NULL,
    sold BOOLEAN NOT NULL,
    saleDate TIMESTAMP,
    FOREIGN KEY (userId) REFERENCES user(id),
    FOREIGN KEY (movieId) REFERENCES movie(id)
);

