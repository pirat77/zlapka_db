CREATE TRIGGER zlapka.bonus_voucher
ON users
AFTER INSERT
AS
BEGIN
INSERT INTO voucher(type, value, user_id)
VALUES("DISCOUNT", 20, (SELECT user_id FROM users ORDER BY user_id DESC LIMIT 1));
END

CREATE TRIGGER zlapka.ended_events
ON event
AFTER INSERT
AS
BEGIN
DELETE FROM event WHERE event.date >= current_date ;
END

