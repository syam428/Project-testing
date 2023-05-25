from flask import *
from database import *
import uuid
import random
import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail
public=Blueprint('public',__name__)

@public.route('/')
def index():
	session['uid']="None"
	return render_template("index.html")

@public.route('/shop',methods=['post','get'])
def shop():
	data={}
	if 'submit' in request.form:
		shop_name=request.form['shop_name']
		proof=request.files['id']
		path='static/'+str(uuid.uuid4())+proof.filename
		proof.save(path)
		dist=request.form['dist']
		place=request.form['place']
		landm=request.form['landm']
		phone=request.form['phone']
		mail=request.form['mail']
		passw=request.form['passw']
		log="select * from login where username='%s'"%(mail)
		login=select(log)
		if login:
			flash("ERROR: Email id already exsist!!")
		else:	
			sh="insert into login values(null,'%s','%s','pending')"%(mail,passw)
			sp=insert(sh)
			shop="insert into shop values(null,'%s','%s','%s','%s','%s','%s','%s','%s','pending')"%(sp,shop_name,dist,place,landm,phone,mail,path)
			ss=insert(shop)
			flash("Registration succefully completed")
			#-----------------------------------------EMAIL PASSWORD-----------------------------------
			rd=random.randrange(1000,9999,4)
			# msg=str(rd)
			msg="Hi %s,Welcome to BrightMart,Your registration is successfully completed.\nPlease use the login credentials to access BrightMart\nPASSWORD: %s\nUSERNAME: %s\nNOTE:It might take few hours for successfull login\n\nRegards\nTeamBrightMart\n"%(shop_name,passw,mail)
			data['rd']=rd
			print(rd)
			try:
				gmail = smtplib.SMTP('smtp.gmail.com', 587)
				gmail.ehlo()
				gmail.starttls()
				gmail.login('teambrightmart@gmail.com','wluwtslqrxalyqpg')
			except Exception as ex:
				print("Couldn't setup email!!"+str(ex))

			msg = MIMEText(msg)

			msg['Subject'] = 'BrighMartLogin'

			msg['To'] = mail

			msg['From'] = 'teambrightmart@gmail.com'

			try:
				gmail.send_message(msg)
				print(msg)
				# flash("EMAIL SENED SUCCESFULLY")
				session['rd']=rd
				# return redirect(url_for('public.enterotp'))
				return redirect(url_for('public.login'))
			except Exception as ex:
				print("COULDN'T SEND EMAIL", str(ex))
				# return redirect(url_for('public.forgotpassword'))
				return redirect(url_for('public.shop'))
			# return redirect(url_for('public.login'))
	return render_template("Shop.html")

@public.route('/user',methods=['post','get'])
def user():
	data={}
	if 'submit' in request.form:
		fname=request.form['fname']
		lname=request.form['lname']
		hname=request.form['hname']
		dist=request.form['dist']
		place=request.form['place']
		landm=request.form['landm']
		pcode=request.form['pcode']
		phone=request.form['phone']
		mail=request.form['mail']
		passw=request.form['passw']
		log= "select * from login where username='%s'"%(mail)
		login=select(log)
		if login:
			flash("ERROR:Email id already registered!!")
		else:	
			us="insert into login values(null,'%s','%s','user')"%(mail,passw)
			un=insert(us)
			user="insert into user values(null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(un,fname,lname,hname,dist,place,landm,pcode,phone,mail)
			usr=insert(user)
			flash("Registration succefully completed")
			#newblock----------------------------------
			############################
			rd=random.randrange(1000,9999,4)
			# msg=str(rd)
			msg="Dear %s,\nYour registration in BrightMart is completed successfully.\nPlease use the login credentials to access BrightMart\nPASSWORD: %s\nUSERNAME: %s\n\n\nRegards\nTeamBrightMart\n"%(fname,passw,mail)
			data['rd']=rd
			print(rd)
			try:
				gmail = smtplib.SMTP('smtp.gmail.com', 587)
				gmail.ehlo()
				gmail.starttls()
				gmail.login('teambrightmart@gmail.com','wluwtslqrxalyqpg')
			except Exception as ex:
				print("Couldn't setup email!!"+str(ex))

			msg = MIMEText(msg)

			msg['Subject'] = 'BrighMartLogin'

			msg['To'] = mail

			msg['From'] = 'teambrightmart@gmail.com'

			try:
				gmail.send_message(msg)
				print(msg)
				# flash("EMAIL SENED SUCCESFULLY")
				session['rd']=rd
				# return redirect(url_for('public.enterotp'))
				return redirect(url_for('public.login'))
			except Exception as ex:
				print("COULDN'T SEND EMAIL", str(ex))
				# return redirect(url_for('public.forgotpassword'))
				return redirect(url_for('public.user'))
				################################	
			#------------------------------------------
			# return redirect(url_for('public.login'))
	return render_template("User.html")

