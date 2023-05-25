from flask import *
from database import *
from Crypto.Cipher import AES, DES
import os
import smtplib
from email.mime.text import MIMEText
from flask_mail import Mail
user=Blueprint('user',__name__)
import random



iv = os.urandom(16)  

# key = os.urandom(16)  


cryptogen = random.SystemRandom()
key = bytearray(cryptogen.getrandbits(8) for i in range(16))
print(key)



def encrypt_card_details(card_details, key, iv):

    cipher = AES.new(key, AES.MODE_CBC, iv)  

  
    block_size = cipher.block_size
    if isinstance(card_details, str):
        card_details = card_details.encode()

    padding_size = block_size - len(card_details) % block_size
    padded_card_details = card_details + padding_size * bytes([padding_size])


    encrypted_card_details = cipher.encrypt(padded_card_details)


    return iv + encrypted_card_details


def decrypt_card_details(encrypted_card_details, key):
    print("DDDDDDDDDDDDDDDDDDDDDDDDDDD")

    iv = encrypted_card_details[:16] 

   
    cipher = AES.new(key, AES.MODE_CBC, iv)  

   
    decrypted_card_details = cipher.decrypt(encrypted_card_details[16:])
    print("PPPPPPP",decrypted_card_details)


    block_size = cipher.block_size
    padding_size = decrypted_card_details[-1]
    print("padding_size : ",padding_size)
    unpadded_card_details = decrypted_card_details[:-padding_size]
    print("UUUUUUUUU",unpadded_card_details)

   
    return unpadded_card_details.decode('utf-8')


@user.route('/usehome')
def usehome():
	data={}
	qry="select * from user inner join login using(login_id) where user_id='%s'"%(session['uid'])
	data['user_det']=select(qry)
	return redirect(url_for('user.useproduct'))
	# return render_template('userhome.html',data=data)

@user.route('/user_view_shops')
def useshop():
	data={}
	qry="select * from shop"
	data['shp']=select(qry)
	return render_template('user_view_shop.html',data=data)

@user.route('/user_view_product',methods=['get','post'])
def useproduct():
	data={}
	qry="select * from product inner join stocks using(product_id)"
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

	if 'search' in request.form:
		item=request.form['item']+'%'
		qry="SELECT * FROM `product` WHERE `product_name` LIKE '%s'"%(item)
		data['prd']=select(qry)


	if "action" in request.args:
		action=request.args['action']
		if action=='sort':
			
			cat=request.args['category']
			qry="select * from product where category_id='%s'"%(cat)
			
			data['prd']=prd=select(qry)
			print(prd)
		if action=='cart':
			prd=request.args['prd']
			session['qnt']=int(request.args['qnt'])
			
			qry="select * from product WHERE product_id='%s'"%(prd)
			data['view']=select(qry)
			qry="select * from stocks WHERE product_id='%s'"%(prd)
			data['stocks']=select(qry)
			data['quant']=int(data['stocks'][0]['quantity'])


		if "sub_cart"in request.form:
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
					flash("item added to cart")
					return redirect(url_for('user.user_cart'))

				else:	

					ormid=ur[0]['order_master_id']
					qry="insert into order_details values(null,'%s','%s','%s','%s')"%(ormid,prd,quant,amount)
					insert(qry)
					flash("item added to cart")
					return redirect(url_for('user.user_cart'))
			else:
				qre="insert into order_master values(null,'%s',null,now(),null,'pending')"%(session['uid'])
				ormid=insert(qre)
				qry="insert into order_details values(null,'%s','%s','%s','%s')"%(ormid,prd,quant,amount)
				insert(qry)
				flash("item added to cart")
				return redirect(url_for('user.user_cart'))
	return render_template('user_view_product.html',data=data)

@user.route('/usrcomplaints',methods=['get','post'])
def usercomplaints():
	data={}
	qry="select * from complaints inner join shop using (shop_id) where user_id='%s'"%(session['uid'])
	data['rep']=select(qry)
	qry="select* from shop"
	data['shop']=select(qry)
	if 'submit' in request.form:
		typ=request.form['type']
		com=request.form['com']
		shop=request.form['shop']
		us="insert into complaints values(null,'%s','%s','%s','%s','pending',now())"%(session['uid'],shop,typ,com)
		insert(us)
		return redirect(url_for('user.usercomplaints'))
	return render_template("Complaints.html",data=data)


@user.route('/user_cart',methods=['get','post'])
def user_cart():
	data={}
	qry="SELECT * FROM `order_details` INNER JOIN `order_master` USING(`order_master_id`) INNER JOIN `product` USING(`product_id`) WHERE `user_id`='%s' AND `status`='pending'"%(session['uid'])
	res=data['ordcart']=select(qry)
	total=0
	data['test']=True
	if res:
		data['test']=False
		for i in res:
			total=total+(int(i['quantity'])*int(i['amount']))
		session['total']=total
	if 'submit' in request.form:
		return redirect(url_for('user.user_payment'))

	if 'action' in request.args:
		action=request.args['action']
		oid=request.args['oid']

	else:
		action=None
	if action=="reject":
		q="delete from order_details where order_details_id='%s'"%(oid)
		update(q)
		return redirect(url_for("user.user_cart"))

	return render_template("user_order_cart.html",data=data,total=total)

