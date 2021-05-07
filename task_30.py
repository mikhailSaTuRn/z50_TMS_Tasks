saturnmkor@gmail.com
16

SELECT model, speed, hd FROM PC WHERE price < 500
SELECT DISTINCT maker FROM Product WHERE type='Printer'
SELECT model, ram, screen FROM Laptop WHERE price > 1000
SELECT * FROM Printer WHERE color = 'y'
SELECT model, speed, hd FROM PC WHERE (cd = '12x' OR cd = '24x') AND price < 600

insert into PC(code, model, speed, ram, hd, cd, price) values (20, 2111, 950, 512, 60, '52x', 1100)
insert into Product(maker, model, type) values ('Z', 4003, 'Printer'), ('Z', 4001, 'PC'), ('Z', 4002, 'Laptop')
INSERT INTO PC(model, code, speed, price, ram, hd, cd) VALUES (4444, 22, 1200, 1350, DEFAULT, DEFAULT, DEFAULT)
insert into PC(code, model, speed, ram, hd, price) select min(code) + 20, model + 1000, max(speed), max(ram) * 2, max(hd) * 2, max(price) / 1.5 from Laptop group by model
DELETE FROM PC WHERE hd = (select min(hd) FROM PC) OR ram = (select min(ram) FROM PC)

