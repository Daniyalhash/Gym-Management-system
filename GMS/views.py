
from django.shortcuts import render,redirect,HttpResponse
from django.db import connections
import uuid
from django.views.decorators.csrf import csrf_exempt


from django.contrib import messages
import sqlite3,os,datetime,random,string
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.
def index(request):

    return render(request,'index.html')

def dashboard(request):

    return render(request,'dashboard.html')
# member
def member(request):
    with sqlite3.connect(BASE_DIR/'db.sqlite3') as db:
        cursor=db.cursor()
        query = "SELECT * FROM member"  
        cursor.execute(query)

        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        # Prepare the data as a list of dictionaries
        members = []
        for row in rows:
            member = dict(zip(column_names, row))
            members.append(member)
        print(members)
        
        return render(request,'member.html',{'member':members})
def delete_member(request,m_id):
    with sqlite3.connect(BASE_DIR / 'db.sqlite3') as db:
        cursor = db.cursor()
        query = "DELETE FROM member WHERE m_id= ?"
        cursor.execute(query, (m_id,))
        messages.success(request, 'Member deleted successfully.')
       
      
        return redirect('/member')
    
def save_member(request):
    if request.method == 'POST':
        m_id =  random.randint(1, 100)
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        status = None
        with sqlite3.connect(BASE_DIR/'db.sqlite3') as db:
            cursor=db.cursor()
           
            query = 'INSERT INTO "member"("m_id","fname","lname","email","phone","status") VALUES (?,?,?,?,?,?)'
            values = (m_id,fname,lname,email,phone,status)
           
            cursor.execute(query, values)
       

    return redirect('/member')
def getmember(request):
    
    with sqlite3.connect(BASE_DIR/'db.sqlite3') as db:
        cursor = db.cursor()
        query = "SELECT * FROM member"  
        cursor.execute(query)

        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        # Prepare the data as a list of dictionaries
        members = []
        for row in rows:
            member = dict(zip(column_names, row))
            members.append(member)
        
        # Count the total number of products
        total_products = len(members)
        
        return render(request, 'product.html', {'member': members, 'total_product': total_products})
def editmember(request):
    if request.method == 'POST':
        m_id = request.POST.get('m_id')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        status = None
        with sqlite3.connect(BASE_DIR / 'db.sqlite3') as db:
            cursor = db.cursor()
            
            query = """
                UPDATE member
                SET fname = ?,
                    lname = ?,
                    email = ?,
                    phone = ?,
                    status = ?
                WHERE m_id = ?
            """
            cursor.execute(query, (fname, lname, email, phone, status, m_id))


    return redirect('/member')


def update_member(request, m_id):
    # Process the form submission and update the product information in the database
        
    with sqlite3.connect(BASE_DIR / 'db.sqlite3') as db:
        cursor = db.cursor()
        query = """
            SELECT * FROM member
            WHERE m_id = ?
        """
        cursor.execute(query, (m_id,))
        rows = cursor.fetchone()
        
        # rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        # Prepare the data as a list of dictionaries
        # Prepare the data as a dictionary
        member = dict(zip(column_names, rows))
        
    return render(request, 'update_m.html', {"member": member})
# trainer
def trainer(request):
    with sqlite3.connect(BASE_DIR/'db.sqlite3') as db:
        cursor=db.cursor()
        query = "SELECT * FROM trainer"  
        cursor.execute(query)

        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        # Prepare the data as a list of dictionaries
        trainers = []
        for row in rows:
            trainer = dict(zip(column_names, row))
            trainers.append(trainer)
        print(trainers)
        
        return render(request,'trainer.html',{'trainer':trainers})
def delete_trainer(request,t_id):
    with sqlite3.connect(BASE_DIR / 'db.sqlite3') as db:
        cursor = db.cursor()
        query = "DELETE FROM trainer WHERE t_id= ?"
        cursor.execute(query, (t_id,))
        messages.success(request, 'trainer deleted successfully.')
       
      
        return redirect('/trainer')
    