@user.route("/user_history")
def user_hist():
	data={}
	qry="SELECT * FROM `order_details` INNER JOIN `product` USING(`product_id`) INNER JOIN `order_master` USING (`order_master_id`) WHERE `user_id`='%s' AND `status`!='pending'"%(session['uid'])
	data['ordhist']=select(qry)
	return render_template("user_order_hist.html",data=data)

@user.route("/feedback",methods=['get','post'])
def user_feedback():
	prd=request.args['prd']
	if 'submit' in request.form:
		rate=request.form['rating']
		review=request.form['review']
		ins="insert into ratings values(null,'%s','%s','%s','%s',now())"%(session['uid'],prd,rate,review)
		insert(ins)
		flash("Thank you for your response ")
		return redirect(url_for("user.usehome"))
	return render_template("user_feed.html")


@user.route("/payment",methods=['get','post'])
def user_payment():
	data={}
	det="select * from user where user_id='%s'"%(session['uid'])
	data['deta']=select(det)
	if 'dd' in request.form:
		# encrypted_card_details = bytes.fromhex(request.form['encrypted_card_details'])
		key1=request.form['key']
		print(key1,'3333333333333333333333333333333333333333333333333333333333')
		q1="SELECT card_enc FROM card WHERE `key`='%s'"%(key1)
		res=select(q1)
		val=res[0]['card_enc']
		encrypted_card_details = bytes.fromhex(val)
		key= bytes.fromhex(request.form['key'])
		print(key," ::::::::::;")
		print("---------- : ",encrypted_card_details)
		decrypted_card_details = decrypt_card_details(encrypted_card_details, key)
		print("@@@@@@@@@@@@@@@@@@@@@@@@ : ",decrypted_card_details)
		print(decrypted_card_details)
		x = decrypted_card_details.split("-")
		data['name']=x[0]
		data['numb']=x[1]
		data['dat']=x[2]
		data['cv']=x[3]

	data['total']=session['total']
	if 'pay' in request.form:
		qry="SELECT * FROM `order_details` INNER JOIN `order_master` USING(`order_master_id`) INNER JOIN `product` USING(`product_id`) WHERE `user_id`='%s' AND `status`='pending'"%(session['uid'])
		res=select(qry)
		for i in res:
			qry="update stocks set quantity=quantity-'%s' where product_id='%s'"%(i['quantity'],i['product_id'])
			update(qry)
			qry="update order_master set status='paid' where order_master_id='%s'"%(i['order_master_id'])
			update(qry)
			flash("Your order has been placed, conformation will be send mail")
		return redirect(url_for("user.user_hist"))	
	return render_template("checkpay.html",data=data)

@user.route("/cardreg",methods=['get','post'])
def user_card():
	key = bytearray(cryptogen.getrandbits(8) for i in range(16))
	print(key)
	if 'regcard' in request.form:
		c_name=request.form['c_name']
		c_num=request.form['c_num']
		c_dat=request.form['c_dat']
		c_cc=request.form['c_cc']
		card_details=c_name+"-"+c_num+"-"+c_dat+"-"+c_cc
		encrypted_card_details = encrypt_card_details(card_details, key, iv)
		rev=encrypted_card_details.hex()
		print(rev)
		# print(key)
		# print(key.hex())
		q0="insert into card values(NULL,'%s','%s','%s')"%(session['uid'],rev,key.hex())
		print(q0)
		insert(q0)
		msg=key.hex()
		qa="select * from user where user_id='%s'"%(session['uid'])
		ra=select(qa)
		email=ra[0]['email']
		try:
				gmail = smtplib.SMTP('smtp.gmail.com', 587)
				gmail.ehlo()
				gmail.starttls()
				gmail.login('teambrightmart@gmail.com','wluwtslqrxalyqpg')
		except Exception as e:
			print("Couldn't setup email!!"+str(e))

		msg = MIMEText(msg)

		msg['Subject'] = 'Card registred successfully, copy the below token!'

		msg['To'] = email

		msg['From'] = 'teambrightmart@gmail.com'

		try:

			gmail.send_message(msg)
			print(msg)
			key = bytearray()
			return '''<script>alert('encrypted and mail send successfully');window.location='usehome'</script>'''


		except Exception as e:
			print("COULDN'T SEND EMAIL", str(e))
			key = bytearray()
			return '''<script>alert('encrypted');window.location='usehome'</script>'''

	return render_template("cardpage.html")

@user.route("/cardinfo")
def card_info():
	return render_template("instruction.html")
	