@public.route('/logout',methods=['get','post'])
def logout():	
	session.clear()
	
	return redirect(url_for('public.login'))

@public.route('/login',methods=['get','post'])
def login():
	if 'submit' in request.form:
		uname=request.form['uname']
		passw=request.form['passw']
		log="select * from login where username='%s' and password='%s'"%(uname,passw)
		login=select(log)
		if login:
			utyp=login[0]['user_type']
			session['lid']=login[0]['login_id']
			# if utyp=='admin':
			#  	return redirect(url_for('admin.adhome'))
			if utyp=='user':
				qry="select * from user where login_id='%s'"%(session['lid'])
				uid=select(qry)
				session['uid']=uid[0]['user_id']
				session['first_name']=uid[0]['first_name']
				return redirect(url_for('user.usehome'))
			elif utyp=='shop':
				qry="select shop_id from shop where login_id='%s'"%(session['lid'])
				sid=select(qry)
				session['sid']=sid[0]['shop_id']
				return redirect(url_for('shop.shphome'))
			elif utyp=='pending':
				flash("Wait for Admin aproval!")	
		else :
			flash("Invalid user") #code
	return render_template("Login.html")


@public.route('/admin_spl_login',methods=['get','post'])
def adsplogin():
	if 'submit' in request.form:
		uname=request.form['uname']
		passw=request.form['passw']
		log="select * from login where username='%s' and password='%s'"%(uname,passw)
		login=select(log)
		if login:
			utyp=login[0]['user_type']
			session['lid']=login[0]['login_id']
			if utyp=='admin':
				return redirect(url_for('admin.adhome'))
				# return redirect(url_for('admin.adnewblock'))
			elif utyp!='admin':
				flash("unauthorized access!!")
				return redirect(url_for("public.adsplogin"))
		else:
			flash("Invalid user!!")		
	return render_template("admin_special_login.html")
	# return render_template("SpecialBlock.html")


#new--------------------------------------------------------------------->
@public.route('/allitems',methods=['get','post'])
def useproduct():
	data={}
	qry="select * from product"
	data['prd']=select(qry)
	qry="select * from product_category"
	data['cat']=select(qry)
	

	if 'srate' in request.form:
		rate=request.form['rating']
		qry="select * from product inner join ratings using(product_id) where rate='%s'"%(rate)
		data['prd']=select(qry)

	if 'scat' in request.form:
		cat=request.form['category']
		qry="select * from product where category_id='%s'"%(cat)
		data['prd']=select(qry)
	if "All items" in request.form:
		return redirect(url_for('public.useproduct'))	

	if 'search' in request.form:
		item=request.form['item']+'%'
		qry="SELECT * FROM `product` WHERE `product_name` LIKE '%s'"%(item)
		data['prd']=select(qry)


	if "action" in request.args:
		action=request.args['action']
		if action=='cart':
			prd=request.args['prd']
			qry="select * from product WHERE product_id='%s'"%(prd)
			data['view']=select(qry)

		if action=='sort':
			print("checking")
			cat=request.args['category']
			qry="select * from product where category_id='%s'"%(cat)
			
			data['prd']=prd=select(qry)
			print(prd)
			
		if "sub_cart"in request.form:
			if session['uid'] != "None":
				quant=request.form['Quant']	
				amount=request.form['hid']
				# shop=request.form['shhid']
				# total=int(quant)*int(amount)
				# qry="insert into order_master values(null,'%s','%s',now(),'%d','pending')"%(session['uid'],shop,total)
				# insert(qry)
				# return redirect(url_for('user.user_cart'))
			
				qry="select * from order_master where user_id='%s' and status='pending'"%(session['uid'])
				ur=select(qry)
				if ur:
					qry="select * from order_master inner join order_details using(order_master_id) where user_id='%s' and status='pending' and order_details.product_id='%s'"%(session['uid'],prd)
					nqry=select(qry)
					if nqry:
						qry="update order_details set quantity=quantity+'%s'"%(quant)
						update(qry)
						return redirect(url_for('user.user_cart'))

					else:	

						ormid=ur[0]['order_master_id']
						qry="insert into order_details values(null,'%s','%s','%s','%s')"%(ormid,prd,quant,amount)
						insert(qry)
						return redirect(url_for('user.user_cart'))
				else:
					qre="insert into order_master values(null,'%s',null,now(),null,'pending')"%(session['uid'])
					ormid=insert(qre)
					qry="insert into order_details values(null,'%s','%s','%s','%s')"%(ormid,prd,quant,amount)
					insert(qry)
					return redirect(url_for('user.user_cart'))
			else:
				flash("please login")
				return redirect(url_for("public.login"))		
	return render_template('items.html',data=data)

@public.route("/specialBlock")
def splblock():
	return render_template("SpecialBlock.html")