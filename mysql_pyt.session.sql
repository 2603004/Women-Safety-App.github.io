CREATE TABLE IF NOT EXISTS loginpage (
        id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) NOT NULL ,
        password VARCHAR(255) NOT NULL
    );

    create table signup(
        id INT AUTO_INCREMENT PRIMARY KEY,
        name varchar(255) not null,
        email VARCHAR(255) NOT NULL ,
        password VARCHAR(255) NOT NULL
        
    );

    INSERT INTO loginpage(email,password) VALUES
    ('abhay@gmail.com','abhay@123');
    SELECT* FROM feedback;
     
    CREATE TABLE IF NOT EXISTS feedback (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL ,
        message VARCHAR(255) NOT NULL
        
    );
    ALTER TABLE feedback
    DROP TABLE feedback;
    DELETE FROM feedback;