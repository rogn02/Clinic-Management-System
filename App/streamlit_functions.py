import streamlit as st
from cursor import conn

#Add function
# GENERAL QUERY : insert into table_name values(*args);
def Add(Clinic):
    #table name selection
    table_name=st.selectbox("Table:", ["patient", "caregiver", "psychologist","hospital","reference_department","billing_department"])
    #switch case using table name
    match (table_name):
        case "patient":
            p_id = st.text_input("p_id:")
            f_name = st.text_input("first name:")
            l_name = st.text_input("last name:")
            age = st.number_input("age:")
            join_date = st.date_input("join date:")
            leave_date = st.date_input("leave date:")
            ps_id = st.text_input("ps_id:")
            cg_id = st.text_input("cg_id:")
            # only when the ADD button is clicked the query is executed
            if (st.button("ADD")):
                # query executer
                Clinic.cursor.execute("insert into patient values(%s,%s,%s,%s,%s,%s,%s,%s);",(p_id,f_name,l_name,age,join_date,leave_date,ps_id,cg_id))
                #conn.commit to make sure that the state is changed immediately at the db
                conn.commit()
                st.success("Values inserted successfully!")
        case "caregiver":
            cg_id = st.text_input("cg_id:")
            f_name = st.text_input("first name:")
            l_name = st.text_input("last name:")
            age = st.number_input("age :")
            phno = st.number_input("phno :")
            # only when the ADD button is clicked the query is executed
            if (st.button("ADD")):
                # query executer
                Clinic.cursor.execute("insert into caregiver values(%s,%s,%s,%s,%s);",(cg_id,f_name,l_name,age,phno))
                #conn.commit to make sure that the state is changed immediately at the db
                conn.commit()
                st.success("Values inserted successfully!")
        case "hospital":
            h_id = st.text_input("h_id :")
            h_name = st.text_input("h_name :")
            ref_doc = st.text_input("ref_doc :")
            ref_date = st.date_input("ref_date :")
            p_f_name = st.text_input("p_f_name :")
            p_l_name = st.text_input("p_l_name :")
            # only when the ADD button is clicked the query is executed
            if (st.button("ADD")):
                # query executer
                Clinic.cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s)",(h_id,h_name,ref_doc,ref_date,p_f_name,p_l_name))
                #conn.commit to make sure that the state is changed immediately at the db
                conn.commit()
                st.success("Values inserted successfully!")
        case "reference_department":
            r_id = st.text_input("r_id :")
            r_date = st.date_input("r_date :")
            description = st.text_input("description :")
            h_id = st.text_input("h_id :")
            ps_id = st.text_input("ps_id :")
            if st.button("ADD"):
                # query executer
                Clinic.cursor.execute("insert into reference_department values(%s,%s,%s,%s,%s);",(r_id,r_date,description,h_id,ps_id))
                #conn.commit to make sure that the state is changed immediately at the db
                conn.commit()
                st.success("Values inserted successfully!")
        case "billing_department":
            b_id = st.text_input("b_id :")
            b_date = st.date_input("b_date :")
            amount = st.number_input("amount :")
            p_id = st.text_input("p_id :")
            if st.button("ADD"):
                # query executer
                Clinic.cursor.execute("insert into billing_department values(%s,%s,%s,%s);",(b_id,b_date,amount,p_id))
                #conn.commit to make sure that the state is changed immediately at the db
                conn.commit()
                st.success("Values inserted successfully!")
        case "psychologist":
            ps_id = st.text_input("ps_id :")
            f_name = st.text_input("f_name :")
            l_name = st.text_input("l_name :")
            age = st.number_input("age :")
            phno = st.number_input("phno :")
            salary = st.number_input("salary :")
            if st.button("ADD"):
                # query executer
                Clinic.cursor.execute("insert into psychologist values(%s,%s,%s,%s,%s,%s);",(ps_id,f_name,l_name,age,phno,salary))
                #conn.commit to make sure that the state is changed immediately at the db
                conn.commit()
                st.success("Values inserted successfully!")

#View function
def View(Clinic):
    #table name selection
    table_name=st.selectbox("Table:", ["patient", "caregiver", "psychologist","hospital","reference_department","billing_department"])
    if (st.button("VIEW")):
        Clinic.view_table(table_name)
        df=[row for row in Clinic.cursor]
        st.table(df)
        st.success("Success")
            
# Delete function
# GENERAL QUERY : delete from table_name where primary_key = input_value;
def Delete(Clinic):
    #table name selection
    table_name=st.selectbox("Table:", ["patient", "caregiver", "psychologist","hospital","reference_department","billing_department"])
    # switch case based on table name
    match(table_name):
        case "patient":
            p_id = st.text_input("p_id :")
            # query only executed when the delete button is clicked
            if st.button("DELETE"):
                # query executer
                Clinic.cursor.execute("DELETE FROM patient WHERE p_id ='{}';".format(p_id))
                #conn.commit to make sure that the state is changed immediately at the db
                conn.commit()
                st.success("Deleted succesfully!")
        case "caregiver":
            cg_id = st.text_input("cg_id :")
            # query only executed when the delete button is clicked
            if st.button("DELETE"):
                # query executer
                Clinic.cursor.execute("delete from caregiver where cg_id = '{}';".format(cg_id))
                #conn.commit to make sure that the state is changed immediately at the db
                conn.commit()
                st.success("Deleted succesfully!")
        case "psychologist":
            ps_id = st.text_input("ps_id :")
            # query only executed when the delete button is clicked
            if st.button("DELETE"):
                # query executer
                Clinic.cursor.execute("delete from psychologist where ps_id = '{}';".format(ps_id))
                #conn.commit to make sure that the state is changed immediately at the db
                conn.commit()
                st.success("Deleted succesfully!")
        case "billing_department":
            b_id = st.text_input("b_id :")
            # query only executed when the delete button is clicked
            if st.button("DELETE"):
                # query executer
                Clinic.cursor.execute("delete from billing_department where b_id = '{}';".format(b_id))
                #conn.commit to make sure that the state is changed immediately at the db
                conn.commit()
                st.success("Deleted succesfully!")
        case "reference_department":
            r_id = st.text_input("r_id :")
            # query only executed when the delete button is clicked
            if st.button("DELETE"):
                # query executer
                Clinic.cursor.execute("delete from reference_department where r_id = '{}';".format(r_id))
                #conn.commit to make sure that the state is changed immediately at the db
                conn.commit()
                st.success("Deleted succesfully!")
        case "hospital":
            h_id = st.text_input("h_id :")
            # query only executed when the delete button is clicked
            if st.button("DELETE"):
                # query executer
                Clinic.cursor.execute("delete from hospital where h_id = '{}';".format(h_id))
                #conn.commit to make sure that the state is changed immediately at the db
                conn.commit()
                st.success("Deleted succesfully!")

