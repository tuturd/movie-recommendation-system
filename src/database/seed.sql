CREATE TABLE IF NOT EXISTS user (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS genre (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS director (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS movie (
    id SERIAL PRIMARY KEY,
    title VARCHAR(50) NOT NULL,
    release_date TIMESTAMP NOT NULL,
    genreId INT NOT NULL,
    directorId INT NOT NULL,
    price INT NOT NULL,
    FOREIGN KEY (genreId) REFERENCES genre(id),
    FOREIGN KEY (directorId) REFERENCES director(id)
);

CREATE TABLE IF NOT EXISTS userMovie (
    id SERIAL PRIMARY KEY,
    userId INT NOT NULL,
    movieId INT NOT NULL,
    rating INT NOT NULL,
    sold BOOLEAN NOT NULL,
    saleDate TIMESTAMP,
    FOREIGN KEY (userId) REFERENCES user(id),
    FOREIGN KEY (movieId) REFERENCES movie(id)
);