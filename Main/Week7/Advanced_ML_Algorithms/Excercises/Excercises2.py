#Handle missing values

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from sklearn.metrics import classification_report, roc_auc_score

#Load Dataset
df = pd.read_csv('Telco-Customer-Churn.csv')

#Display dataset information and preview
print('Dataset Info: \n')
print(df.info())
print('\n Class Distribution')
print(df['Churn'].value_counts())
print('n\ Sample Data: \n', df.head())

#Handle Missing values
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')
df.fillna({'TotalCharges':df['TotalCharges'].median()}, inplace=True)

#Encode categorical variables
label_encoder = LabelEncoder()
for column in df.select_dtypes(include=['object']).columns:
    if column != 'Churn':
        df[column] = label_encoder.fit_transform(df[column])

#Encode target variable
df['Churn'] = label_encoder.fit_transform(df['Churn'])

#Scale numerical features
scaler = StandardScaler()
numerical_features = ['tenure', 'MonthlyCharges', 'TotalCharges']
df[numerical_features] = scaler.fit_transform(df[numerical_features])

#Split dataset: Features and Target
x = df.drop(columns=['Churn'])
y = df['Churn']

#Split dataset:
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

#Apply SMOTE
smote = SMOTE(random_state=42)
x_train_resampled , y_train_resampled = smote.fit_resample(x_train, y_train)

#Display class distribution after SMOTE
print('\n Class Distribution after SMOTE: \n')
print(pd.Series(y_train_resampled).value_counts())

#Train Random Forest
rf_model = RandomForestClassifier(random_state=42)
rf_model.fit(x_train_resampled, y_train_resampled)
y_pred_rf = rf_model.predict(x_test)
roc_auc_rf = roc_auc_score(y_test, rf_model.predict_proba(x_test)[:,1])

#Train XGBoost
xgb_model = XGBClassifier(eval_metric='logloss',random_state=42)
xgb_model.fit(x_train_resampled, y_train_resampled)
y_pred_xgb = xgb_model.predict(x_test)
roc_auc_xgb = roc_auc_score(y_test, xgb_model.predict_proba(x_test)[:,1])

#Train LightGBM
lgb_model = LGBMClassifier(random_state=42)
lgb_model.fit(x_train_resampled, y_train_resampled)
y_pred_lgb = lgb_model.predict(x_test)
roc_auc_lgb = roc_auc_score(y_test, lgb_model.predict_proba(x_test)[:,1])

#Classification Report
print('Random Forest Report:\n', classification_report(y_test, y_pred_rf))
print('XGBoost Report: \n', classification_report(y_test, y_pred_xgb))
print('LighGBM Report: \n', classification_report(y_test, y_pred_lgb))

#ROC_AUC comparison
print('ROC-AUC Scores: \n')
print(f'Random Forest: {roc_auc_rf:.2f}')
print(f'XGBoost : {roc_auc_xgb:.2f}')
print(f'LightGBM : {roc_auc_lgb:.2f}')


