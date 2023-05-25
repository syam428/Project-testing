from flask import *
from database import *
admin=Blueprint('admin',__name__)

@admin.route('/adhome')
def adhome():
	return render_template("SpecialBlock.html")

@admin.route('/ad_shops')
def adshop():
	data={}
	qry="select * from shop order by shop_id desc"

	if 'action' in request.args:
		action=request.args['action']
		lid=request.args['lid']

	else:
		action=None
	if action=="accept":
		q="update login set user_type='shop' where login_id='%s'"%(lid)
		update(q)
		qry="update shop set status='Accepted' where login_id='%s'"%(lid)
		update(qry)
		return redirect(url_for('admin.adshop'))
	if action=='reject':
		q="delete from shop where login_id='%s'"%(lid)
		delete(q)
		r="delete from login where login_id='%s'"%(lid)
		delete(r)
	data['res']=select(qry)
	return render_template("admin_view_shop.html",data=data)

@admin.route('/ad_productcat',methods=['get','post'])
def adprdman():
	data={}
	qry="select * from product_category"
	data['val']=select(qry)

	if 'action' in request.args:
		action=request.args['action']
		lid=request.args['lid']
	else:
		action=None

	if action=='update':
		q="select * from product_category where category_id='%s'"%(lid)
		data['upd']=select(q)
		if 'edit' in request.form:
			cat=request.form['adcat']
			val="update product_category set category_name ='%s' where category_id='%s'"%(cat,lid)
			update(val)
			return redirect(url_for('admin.adprdman'))
			flash("Category updated succefully!")
	if action=='delete':
		qry="delete from product_category where category_id='%s'"%(lid)
		delete(qry)
		return redirect(url_for('admin.adprdman'))

	if 'submit' in request.form:
		value=request.form['adcat']
		qry="insert into product_category values(null,'%s')"%(value)
		val=insert(qry)
		return redirect(url_for('admin.adprdman'))
	return render_template("admin_productcat.html",data=data)

@admin.route('/ad_product')
def adprd():
	data={}
	qry="select * from product inner join shop using(shop_id)"
	data['res']=select(qry)
	return render_template("admin_product.html",data=data)

@admin.route('/ad_stock')
def adstock():
	data={}
	# qry="select * from stocks inner join product using(product_id)"
	qry="SELECT * FROM product INNER JOIN stocks USING (product_id) INNER JOIN shop USING(shop_id)"

	data['res']=select(qry)
	return render_template("admin_stock.html",data=data)


@admin.route('/ad_complaint',methods=['get','post'])
def adcomplaint():
	data={}
	qry="select * from complaints inner join shop using(shop_id)"
	data['res']=select(qry)
	qry="select * from complaints inner join shop using(shop_id)";
	data['shopname']=select(qry)
	if "action" in request.args:
		action=request.args['action']
		session['cid']=request.args['cid']
		if action=='reply':
			data['reply']=0	
	if 'sub_replay' in request.form:
	    reply=request.form['replay']
	    qry="update complaints set reply='%s' where complaint_id='%s'"%(reply,session['cid'])
	    update(qry)
	    return redirect(url_for('admin.adcomplaint'))

	return render_template("admin_complaint.html",data=data)



@admin.route('/ad_cust')
def adcoust():
	data={}
	qry="select * from user"
	data['res']=select(qry)
	return render_template("admin_coustmer.html",data=data)

@admin.route('/adminreply', methods=['get','post'])
def adreply():
	cid=request.args['complaintid']
	if 'submit' in request.form:
		reply=request.form['reply']
		val="update complaints set reply ='%s' where complaint_id='%s'"%(reply,cid)
		update(val)
		return redirect(url_for('admin.adcomplaint'))
	return render_template("admin_reply.html")


@admin.route('/newblock')
def adnewblock():
	return render_template("SpecialBlock.html")



