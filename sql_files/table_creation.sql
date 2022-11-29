create table caregiver(
    cg_id varchar(5) not null primary key,
    f_name text,
    l_name text,
    age int,
    phno varchar(10));
    
create table psychologist(
    ps_id varchar(5) not null primary key,
    f_name text,
    l_name text,
    age int,
    phno varchar(10),
    salary int);

create table patient(
    p_id varchar(5) not null primary key,
    f_name text,
    l_name text,
    age int,
    join_date date,
    leave_date date,
    ps_id varchar(5),
    cg_id varchar(5),
    FOREIGN key (ps_id) REFERENCES psychologist(ps_id),
    FOREIGN key (cg_id) REFERENCES caregiver(cg_id));
    
create table billing_department(
    b_id varchar(5) not null primary key,
    b_date date,
    amount int,
    p_id varchar(5),
    FOREIGN key (p_id) REFERENCES patient(p_id));
    
create table hospital(
    h_id varchar(5) not null primary key,
    h_name text,
    ref_doc text,
    ref_date date,
    p_f_name text,
    p_l_name text);
    
create table reference_department(
    r_id varchar(5) not null primary key,
    r_date date,
    description text,
    h_id varchar(5),
    ps_id varchar(5),
    FOREIGN key (h_id) REFERENCES hospital(h_id),
    FOREIGN key (ps_id) REFERENCES psychologist(ps_id));