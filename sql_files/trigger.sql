# trigger to check if patient is a minor

DELIMITER //
Create Trigger before_insert_patient BEFORE INSERT ON patient FOR EACH ROW
BEGIN
IF NEW.age > 18 THEN SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'This database is only for minors';
END IF;
END //

#Fail

insert into patient(p_id,f_name,l_name,age,join_date,leave_date,ps_id,cg_id) values('P0006','Keshav','Yadav',19,'2021-09-17','2021-10-18','PS001','CG004');

#Pass

insert into patient(p_id,f_name,l_name,age,join_date,leave_date,ps_id,cg_id) values('P0006','Keshav','Yadav',17,'2021-09-17','2021-10-18','PS001','CG004');