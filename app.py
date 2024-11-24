from flask import Flask, render_template, request
import joblib
import warnings

#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------

# Filter out any warnings you want to suppress
warnings.filterwarnings("ignore", category=UserWarning)

model= joblib.load('models\crop_app')

#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------

app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('Crop Recommendation.html', title='Home')

#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------

@app.route('/rec_cr', methods=["POST"])
def recomm():
    Nitrogen=float(request.form['Nitrogen'])
    Phosphorus=float(request.form['Phosporus'])
    Potassium=float(request.form['Potassium'])
    Temperature=float(request.form['Temperature'])
    Humidity=float(request.form['Humidity'])
    Ph=float(request.form['ph'])
    Rainfall=float(request.form['Rainfall'])
     
    values=[Nitrogen,Phosphorus,Potassium,Temperature,Humidity,Ph,Rainfall]
    
    if Ph>0 and Ph<=14 and Temperature<100 and Humidity>0:
        arr = [values]
        acc = model.predict(arr)
        print(acc)
        return render_template('Crop Recommendation.html', result=str(acc))
    else:
        return "Error!"

#--------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True)
