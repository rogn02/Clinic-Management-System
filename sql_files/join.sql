#1
-- tp get patient name, caregiver name and caregiver phone no
select p.f_name,p.l_name,cg.f_name as cg_f_name,cg.l_name as cg_l_name,cg.phno from patient as p join caregiver as cg where p.cg_id=cg.cg_id;
#2
-- to get psychologist name, patient name, patient condition description 
select distinct temp.ps_f_name,temp.ps_l_name,temp.f_name,temp.l_name,r.description from (select distinct ps.f_name as ps_f_name,ps.l_name as ps_l_name,p.f_name,p.l_name,ps.ps_id from patient as p ,psychologist as ps where ps.ps_id=p.ps_id) as temp join reference_department as r where temp.ps_id=r.ps_id;
#3
-- to get patient name, caregiver id and bill amount
select p.f_name,p.l_name,p.cg_id,b.amount from patient as p join billing_department as b where b.p_id=p.p_id;
#4
-- to get hospital name, refernce doc and patient name and join date
select h.h_name,h.ref_doc,p.f_name,p.l_name,p.join_date from  hospital as h join patient as p where h.ref_date=p.join_date;
