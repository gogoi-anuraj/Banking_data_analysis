import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)
banking=pd.read_csv(r"c:\Users\DELL\Downloads\banking_data.csv")
print(banking.head())
print(banking.shape)
print(banking.columns)
print(banking.info())
print(banking.nunique())
print(banking.isnull().sum())
banking.dropna(inplace=True)
print(banking.isnull().sum())
print(banking.shape)


#removing marital_status
print(banking.marital.value_counts())
print(banking.marital_status.value_counts())
banking.drop(columns=['marital_status'], inplace=True)
print(banking.columns)



## What is the distribution of age among the clients?
sns.histplot(banking['age'], bins=100, kde=True)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

sns.boxplot(banking.age)
plt.title('Age')
plt.show()

sns.boxplot(y="job", x="age", data=banking)
plt.title('Age as per jobs')
plt.show()




##-	How does the job type vary among the clients?
sns.countplot(y='job', data=banking, order=banking['job'].value_counts().index)
plt.title('Job Type Distribution')
plt.show()

no_unknown=banking[banking.education!='unknown']
sns.countplot(x='education', hue='job', data= no_unknown, palette='viridis' )
plt.title('Classification of Jobs based on Education')
plt.show()




##-	What is the marital status distribution of the clients?
sns.countplot(x='marital',hue='marital', data=banking, palette='viridis')
plt.title('Marital Status Distribution')
plt.ylabel('Count')
plt.show()
print(banking.marital.value_counts())

sns.boxplot(x='marital', y='age',hue='marital', data=banking, palette='viridis')
plt.title('Distribution of Age by Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Age')
plt.show()




##-	What is the level of education among the clients?
print(banking.education.value_counts())

sns.countplot(x='education', data=banking)
plt.title('Education Level Distribution')
plt.xlabel('Education Level')
plt.ylabel('Count')
plt.show()





## What proportion of clients have credit in default?
credit_in_default=banking.default.value_counts(normalize=True)*100
print(f'Proportion of clients having credits in default in percentage: {credit_in_default}')

sns.barplot(x=credit_in_default.index, y=credit_in_default.values)
plt.title('Proportion of Clients with Credit in Default')
plt.xlabel('Default')
plt.ylabel('Percentage')
plt.show()





##-	What is the distribution of average yearly balance among the clients?
sns.histplot(banking['balance'], bins=30,  kde=True)
plt.title('Average Yearly Balance Distribution')
plt.xlabel('Balance (in euros)')
plt.ylabel('Frequency')
plt.show()
print(banking.balance.describe())

average_balance_by_job = banking.groupby('job')['balance'].median().sort_values()
print(average_balance_by_job)
sns.barplot(x=average_balance_by_job.values, hue=average_balance_by_job.index, palette='viridis')
plt.title('Average Yearly Balance by Job Type')
plt.xlabel('Average Balance')
plt.ylabel('Job Type')
plt.show()






##-	How many clients have housing loans?
sns.countplot(x=banking.housing)
plt.title('Number of Clients with Housing Loans')
plt.xlabel('Housing Loan')
plt.ylabel('Count')
plt.show()
housing_loan=len(banking[banking.housing=='yes'])
print(f'Number of clients having housing loan: {housing_loan}')
print(f'Number of clients who do not have housing loan: {len(banking)-housing_loan}')





##-	How many clients have personal loans?
sns.countplot(x=banking.loan)
plt.title('Number of Clients with personal Loans')
plt.xlabel('Personal Loan')
plt.ylabel('Count')
plt.show()
personal_loan=len(banking[banking.loan=='yes'])
print(f'Number of clients having personal loan: {personal_loan}')
print(f'Number of clients who do not have personal loan: {len(banking)-personal_loan}')





##-	What are the communication types used for contacting clients during the campaign?
sns.countplot(x='contact', hue='contact',data=banking, palette='viridis')
plt.xlabel('Communication Type')
plt.ylabel('Count')
plt.title('Communication Types Used for Contacting Clients')
plt.show()
without_contact_unknown=banking[banking.contact!='unknown']
contacting_types=without_contact_unknown.contact.unique()
print(f'The communication types used for contacting clients during the campaign are: {contacting_types}')





##-	What is the distribution of the last contact day of the month?
sns.histplot(x=banking['day'],hue=banking['day'], bins=31, palette='viridis', legend=False)
plt.title('Distribution of the Last Contact Day of the Month')
plt.xlabel('Day of the Month')
plt.ylabel('Frequency')
plt.show()

