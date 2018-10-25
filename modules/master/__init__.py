from flask import Blueprint, render_template, redirect, url_for, request, flash
from modules.libs import Query
master = Blueprint('master', __name__)

def noSKU():
    no = 0
    last_sku = Query().custom_query('select no_sku from tb_produk where id = (select max(id) from tb_produk);')
    if len(last_sku) < 1:
        no = 90001
    else:
        no = int(last_sku[0][0]) + 1 
    return no

@master.route('/')
def main():
    try:
        data = Query('tb_produk').get_by()
        no_sku = noSKU()
        return render_template('master/index.html', dataTable=data, no_sku=no_sku)
    except Exception as e:
        print str(e)

@master.route('/tambah', methods=['POST'])
def tambah():
    try:
        query = Query('tb_produk')
        if request.method == 'POST':
            no_sku = request.form['no_sku']
            nama = request.form['nama']
            ukuran =  request.form['ukuran']
            harga = request.form['harga']
            pajak = request.form['pajak']

            result = query.insert({
                "no_sku" : no_sku,
                "nama" : nama,
                "ukuran" : ukuran,
                "harga" : harga,
                "pajak" : pajak
            })

            if result is True:
                flash("Data Produk Berhasil Disimpan.", "success")                        
            else:
                flash("Data Produk Gagal Disimpan.", "error")
            
        return redirect(url_for('master.main'))
    except Exception as e:
        print str(e)

@master.route('/edit', methods=['POST'])
def edit():
    try:
        query = Query('tb_produk')
        if request.method == 'POST':
            id = request.form['id']
            nama = request.form['nama']
            ukuran =  request.form['ukuran']
            harga = request.form['harga']
            pajak = request.form['pajak']

            result = query.update({
                "id" : id,
                "nama" : nama,
                "ukuran" : ukuran,
                "harga" : harga,
                "pajak" : pajak
            })
            if result is True:
                flash("Data Produk Berhasil Diperbarui.", "success")                        
            else:
                flash("Data Produk Gagal Dipierbarui.", "error")
            
        return redirect(url_for('master.main'))
        
    except Exception as e:
        print str(e)

@master.route('/hapus', methods=['POST'])
def hapus():
    try:
        query = Query('tb_produk')
        if request.method == 'POST':
            id = request.form['id']

            result = query.delete(id=id)
            if result is True:
                flash("Data Produk Berhasil Dihapus.", "success")                        
            else:
                flash("Data Produk Gagal Dihapus.", "error")
            
        return redirect(url_for('master.main'))        
    except Exception as e:
        print str(e)