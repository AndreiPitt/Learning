CREATE DATABASE gymdb;
USE gymdb;

CREATE TABLE frames (
    frame_id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL
);

CREATE TABLE objects (
    object_id INT AUTO_INCREMENT PRIMARY KEY,
    frame_id INT,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    FOREIGN KEY (frame_id) REFERENCES frames(frame_id) ON DELETE CASCADE
);

INSERT INTO frames (date) VALUES ('2024-05-25'), ('2024-05-26'), ('2024-05-27');


INSERT INTO objects (frame_id, name, description) VALUES
(1, 'Object A', 'Description A for 2024-01-01'),
(1, 'Object B', 'Description B for 2024-01-01'),
(2, 'Object C', 'Description C for 2024-01-02'),
(3, 'Object D', 'Description D for 2024-01-03'),
(3, 'Object E', 'Description E for 2024-01-03'),
(3, 'Object F', 'Description F for 2024-01-03');



SELECT * FROM frames;


SELECT f.date, o.name, o.description
FROM frames f
LEFT JOIN objects o ON f.frame_id = o.frame_id;
