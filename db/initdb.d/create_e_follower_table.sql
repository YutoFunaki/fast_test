CREATE TABLE followers (
    following_id BIGINT UNSIGNED,
    followed_id BIGINT UNSIGNED,
    FOREIGN KEY (following_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (followed_id) REFERENCES users(id) ON DELETE CASCADE,
    PRIMARY KEY (following_id, followed_id)
);