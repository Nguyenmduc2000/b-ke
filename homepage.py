from flask import Flask, request, render_template,session,redirect, url_for
import mlab
from models.superbike import Bike

app = Flask(__name__)
mlab.connect()

@app.route("/", methods=['GET', 'POST'])
def homepage():
  if request.method == 'GET':
    return render_template("homepage.html")
  elif request.method == 'POST':
    form = request.form
    search_name = form['search_bike']
    return redirect(url_for('search', search_name = search_name))

# @app.route("/<brand>")
# def intro(brand):
#   return render_template("intro.html", hangxe=brand )



  

@app.route("/<brand>", methods = ["GET","POST"])
def phankhuc(brand):
  if request.method == "GET" :
    bikes = Bike.objects(hangxe=brand)
    return render_template("phankhuc.html",hangxe=brand, bikes = bikes)
  if request.method == "POST":
    return render_template("homepage.html")
  

@app.route("/<brand>/<name>", methods = ["GET","POST"])
def thongso(brand,name):

  if request.method == "GET":
    info = Bike.objects(bikename=name)  
    return render_template("thongso.html", hangxe = brand, dongxe = name, info = info)
  if request.method == "POST":
    return render_template("homepage.html")
  

@app.route('/search/<search_name>')
def search(search_name):
  print(search_name)
  bikes = Bike.objects(hangxe__icontains = search_name)
  print(bikes)
  return redirect("<brand>/<search_name>")

# @app.route('/search/<search_name>')
# def search(search_name):
#   # print(search_name)
#   bikes = Bike.objects(hangxe__icontains = search_name)
#   # print(bikes)
#   if "search_name" == Bike["bikename"]:
#     return redirect("<brand>/<search_name>")
#   else :
#     return "abc"
  
 
  
if __name__ == '__main__':
  app.run(debug=True)