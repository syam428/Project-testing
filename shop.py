from flask import *
from database import *
import uuid
shop=Blueprint('shop',__name__)


@shop.route('/shphome')
def shphome():
	data={}
	qry="select * from shop where shop_id='%s'"%(session['sid'])
	data['shop_det']=select(qry)
	return render_template('shophome.html',data=data)

@shop.route('/shp_view_prd',methods=['get','post'])
def shp_view_prd():
	data={}
	qry="select * from product inner join product_category using(category_id) where shop_id='%s'"%(session['sid']) 
	data['res']=select(qry)
	q="select * from product_category"
	data['cat']=select(q)
	if 'action' in request.args:
		action=request.args['action']
		prd=request.args['prd']
		if action=='update':
			qry="select * from product inner join product_category using(category_id) where product_id='%s'"%(prd) 
			res=data['upd']=select(qry)
			session['img']=res[0]['image']
		elif action=='delete':
			qry="delete from product where product_id='%s'"%(prd)
			delete(qry)
			return redirect(url_for('shop.shp_view_prd'))
			qry="delete from stock where product_id='%s'"%(prd)
			delete(qry)
		else:
			none


	if 'submit' in request.form:
		cat=request.form['category']
		proname=request.form['proname']
		prodet=request.form['prodet']
		proprice=request.form['proprice']
		profile=request.files['profile']
		path='static/'+str(uuid.uuid4())+profile.filename
		profile.save(path)
		pro="insert into product values(null,'%s','%s','%s','%s','%s','%s')"%(cat,session['sid'],proname,prodet,proprice,path)
		prd=insert(pro)
		stk="insert into stocks values(null,'%s',0,now())"%(prd)
		insert(stk)
		return redirect(url_for('shop.shp_view_prd'))

	if 'up_submit' in request.form:
		cat=request.form['category']
		proname=request.form['proname']
		prodet=request.form['prodet']
		proprice=request.form['proprice']
		profile=request.files['profile']
		if profile:
			path='static/'+str(uuid.uuid4())+profile.filename
			profile.save(path)
			upd="update product set category_id='%s',product_name='%s',details='%s',price='%s',image='%s' where product_id='%s'"%(cat,proname,prodet,proprice,path,prd)
			update(upd)
			return redirect(url_for('shop.shp_view_prd'))
		else:
			upd="update product set category_id='%s',product_name='%s',details='%s',price='%s',image='%s' where product_id='%s'"%(cat,proname,prodet,proprice,session['img'],prd)
			update(upd)
			flash("Product Updated successfully!!!")
			return redirect(url_for('shop.shp_view_prd'))
	return render_template('shop_add_product.html',data=data)

	
@shop.route('/shp_rating')
def shprate():
	data={}
	qry="select * from ratings inner join product using(product_id) where product_id in(SELECT `product_id` FROM `product` WHERE `shop_id`='%s')"%(session['sid'])
	data['rate']=select(qry)
	return render_template('shop_view_rating.html',data=data)

@shop.route('/shp_order')
def shporder():
	data={}
	qry="SELECT * FROM `order_master` INNER JOIN `order_details` USING(`order_master_id`) inner join product using(product_id)  WHERE `order_details`.`product_id` IN (SELECT `product_id` FROM `product` WHERE `shop_id`='%s') AND (`order_master`.`status`='paid' or `order_master`.`status`='Out For Delivery')"%(session['sid'])
	data['shpord']=select(qry)
	if 'action' in request.args:

		ordim=request.args['ordmid']
		qry="update order_master set status='Out For Delivery' where order_master_id='%s'"%(ordim)
		update(qry)
		flash("Order Placed!!")
		return redirect(url_for('shop.shporder'))
	return render_template('shop_view_order.html',data=data)

@shop.route('/payment_slip')
def shppayment():
	data={}
	ordd=request.args['orddet']
	ordmd=request.args['ordmid']
	qry="select * from order_details inner join product using(product_id) where order_details_id='%s'"%(ordd)
	res=select(qry)
	if res:
		data['total']=int(res[0]['quantity'])*int(res[0]['amount'])
		data['pay']=res
		qr="select * from order_master inner join user using(user_id) where order_master_id='%s'"%(ordmd)
		res=select(qr)
		data['user']=res
		
	return render_template('shop_payment_slip.html',data=data)


@shop.route('/shp_stock',methods=['post','get'])
def shpstock():
	data={}
	qry="select * from stocks inner join product using(product_id) where shop_id='%s'"%(session['sid'])
	data['shpstk']=select(qry)
	if 'action' in request.args:
		prd=request.args['prd']
		qry="select * from product where product_id='%s'"%(prd)
		data['stock']=select(qry)
	if 'up_stock' in request.form:
		quant=request.form['quant']
		qry="update stocks set quantity='%s', date_time=now() where product_id='%s'"%(quant,prd)
		update(qry)
		flash("Stock updated!")
		return redirect(url_for('shop.shpstock'))
	return render_template('shop_stock_details.html',data=data)


@shop.route('/shp_complaints',methods=['get','post'])
def shpcomp():
	data={}
	qry="SELECT * FROM `complaints` INNER JOIN `user` USING (`user_id`) WHERE shop_id='%s'"%(session['sid'])
	data['complaints']=select(qry)
	if "action" in request.args:
		action=request.args['action']
		session['cid']=request.args['cid']
		if action=='reply':
			data['reply']=0	
	if 'shop_replay' in request.form:
	    reply=request.form['replay']
	    qry="update complaints set reply='%s' where complaint_id='%s'"%(reply,session['cid'])
	    update(qry)
	    return redirect(url_for('shop.shpcomp'))
	return render_template("shop_view_complaints.html",data=data)


