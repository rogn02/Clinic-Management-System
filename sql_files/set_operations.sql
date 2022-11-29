#1 union

(select p.f_name, p.l_name from patient as p) UNION (select h.p_f_name, h.p_l_name from hospital as h);

#2 union all

(select p.f_name, p.l_name from patient as p) UNION ALL (select h.p_f_name, h.p_l_name from hospital as h);

#3 except

(select ps.f_name, ps.l_name, ps.salary from psychologist as ps) 
except (SELECT ps.f_name, ps.l_name, ps.salary from psychologist as ps where ps.salary<100000);

#4 intersect

(select ps.f_name, ps.l_name, ps.salary from psychologist as ps where ps.salary>1000000) 
intersect (SELECT ps.f_name, ps.l_name, ps.salary from psychologist as ps where ps.salary<2000000);