def save_trainer(request):
    if request.method == 'POST':
        t_id =  random.randint(1, 100)
        fnamet = request.POST.get('fnamet')
        lnamet = request.POST.get('lnamet')
        emailt = request.POST.get('emailt')
        phonet = request.POST.get('phonet')
        age = request.POST.get('age')
        exp = request.POST.get('exp')
        status = None
        clients = None
        with sqlite3.connect(BASE_DIR/'db.sqlite3') as db:
            cursor=db.cursor()
           
            query = 'INSERT INTO "trainer"("t_id","fnamet","lnamet","emailt","phonet","age","exp","status","clients") VALUES (?,?,?,?,?,?,?,?,?)'
            values = (t_id,fnamet,lnamet,emailt,phonet,age,exp,status,clients)
           
            cursor.execute(query, values)
       

    return redirect('/trainer')
def gettrainer(request):
    
    with sqlite3.connect(BASE_DIR/'db.sqlite3') as db:
        cursor = db.cursor()
        query = "SELECT * FROM trainer"  
        cursor.execute(query)

        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        # Prepare the data as a list of dictionaries
        trainers = []
        for row in rows:
            trainer = dict(zip(column_names, row))
            trainers.append(trainer)
        
        # Count the total number of products
        total_products = len(trainers)
        
        return render(request, 'trainer.html', {'trainer': trainers, 'total_product': total_products})
def edittrainer(request):
    if request.method == 'POST':
        t_id =  request.POST.get('t_id')
        fnamet = request.POST.get('fnamet')
        lnamet = request.POST.get('lnamet')
        emailt = request.POST.get('emailt')
        phonet = request.POST.get('phonet')
        age = request.POST.get('age')
        exp = request.POST.get('exp')
        status = None
        clients = None
        with sqlite3.connect(BASE_DIR / 'db.sqlite3') as db:
            cursor = db.cursor()
            
            query = """
                UPDATE trainer
                SET fnamet = ?,
                    lnamet = ?,
                    emailt = ?,
                    phonet = ?,
                    age = ?,
                    exp =?,
                    status = ?,
                    clients =?
                WHERE t_id = ?
            """
            cursor.execute(query, (fnamet,lnamet,emailt,phonet,age,exp,status,clients,t_id))


    return redirect('/trainer')


def update_trainer(request, t_id):
    # Process the form submission and update the product information in the database
        
    with sqlite3.connect(BASE_DIR / 'db.sqlite3') as db:
        cursor = db.cursor()
        query = """
            SELECT * FROM trainer
            WHERE t_id = ?
        """
        cursor.execute(query, (t_id,))
        rows = cursor.fetchone()
        
        # rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        # Prepare the data as a list of dictionaries
        # Prepare the data as a dictionary
        trainer = dict(zip(column_names, rows))
        
    return render(request, 'update_t.html', {"trainer": trainer})
# plan
def plan(request):
    with sqlite3.connect(BASE_DIR/'db.sqlite3') as db:
            cursor=db.cursor()
            query = "SELECT * FROM member"  
            cursor.execute(query)

            rows = cursor.fetchall()
            column_names = [description[0] for description in cursor.description]

            # Prepare the data as a list of dictionaries
            members = []
            for row in rows:
                member = dict(zip(column_names, row))
                members.append(member)
            print(members)
            
    with sqlite3.connect(BASE_DIR/'db.sqlite3') as db:
            cursor2=db.cursor()
            query2 = "SELECT * FROM plan"  
            cursor2.execute(query2)

            rows2 = cursor2.fetchall()
            column_names2 = [description[0] for description in cursor2.description]

            # Prepare the data as a list of dictionaries
            plans= []
            for row2 in rows2:
                plan = dict(zip(column_names2, row2))
                plans.append(plan)
            print(plans)
            return render(request,'plan.html',{'plan':plans,'member':members})