months_order=['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep' ,'oct', 'nov', 'dec'] 
banking['month'] = pd.Categorical(banking['month'], categories=months_order, ordered=True)
g = sns.FacetGrid(banking, col="month", col_wrap=4, height=4, aspect=1.2)
g.map(sns.histplot, 'day', bins=31)
g.set_titles("{col_name}")
g.set_axis_labels(y_var="Frequency")
g.figure.suptitle('Distribution of the Last Contact Day of the Month According to Month')
plt.show()





##-	How does the last contact month vary among the clients?
sns.histplot(x='month', data=banking)
plt.title('Distribution of last contact month')
plt.show()





##-	What is the distribution of the duration of the last contact?
print(banking.duration.describe())

sns.histplot(banking['duration'], bins=100, kde=True)
plt.title('Distribution of Contact Duration')
plt.xlabel('Duration (seconds)')
plt.ylabel('Frequency')
plt.show()





##-	How many contacts were performed during the campaign for each client?
print(banking.campaign.nunique())

sns.countplot(x=banking['campaign'], color='blue')
plt.title('Number of Contacts During the Campaign for Each Client')
plt.xlabel('Number of Contacts')
plt.ylabel('Frequency')
plt.show()






##-	What is the distribution of the number of days passed since the client was last contacted from a previous campaign?
print(banking.pdays.describe())

pdays_1 = banking[banking['pdays'] == -1]
pdays_non_1 = banking[banking['pdays'] != -1]

sns.countplot(x=pdays_1['pdays'], color='blue')
plt.title('Number of Clients with No Previous Contact (pdays=-1)')
plt.xlabel('Number of Days')
plt.ylabel('Frequency')
plt.show()

sns.histplot(pdays_non_1['pdays'], bins=50, kde=True, color='blue')
plt.title('Distribution of the Number of Days Passed Since Last Contact (Excluding pdays=-1)')
plt.xlabel('Number of Days')
plt.ylabel('Frequency')
plt.show()





##-	How many contacts were performed before the current campaign for each client?
print(banking.previous.value_counts())
sns.histplot(banking['previous'], bins=100, color='blue')
plt.title('Number of Contacts Performed Before the Current Campaign for Each Client')
plt.yscale('log')
plt.xlabel('Number of Previous Contacts')
plt.ylabel('Frequency')
plt.show()





##-	What were the outcomes of the previous marketing campaigns?
sns.countplot(x='poutcome',hue='poutcome', data=banking)
plt.title('Outcome of Previous Campaigns')
plt.xlabel('Previous Campaign Outcome')
plt.ylabel('Count')
plt.show()
print(banking.poutcome.value_counts(normalize=True)*100)





##-	What is the distribution of clients who subscribed to a term deposit vs. those who did not?
sns.countplot(x='y', data=banking)
plt.title('Subscription to Term Deposit')
plt.show()
print(banking.y.value_counts(normalize=True)*100)
sns.histplot(data=banking, x='age', hue='y', multiple='fill', bins=30)
plt.title('Subscription to Term Deposit by Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

sns.histplot(x='job', hue='y', data=banking, multiple='fill')
plt.title('Subscription to Term Deposit by Job Type')
plt.ylabel('Job Type')
plt.xticks(rotation=45)
plt.show()






##-	Are there any correlations between different attributes and the likelihood of subscribing to a term deposit?

sns.histplot(x='education', hue='y', data=banking, multiple='fill')
plt.title('Subscription to Term Deposit by Education')
plt.show()
sns.histplot(x='marital', hue='y', data=banking, multiple='fill')
plt.title('Subscription to Term Deposit by Marital Status')
plt.show()
sns.histplot(x='month', hue='y', data=banking, multiple='fill')
plt.title('Subscription to Term Deposit by Month of last contact')
plt.show()

banking['housing'] = banking['housing'].map({'yes': 1, 'no': 0})
banking['loan'] = banking['loan'].map({'yes': 1, 'no': 0})
banking['y'] = banking['y'].map({'yes': 1, 'no': 0})
numeric_data = banking.select_dtypes(include=['int64', 'float64'])

corr_matrix = numeric_data.corr()
sns.heatmap(corr_matrix, annot=True, cmap='RdBu', center=0, linewidths=0.5)
plt.title('Correlation Matrix Heatmap')
plt.show()

correlations = numeric_data.corr()['y'].sort_values(ascending=False)
sns.barplot(hue=correlations.index, y=correlations.values, palette='coolwarm')
plt.title('Correlation of attributes with Subscription to Term Deposit')
plt.xlabel('attributes')
plt.ylabel('Correlation with y')
plt.xticks(rotation=90, ha='right')
plt.legend(title='Attributes')
plt.show()


