-- Отримати всі завдання певного користувача. Використайте SELECT для отримання завдань конкретного користувача за його user_id.
SELECT t.id, t.title, t.description, t.user_id
FROM tasks t
WHERE t.user_id = 1
ORDER BY t.id;

-- Вибрати завдання за певним статусом. Використайте підзапит для вибору завдань з конкретним статусом, наприклад, 'new'.
SELECT t.id, t.title, t.description, t.user_id
FROM tasks t
JOIN status s ON t.status_id = s.id
WHERE s.name = 'not solved'

-- Оновити статус конкретного завдання. Змініть статус конкретного завдання на 'in progress' або інший статус.
UPDATE tasks
SET status_id = (
    SELECT id
    FROM status
    WHERE name = 'not solved'
    )
WHERE id = 2;

-- Отримати список користувачів, які не мають жодного завдання.
SELECT *
FROM users u
LEFT JOIN tasks t ON u.id = t.user_id
WHERE t.id is NULL;

-- Додати нове завдання для конкретного користувача. Використайте INSERT для додавання нового завдання.
INSERT INTO tasks (title, description, status_id, user_id)
VALUES ('Newly added task', 'You have to do a lot of things', (SELECT id FROM status WHERE name = 'new'), 12));

-- Отримати всі завдання, які ще не завершено. Виберіть завдання, чий статус не є 'завершено'.
SELECT *
FROM tasks t
JOIN status s ON s.id = t.status_id
WHERE s.name != 'completed';

-- Видалити конкретне завдання. Використайте DELETE для видалення завдання за його id.
DELETE FROM tasks t
WHERE t.id = 101;

-- Знайти користувачів з певною електронною поштою. Використайте SELECT із умовою LIKE для фільтрації за електронною поштою.
SELECT *
FROM users u
WHERE u.email LIKE '%.com'
ORDER BY u.id;

-- Оновити ім'я користувача. Змініть ім'я користувача за допомогою UPDATE.
UPDATE users
SET fullname = 'Dean L Jones'
WHERE id = 12;

-- Отримати кількість завдань для кожного статусу. Використайте SELECT, COUNT, GROUP BY для групування завдань за статусами.
SELECT COUNT(t.status_id), s.name
FROM tasks t
JOIN status s ON s.id = t.status_id
GROUP BY s.name;

-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти. Використайте SELECT з умовою LIKE в поєднанні з JOIN, щоб вибрати завдання, призначені користувачам, чия електронна пошта містить певний домен (наприклад, '%@example.com').
SELECT *
FROM tasks t
JOIN users u ON t.user_id = u.id
WHERE u.email LIKE '%.com'
ORDER BY t.title;

-- Отримати список завдань, що не мають опису. Виберіть завдання, у яких відсутній опис.
SELECT *
FROM tasks t
WHERE t.description is NULL or t.description = '';

-- Вибрати користувачів та їхні завдання, які є у статусі 'in progress'. Використайте INNER JOIN для отримання списку користувачів та їхніх завдань із певним статусом.
SELECT u.fullname AS user, t.title, t.description
FROM users u
JOIN tasks t ON u.id = t.user_id
JOIN status s ON s.id = t.status_id
WHERE s.name = 'in progress';

-- Отримати користувачів та кількість їхніх завдань. Використайте LEFT JOIN та GROUP BY для вибору користувачів та підрахунку їхніх завдань.
SELECT u.fullname, COUNT(t.user_id)
FROM users u
JOIN tasks t ON u.id = t.user_id
GROUP BY u.fullname;