def save_plan(request):
    if request.method == 'POST':
        mm_id =  random.randint(1, 100)
        m_id =  request.POST.get('m_id')
        age = request.POST.get('age')
        height = request.POST.get('height')
        pound = request.POST.get('pound')
        kg = request.POST.get('kg')
        c_type = request.POST.get('c_type')
        w_type = request.POST.get('w_type')
        tp = request.POST.get('tp')
        tpl = request.POST.get('tpl')
        t_id = request.POST.get('t_id')
      
        with sqlite3.connect(BASE_DIR / 'db.sqlite3') as db:
            cursor2 = db.cursor()
            query2 = """
                SELECT COUNT(*) FROM plan
                WHERE m_id = ? AND t_id = ? AND c_type = ? AND w_type = ?
            """
            cursor2.execute(query2 ,(m_id, t_id, c_type, w_type))
            count = cursor2.fetchone()[0]
            
            if count > 0:
                # If count is greater than 0, it means the plan already exists for this member, trainer, and exercise.
                # You can show an error message or take appropriate action here.
                return redirect("Error: This plan already exists for this member and trainer.")
            else:
                # If the plan does not exist, proceed with the insertion as usual.
                query2 = 'INSERT INTO "plan"("mm_id", "m_id", "age", "height", "pound", "kg", "c_type", "w_type", "tp", "tpl", "t_id") VALUES (?,?,?,?,?,?,?,?,?,?,?)'
                values2 = (mm_id, m_id, age, height, pound, kg, c_type, w_type, tp, tpl, t_id)
                cursor2.execute(query2, values2)
                # updating trainer db and member db
                # Fetch the number of plans with the same trainer
                query3 = """
                    SELECT COUNT(*) FROM plan
                    WHERE t_id = ?
                """
                cursor2.execute(query3, (t_id,))
                plans_with_same_trainer = cursor2.fetchone()[0]

                # Update the trainer's clients count based on the number of plans with the same trainer
                cursor = db.cursor()
                query5 = """
                    UPDATE trainer
                    SET status = ?,
                        clients = ?
                    WHERE t_id = ?
                """
                cursor.execute(query5, ('on', plans_with_same_trainer, t_id))
                # update also member
                cursor = db.cursor()
                query5 = """
                    UPDATE member
                    SET status = ?
                     
                    WHERE m_id = ?
                """
                cursor.execute(query5, ('on',  m_id))

    return redirect('/plan')


def create_plan(request, m_id):
    # Process the form submission and update the product information in the database
        
    with sqlite3.connect(BASE_DIR / 'db.sqlite3') as db:
        cursor = db.cursor()
        query = """
            SELECT * FROM member
            WHERE m_id = ?
        """
        cursor.execute(query, (m_id,))
        rows = cursor.fetchone()
        
        # rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        # Prepare the data as a list of dictionaries
        # Prepare the data as a dictionary
        member = dict(zip(column_names, rows))
             
    with sqlite3.connect(BASE_DIR/'db.sqlite3') as db:
            cursor2=db.cursor()
            query2 = "SELECT * FROM trainer"  
            cursor2.execute(query2)

            rows2 = cursor2.fetchall()
            column_names2 = [description[0] for description in cursor2.description]

            # Prepare the data as a list of dictionaries
            trainers = []
            for row2 in rows2:
                trainer = dict(zip(column_names2, row2))
                trainers.append(trainer)
            print(trainers)   
    return render(request, 'planning.html', {"member": member,'trainer':trainers})

# def delete_plan(request, mm_id):
#     with sqlite3.connect(BASE_DIR / 'db.sqlite3') as db:
#         cursor = db.cursor()

#         # Fetch the plan to get the t_id and m_id before deleting it
#         query = """
#             SELECT * FROM plan
#             WHERE mm_id = ?
#         """
#         cursor.execute(query, (mm_id,))
#         plan = cursor.fetchone()

#         # Get the trainer's ID (t_id) and member's ID (m_id) from the plan
#         t_id = plan[10]
       

#         # Delete the plan from the 'plan' table
#         query2 = "DELETE FROM plan WHERE mm_id = ?"
#         cursor.execute(query2, (mm_id,))
#         messages.success(request, 'Plan deleted successfully.')

