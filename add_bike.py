from flask import Flask, render_template , request
import mlab
from models.superbike import Bike

mlab.connect()

app = Flask(__name__)

@app.route("/add_bike", methods = ["GET","POST"])
def add_bike():
    if request.method == "GET":
        return render_template("add_bike.html")
    if request.method == "POST":
        form = request.form 
        bikename = form["bikename"]
        hangxe = form["hangxe"]
        image = form["image"]
        dongco = form["dongco"]
        maluc = form["maluc"]
        hopso = form["hopso"]
        chieucaoyenxe = form["chieucaoyenxe"]
        dacdiemkhac = form["dacdiemkhac"]
        giaxe = form["giaxe"]
        superbike = Bike(bikename = bikename,hangxe = hangxe, image = image ,dongco = dongco , maluc = maluc , hopso = hopso , chieucaoyenxe = chieucaoyenxe  , dacdiemkhac = dacdiemkhac , giaxe = giaxe)
        superbike.save()
        return render_template("add_bike.html")

if __name__ == "__main__":
    app.run(debug=True)


# bike = Bike.objects.with_id("5c1bc34abd42b10f5051e379")

# bike.update(set__bikename = " CB 500F")
# print(bike.bikename)
    