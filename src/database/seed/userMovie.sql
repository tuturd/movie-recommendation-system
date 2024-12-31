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
