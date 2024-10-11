-- 공통
SELECT * FROM articles;
SELECT * FROM users;
DROP TABLE articles;
DROP TABLE users;
PRAGMA table_info('articles');


-- 실습용 데이터
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50) NOT NULL
);

CREATE TABLE articles (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title VARCHAR(50) NOT NULL,
  content VARCHAR(100) NOT NULL,
  userId INTEGER NOT NULL,
  FOREIGN KEY (userId) 
    REFERENCES users(id)
);

INSERT INTO 
  users (name)
VALUES 
  ('하석주'),
  ('송윤미'),
  ('유하선');

INSERT INTO
  articles (title, content, userId)
VALUES 
  ('제목1', '내용1', 1),
  ('제목2', '내용2', 2),
  ('제목3', '내용3', 1),
  ('제목4', '내용4', 4),
  ('제목5', '내용5', 1);


-- INNER JOIN
SELECT * FROM articles 
INNER JOIN users
  ON users.id = articles.userid;
SELECT articles.title, users.name
FROM 
  articles INNER JOIN users
  ON users.id = articles.userid
  WHERE users.id = 1;

-- LEFT JOIN
SELECT *
FROM articles LEFT JOIN users 
  ON users.id = articles.userId;
SELECT *
FROM articles RIGHT JOIN users 
  ON users.id = articles.userId;
SELECT *
FROM articles FULL OUTER JOIN users
  ON users.id = articles.userId;

-- CROSS JOIN
-- 두 테이블 간의 가능한 모든 경우의 수를 출력
-- 출력 결과 : 왼쪽 테이블 * 오른쪽 테이블
SELECT *
FROM articles, users;