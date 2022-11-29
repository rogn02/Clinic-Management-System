# to check if individual is eligible to be a caregiver

#function declaration

DELIMITER $$
CREATE FUNCTION isEligible(
age INTEGER
)
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
IF age > 18 THEN
RETURN ("yes");
ELSE
RETURN ("No");
END IF;
END$$
DELIMITER ;

# True case
select isEligible(cg.age) from caregiver as cg;

# False case
select isEligible(p.age) from patient as p;