#         # Update the trainer's client count
#         cursor2 = db.cursor()
#         # Get the current client count for the trainer
#         query = """
#             SELECT clients FROM trainer
#             WHERE t_id = ?
#         """
#         cursor2.execute(query, (t_id,))
#         current_clients = cursor2.fetchone()[0]

#         # Update the client count for the trainer (subtract 1)
#         new_clients = int(current_clients) - 1

#         # Update the client count for the trainer in the 'trainer' table
#         query = """
#             UPDATE trainer
#             SET clients = ?
#             WHERE t_id = ?
#         """
#         cursor2.execute(query, (new_clients, t_id))

#         # Update the status of the trainer based on the new client count
#         new_status = 'on' if new_clients > 0 else 'off'
#         query = """
#             UPDATE trainer
#             SET status = ?
#             WHERE t_id = ?
#         """
#         cursor2.execute(query, (new_status, t_id))


#         return redirect('/plan')
def delete_plan(request, mm_id):
    with sqlite3.connect(BASE_DIR / 'db.sqlite3') as db:
        cursor = db.cursor()

        # Fetch the plan to get the t_id and m_id before deleting it
        query = """
            SELECT * FROM plan
            WHERE mm_id = ?
        """
        cursor.execute(query, (mm_id,))
        plan = cursor.fetchone()

        if plan:  # Check if plan is not None
            # Get the trainer's ID (t_id) and member's ID (m_id) from the plan
            t_id = plan[10]

            # Delete the plan from the 'plan' table
            query2 = "DELETE FROM plan WHERE mm_id = ?"
            cursor.execute(query2, (mm_id,))
            messages.success(request, 'Plan deleted successfully.')

            # Update the trainer's client count
            cursor2 = db.cursor()
            # Get the current client count for the trainer
            query = """
                SELECT clients FROM trainer
                WHERE t_id = ?
            """
            cursor2.execute(query, (t_id,))
            current_clients = cursor2.fetchone()[0]

            # Update the client count for the trainer (subtract 1)
            new_clients = int(current_clients) - 1

            # Update the client count for the trainer in the 'trainer' table
            query = """
                UPDATE trainer
                SET clients = ?
                WHERE t_id = ?
            """
            cursor2.execute(query, (new_clients, t_id))

            # Update the status of the trainer based on the new client count
            new_status = 'on' if new_clients > 0 else 'off'
            query = """
                UPDATE trainer
                SET status = ?
                WHERE t_id = ?
            """
            cursor2.execute(query, (new_status, t_id))

        return redirect('/plan')

# extra work
def your_view_function(request):
    with sqlite3.connect(BASE_DIR/'db.sqlite3') as db:
        cursor=db.cursor()
        query = "SELECT * FROM member"  
        cursor.execute(query)

        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        # Prepare the data as a list of dictionaries
        members = []
        for row in rows:
            member = dict(zip(column_names, row))
            members.append(member)
        print(members)
        
        
    with sqlite3.connect(BASE_DIR/'db.sqlite3') as db:
        cursor=db.cursor()
        query = "SELECT * FROM trainer"  
        cursor.execute(query)

        rows = cursor.fetchall()
        column_names = [description[0] for description in cursor.description]

        # Prepare the data as a list of dictionaries
        trainers = []
        for row in rows:
            trainer = dict(zip(column_names, row))
            trainers.append(trainer)
        print(trainers)
        
        
    with sqlite3.connect(BASE_DIR/'db.sqlite3') as db:
        cursor2=db.cursor()
        query2 = "SELECT * FROM plan"  
        cursor2.execute(query2)

        rows2 = cursor2.fetchall()
        column_names2 = [description[0] for description in cursor2.description]

        # Prepare the data as a list of dictionaries
        plans= []
        for row2 in rows2:
            plan = dict(zip(column_names2, row2))
            plans.append(plan)
        print(plans)
        return render(request,'dashboard.html',{'plan':plans,'member':members,'trainer':trainers})
