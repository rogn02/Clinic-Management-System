def Update(Clinic):
    #table name selection
    table_name=st.selectbox("Table:", ["patient", "caregiver", "psychologist","hospital","reference_department","billing_department"])
    #switch case using table name
    match (table_name):
        case "patient":
            p_id = st.text_input("p_id:")
            column_name=st.selectbox("Columns:",["f_name","l_name","age","join_date","leave_date","ps_id","cg_id"])
            match (column_name):
                case("f_name"):
                    f_name = st.text_input("first name:")
                    if (st.button("Update")):
                        # query executer
                        Clinic.cursor.execute("update patient set f_name='"+f_name+"' where p_id='"+p_id+"';")
                        #conn.commit to make sure that the state is changed immediately at the db
                        conn.commit()
                        st.success("Values updated successfully!")
            
                case("l_name"):
                    l_name = st.text_input("last name:")
                    if (st.button("Update")):
                        # query executer
                        Clinic.cursor.execute("update patient set l_name='"+l_name+"' where p_id='"+p_id+"';")
                        #conn.commit to make sure that the state is changed immediately at the db
                        conn.commit()
                        st.success("Values updated successfully!")
                case("age"):
                    age = st.text_input("age:")
                    if (st.button("Update")):
                        # query executer
                        Clinic.cursor.execute("update patient set age="+age+" where p_id='"+p_id+"';")
                        #conn.commit to make sure that the state is changed immediately at the db
                        conn.commit()
                        st.success("Values updated successfully!")
            
                case("join_date"):
                    join_date = st.text_input("join date:")
                    if (st.button("Update")):
                        # query executer
                        Clinic.cursor.execute("update patient set join_date='"+join_date+"' where p_id='"+p_id+"';")
                        #conn.commit to make sure that the state is changed immediately at the db
                        conn.commit()
                        st.success("Values updated successfully!")
            
                case("ps_id"):
                    ps_id = st.text_input("ps_id:")
                    if (st.button("Update")):
                        # query executer
                        Clinic.cursor.execute("update patient set ps_id='"+ps_id+"' where p_id='"+p_id+"';",(ps_id,p_id))
                        #conn.commit to make sure that the state is changed immediately at the db
                        conn.commit()
                        st.success("Values updated successfully!")
                case("cg_id"):
                    cg_id = st.text_input("cg_id:")
                    if (st.button("Update")):
                        # query executer
                        Clinic.cursor.execute("update patient set cg_id='"+cg_id+"' where p_id='"+p_id+"';")
                        #conn.commit to make sure that the state is changed immediately at the db
                        conn.commit()
                        st.success("Values updated successfully!")
        case "caregiver":
            column_name=st.selectbox(["f_name","l_name","age","phno"])
            cg_id = st.text_input("cg_id:")
            match (column_name):
                case("f_name"):
                    f_name = st.text_input("first name:")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update caregiver set f_name='"++"' where cg_id='"++"';",(f_name,cg_id))
                        conn.commit()
                        st.success("Values updated successfully!")
                case("l_name"):
                    l_name = st.text_input("last name:")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update caregiver set l_name='"++"' where cg_id='"++"';",(l_name,cg_id))
                        conn.commit()
                        st.success("Values updated successfully!")
                case("age"):
                    age = st.number_input("age :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update caregiver set age="++" where cg_id='"++"';",(age,cg_id))
                        conn.commit()
                        st.success("Values updated successfully!")
                case("phno"):
                    phno = st.number_input("phno :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update caregiver set phno='"++"' where cg_id='"++"';",(phno,cg_id))
                        conn.commit()
                        st.success("Values updated successfully!")
        case "hospital":
            h_id = st.text_input("h_id :")
            column_name=st.selectbox(["h_name,ref_doc,ref_date,p_f_name,l_f_name"])
            match (column_name):
                case("h_name"):
                    h_name = st.text_input("h_name :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update hospital set h_name='"++"' where h_id='"++"';",(h_name,h_id))
                        conn.commit()
                        st.success("Values updated successfully!")
                case("ref_doc"):
                    ref_doc = st.text_input("ref_doc :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update hospital set ref_doc='"++"' where h_id='"++"';",(ref_doc,h_id))
                        conn.commit()
                        st.success("Values updated successfully!")
                case("ref_date"):
                    ref_date = st.date_input("ref_date :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update hospital set ref_date='"++"' where h_id='"++"';",(ref_date,h_id))
                        conn.commit()
                        st.success("Values updated successfully!")
                case("p_f_name"):
                    p_f_name = st.text_input("p_f_name :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update hospital set p_f_name='"++"' where h_id='"++"';",(p_f_name,h_id))
                        conn.commit()
                        st.success("Values updated successfully!")
                case("p_l_name"):
                    p_l_name = st.text_input("p_l_name :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update hospital set p_l_name='"++"' where h_id='"++"';",(p_l_name,h_id))
                        conn.commit()
                        st.success("Values updated successfully!")      
        case "reference_department":
            r_id = st.text_input("r_id :")
            column_name=st.selectbox(["r_date","description","h_id","ps_id"])
            match(column_name):
                case("r_date"):
                    r_date = st.date_input("r_date :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update reference_department set r_date='"++"' where r_id='"++"';",(r_date,r_id))
                        conn.commit()
                        st.success("Values updated successfully!")
                case("description"):
                    description = st.text_input("description :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update reference_department set description='"++"' where r_id='"++"';",(description,r_id))
                        conn.commit()
                        st.success("Values updated successfully!")
                case("h_id"):
                    h_id = st.text_input("h_id :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update reference_department set h_id='"++"' where r_id='"++"';",(h_id,r_id))
                        conn.commit()
                        st.success("Values updated successfully!")
                case("ps_id"):
                    ps_id = st.text_input("ps_id :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update reference_department set ps_id='"++"' where r_id='"++"';",(ps_id,r_id))
                        conn.commit()
                        st.success("Values updated successfully!")
        case "billing_department":
            b_id = st.text_input("b_id :")
            column_name=st.selectbox(["b_date","amount","p_id"])
            match(column_name):
                case("b_date"):
                    b_date = st.date_input("b_date :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update billing_department set b_date='"++"' where b_id='"++"';",(b_date,b_id))
                        conn.commit()
                        st.success("Values updated successfully!")
                case("amount"):
                    amount = st.number_input("amount :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update billing_department set amount='"++"' where b_id='"++"';",(amount,b_id))
                        conn.commit()
                        st.success("Values updated successfully!")
                case("p_id"):
                    p_id = st.text_input("p_id :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update billing_department set p_id='"++"' where b_id='"++"';",(p_id,b_id))
                        conn.commit()
                        st.success("Values updated successfully!")
        case "psychologist":
            ps_id = st.text_input("ps_id :")
            column_name=st.selectbox(["f_name","l_name","age","phno","salary"])
            match(column_name):
                case("f_name"):
                    f_name = st.text_input("f_name :")
                    if(st.button("Update")):
                        Clinic.cursor.execute("update psychologist set f_name='"++"' where ps_id='"++"';",(f_name,ps_id))
                        conn.commit()
                        st.success("Values updated successfully!")
                case("l_name"):
                    l_name = st.text_input("l_name :")
                    if(st.button("Update")):
                        Clinic.cursor.execute("update psychologist set l_name='"++"' where ps_id='"++"';",(l_name,ps_id))
                        conn.commit()
                        st.success("Values updated successfully!")
                case("age"):
                    age = st.number_input("age :")
                    if(st.button("Update")):
                        Clinic.cursor.execute("update psychologist set age="++" where ps_id='"++"';",(age,ps_id))
                        conn.commit()
                        st.success("Values updated successfully!")
                case("phno"):
                    phno = st.number_input("phno :")
                    if(st.button("Update")):
                        Clinic.cursor.execute("update psychologist set phno='"++"' where ps_id='"++"';",(phno,ps_id))
                        conn.commit()
                        st.success("Values updated successfully!")
                case("salary"):
                    salary = st.number_input("salary :")
                    if(st.button("Update")):
                        Clinic.cursor.execute("update psychologist set salary="++" where ps_id='"++"';",(salary,ps_id))
                        conn.commit()
                        st.success("Values updated successfully!")
            
