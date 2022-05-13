from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

@app.route('/', methods = ['GET','POST'])
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')



@app.route('/getResponseLinearReg',methods=["GET","POST"])
def getResponseLinearReg():
    TEMPERATURE = request.form["TEMPERATURE"]
    CLEARSKYDHI = request.form["CLEARSKYDHI"]
    CLEARSKYDNI = request.form["CLEARSKYDNI"]
    CLEARSKYGHI = request.form["CLEARSKYGHI"]
    CLOUDTYPE = request.form["CLOUDTYPE"]
    DEWPOINT = request.form["DEWPOINT"]
    DHI = request.form["DHI"]
    DNI = request.form["DNI"]
    FILLFLAG = request.form["FILLFLAG"]
    OZONE = request.form["OZONE"]
    RELATIVEHUMADITY = request.form["RELATIVEHUMADITY"]
    SOLARZENITHANGLE = request.form["SOLARZENITHANGLE"]
    SURFACEALBEDO = request.form["SURFACEALBEDO"]
    PRESSURE = request.form["PRESSURE"]
    PRECIPITABLEWATER = request.form["PRECIPITABLEWATER"]
    WINDDIRECTION = request.form["WINDDIRECTION"]
    WINDSPEED = request.form["WINDSPEED"]
    CLOUDCOVER = request.form["CLOUDCOVER"]
    DHI_LOG = request.form["DHI_LOG"]
    GHI_LOG = request.form["GHI_LOG"]
    CLOUDCOVER_LOG = request.form["CLOUDCOVER_LOG"]

    inputList = [TEMPERATURE,CLEARSKYDHI,CLEARSKYDNI,CLEARSKYGHI,CLOUDTYPE,DEWPOINT,DHI,DNI,FILLFLAG,OZONE,RELATIVEHUMADITY,SOLARZENITHANGLE,SURFACEALBEDO,PRESSURE,PRECIPITABLEWATER,WINDDIRECTION,WINDSPEED,CLOUDCOVER,DHI_LOG,GHI_LOG,CLOUDCOVER_LOG]
    with open("trainedmodel.pkl", 'rb') as file:
            pickle_model = pickle.load(file)
            y_pred_from_pkl = pickle_model.predict([inputList])
    print(y_pred_from_pkl)
    return str(y_pred_from_pkl[0])

if __name__ == '__main__':
    app.run(debug=True)


