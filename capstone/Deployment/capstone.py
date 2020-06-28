#import relevant libraries
from flask import Flask, jsonify, request, render_template
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

model = pickle.load(open("capstone.pkl", 'rb')) #load model


@app.route('/')
def home():
    return render_template('/form_upload_1.html') #page to upload csv file


@app.route('/prediction',methods = ['POST'])
def upload_route_summary():
    if request.method == 'POST':

        # Create variable for uploaded file
        f = request.files['fileupload']

        #convert the csv file to dataframe
        df = pd.read_csv(f)
        ss = StandardScaler()
        df_ss  = ss.fit_transform(df)#scale the data

        df['buy_prob'] = [prob[1] for prob in model.predict_proba(df_ss)]#generate predict proba
        df['Customer ID']=np.arange(len(df)).astype(str)

        ## Generating random phone numbers

        from random import randint
        def random_with_N_digits(n):
            range_start = 10**(n-1)
            range_end = (10**n)-1
            return randint(range_start, range_end)

        df['phone number'] =1

        df['phone number'] = df['phone number'].apply(lambda x:f'{9}{random_with_N_digits(7)}')

        submission = df[['Customer ID','phone number' ,'buy_prob']]
        leads =submission.loc[df.buy_prob >0.5].sort_values(['buy_prob'], ascending= False).reset_index(drop= True) #slice the dataframe so that we show only the important columns and hides index

        pred_html = leads.to_html(col_space=100) #convert dataframe to html
#        pred_html =df.head(20).to_html(col_space=100)
#    return render_template("pred_html", output = output)

    return pred_html

if __name__ == "__main__":
    app.run(debug=True)
