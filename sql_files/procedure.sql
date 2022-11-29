# procedure to get all patient info

DELIMITER $$
CREATE PROCEDURE GetPatientInfo(IN fname text)
BEGIN
SELECT
p.f_name, p.l_name, p.age, p.join_date, p.leave_date
FROM
patient as p
WHERE p.f_name = fname ;
END$$
DELIMITER ;

# procedure call
call GetPatientInfo('Rijul');