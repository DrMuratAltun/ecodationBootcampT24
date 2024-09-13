# veri manipülasyonu temel küt.
import pandas as pd
#veri setini bölmek iin kullanılan modül
from sklearn.model_selection import train_test_split
#Regresyone modeli
from sklearn.linear_model import LinearRegression
#Değerlendirme için metrikler
from sklearn.metrics import r2_score, mean_squared_error
#veri ön işlemede kullanılacak modüller
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline


## Veri setini yükle

df=pd.read_excel(r'C:\Users\murat\Documents\EcodationBootcamp\day15\cars.xls')
df
X=df.drop('Price', axis=1)
y=df['Price']
X_train, X_test, y_train,y_test=train_test_split(X,y,
                                                test_size=.2,
                                                random_state=42)

mymodel=LinearRegression()
preprocess=ColumnTransformer (
    transformers=[
        ('num', StandardScaler(),['Mileage','Cylinder','Liter','Doors']),
        ('cat',OneHotEncoder(),['Make','Model','Trim', 'Type'])     
    ]
)

pipe=Pipeline(steps=[('preprocessor',preprocess),
                    ('model',mymodel)])

pipe.fit(X_train,y_train)

def price(make,model, trim, mileage, car_type,cylinder,liter, doors, cruise, sound, leather):
    input_data=pd.DataFrame({'Make':[make],
                            'Model':[model],
                            'Trim':[trim],
                            'Mileage':[mileage],
                             'Type':[car_type],
                             'Cylinder':[cylinder],
                             'Liter':[liter],
                             'Doors':[doors],
                             'Cruise': [cruise],
                             'Sound':[sound],
                             'Leather':[leather]})
    prediction=pipe.predict(input_data)[0]
    return prediction
import streamlit as st
st.title("II. El Araç Fiyatı Tahmin Modeli: @drmurataltun")
st.write("Arabanın özelliklerini seçiniz")
make=st.selectbox('Marka',df['Make'].unique())
model=st.selectbox('Model', df[df['Make']==make]['Model'].unique())
trim=st.selectbox('Trim',df[df['Model']==model]['Trim'].unique())
mileage=st.number_input('Mileage', 100,200000,1000)
car_type=st.selectbox('Araç tipi', df[(df['Model']==model) & (df['Trim']==trim)]['Type'].unique())
cylinder=st.selectbox('Cylinder', df['Cylinder'].unique())
liter=st.number_input('Liter', 1,10)
doors=st.selectbox('Doors', df['Doors'].unique())
cruise=st.radio('Cruise',[True,False])
sound=st.radio('Sound',[True,False])
leather=st.radio('Leather', [True,False])
if st.button('Tahmin Yap'):
    #pred= price(make,model, trim, mileage, car_type,cylinder,liter, doors, cruise, sound, leather)
    #st.write('Fiyat: $', round(pred[0],2))
    print ('ÇAışıyor')