#Any Query function
def AnyFunc(Clinic):
    # query input
    query = st.text_input("Enter your query:")
    if st.button("Run"):
        #query execution
        Clinic.cursor.execute(query)
        # creating a df obj so its easier to represent as a tablek
        df = [row for row in Clinic.cursor]
        st.table(df)
        st.success("Query excecuted successfully!")

#Update Function
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
                        Clinic.cursor.execute("update caregiver set f_name='"+f_name+"' where cg_id='"+cg_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
                case("l_name"):
                    l_name = st.text_input("last name:")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update caregiver set l_name='"+l_name+"' where cg_id='"+cg_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
                case("age"):
                    age = st.number_input("age :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update caregiver set age="+age+" where cg_id='"+cg_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
                case("phno"):
                    phno = st.number_input("phno :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update caregiver set phno='"+phno+"' where cg_id='"+cg_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
        case "hospital":
            h_id = st.text_input("h_id :")
            column_name=st.selectbox(["h_name,ref_doc,ref_date,p_f_name,l_f_name"])
            match (column_name):
                case("h_name"):
                    h_name = st.text_input("h_name :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update hospital set h_name='"+h_name+"' where h_id='"+h_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
                case("ref_doc"):
                    ref_doc = st.text_input("ref_doc :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update hospital set ref_doc='"+ref_doc+"' where h_id='"+h_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
                case("ref_date"):
                    ref_date = st.date_input("ref_date :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update hospital set ref_date='"+ref_date+"' where h_id='"+h_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
                case("p_f_name"):
                    p_f_name = st.text_input("p_f_name :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update hospital set p_f_name='"+p_f_name+"' where h_id='"+h_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
                case("p_l_name"):
                    p_l_name = st.text_input("p_l_name :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update hospital set p_l_name='"+p_l_name+"' where h_id='"+h_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")      
        case "reference_department":
            r_id = st.text_input("r_id :")
            column_name=st.selectbox(["r_date","description","h_id","ps_id"])
            match(column_name):
                case("r_date"):
                    r_date = st.date_input("r_date :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update reference_department set r_date='"+r_date+"' where r_id='"+r_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
                case("description"):
                    description = st.text_input("description :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update reference_department set description='"+description+"' where r_id='"+r_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
                case("h_id"):
                    h_id = st.text_input("h_id :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update reference_department set h_id='"+h_id+"' where r_id='"+r_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
                case("ps_id"):
                    ps_id = st.text_input("ps_id :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update reference_department set ps_id='"+ps_id+"' where r_id='"+r_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
        case "billing_department":
            b_id = st.text_input("b_id :")
            column_name=st.selectbox(["b_date","amount","p_id"])
            match(column_name):
                case("b_date"):
                    b_date = st.date_input("b_date :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update billing_department set b_date='"+b_date+"' where b_id='"+b_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
                case("amount"):
                    amount = st.number_input("amount :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update billing_department set amount='"+amount+"' where b_id='"+b_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
                case("p_id"):
                    p_id = st.text_input("p_id :")
                    if (st.button("Update")):
                        Clinic.cursor.execute("update billing_department set p_id='"+p_id+"' where b_id='"+b_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
        case "psychologist":
            ps_id = st.text_input("ps_id :")
            column_name=st.selectbox(["f_name","l_name","age","phno","salary"])
            match(column_name):
                case("f_name"):
                    f_name = st.text_input("f_name :")
                    if(st.button("Update")):
                        Clinic.cursor.execute("update psychologist set f_name='"+f_name+"' where ps_id='"+ps_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
                case("l_name"):
                    l_name = st.text_input("l_name :")
                    if(st.button("Update")):
                        Clinic.cursor.execute("update psychologist set l_name='"+l_name+"' where ps_id='"+ps_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
                case("age"):
                    age = st.number_input("age :")
                    if(st.button("Update")):
                        Clinic.cursor.execute("update psychologist set age="+age+" where ps_id='"+ps_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
                case("phno"):
                    phno = st.number_input("phno :")
                    if(st.button("Update")):
                        Clinic.cursor.execute("update psychologist set phno='"+phno+"' where ps_id='"+ps_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")
                case("salary"):
                    salary = st.number_input("salary :")
                    if(st.button("Update")):
                        Clinic.cursor.execute("update psychologist set salary="+salary+" where ps_id='"+ps_id+"';")
                        conn.commit()
                        st.success("Values updated successfully!")