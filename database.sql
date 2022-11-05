create table patient(
    patient_id varchar(5) primary key,
    first_name char(30),
    last_name char(30),
    age int,
    join_date date,
    leave_date date);

create table caregiver(
    caregiver_id varchar(5) primary key,
    first_name char(30),
    last_name char(30),
    age int,
    phoneno bigint,
    p_id varchar(5),
    foreign key (p_id) references patient(patient_id));

create table employee(
    employee_id varchar(5) primary key,
    first_name char(30),
    last_name char(30),
    age int,
    phoneno bigint,
    salary int,
    p_id varchar(5),
    foreign key (p_id) references patient(patient_id));

create table hospital(
    hospital_id varchar(5) primary key,
    name char(30),
    reference_doctor char(50),
    reference_date date,
    p_id varchar(5),
    foreign key (p_id) references patient(patient_id));

create table psychologist(
    psychologist_id varchar(5) primary key,
    first_name char(30),
    last_name char(30),
    age int,
    phoneno bigint,
    salary int,
    p_id varchar(5),
    foreign key (p_id) references patient(patient_id));

create table case_info(
    case_id varchar(5) primary key,
    p_id varchar(5),
    ps_id varchar(5),
    h_id varchar(5),
    e_id varchar(5),
    description text,
    foreign key (p_id) references patient(patient_id),
    foreign key (ps_id) references psychologist(psychologist_id),
    foreign key (h_id) references hospital(hospital_id),
    foreign key (e_id) references employee(employee_id)
);

create table reference_department(
    reference_id varchar(5),
    e_id varchar(5),
    h_id varchar(5),
    ps_id varchar(5),
    foreign key (e_id) references employee(employee_id),
    foreign key (h_id) references hospital(hospital_id),
    foreign key (ps_id) references psychologist(psychologist_id));

create table billing_department(
    billing_id varchar(5),
    amount int,
    billing_date date,
    c_id varchar(5),
    foreign key (c_id) references case_info(case_id));
