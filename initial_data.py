import os
import pandas as pd
import numpy as np

file_name = "flory_data.dta"

os.chdir("C:\\Users\\kiera\\Desktop\\Lowe")

data = pd.read_stata(file_name, index_col='id')

# data = data[data.ApplicationStatusText != '']

data = data[data.treatment == '']
data = data.drop(columns=['appNum', 'AppSubmissionDate_original'])
# print(data.shape)

# sorter = []

# data = data[data.ApplicationStatusText != 'Chose Other BLK Offer']
data = data[data.ApplicationStatusText != '']

# data = data.drop_duplicates()
#print(data.shape)
#a = (data.ApplicationStatusText.unique())
#print(a)
#print(type(a))

sorter = [
    'Hired',

    'Offer Accepted – Offer Confirmation Form Complete',
    'Offer Reneged',
    'Offer Declined',
    'Offer Rescinded',
    'Chose Other BLK Offer',
    'Offer Accepted – Offer Confirmation Form in Progress',
    'Application withdrawn > Offer extended',

    'Final Interview - Rejected',
    'Application Withdrawn > Final Interview - Selected',
    'Final Interview - Scheduled',
    'Final Interview - Hold',

    'Application withdrawn > Final round stage – invited',
    'Application withdrawn > Final round stage – scheduled',
    'Application withdrawn > Final round stage - on hold',

    'Business Review',
    'Business Review - Rejected',
    'Application withdrawn > Business Review - on hold',
    'Application withdrawn > Business Review',
    'Business Review - Pending Reject',
    'Business Review - Hold',

    '1st Interview - Rejected',
    '1st Interview - Invited',
    '1st Interview - Selected',
    'Application Withdrawn > 1st Interview - Selected',
    'Application withdrawn > 1st round interview - on hold',
    'Application withdrawn > 1st round interview – invited',
    'Application withdrawn > 1st round interview – scheduled',

    'HR Review',
    'HR Review - Reject',
    'HR Review - Hold',
    'Application withdrawn > HR Review',
    'Application withdrawn > HR Review - Hold',
    'HR Review - Pending Reject'
    
    'HireVue – Rejected',
    'HireVue - Incomplete',
    'HireVue - Completed',
    'HireVue - Invited',
    'Application Withdrawn > HireVue',
    'HireVue – Pending Reject',
    'Application Withdrawn > HireVue - Hold',

    'Positions Full',
    'Application Withdrawn > Potential Duplicate',
    'Application Withdrawn > New Application',
    'Rejected - minimum requirements not met',
    'Confirmed Duplicate',
    'Potential Duplicate',
    'Minimum Requirements not met - Pending Reject'     
    'Application Submitted - Pre-Forking',
    'Application withdrawn'
    'Application withdrawn > Application submitted – pre-forking',
    'Duplicate Check',
    ]

sorterIndex = dict(zip(sorter, range(len(sorter))))

print(data.shape)
#print(data['ApplicationStatusText'].head())

data.ApplicationStatusText = data.ApplicationStatusText.astype("category")
data.ApplicationStatusText.cat.set_categories(sorter, inplace=True)
#print(data.ApplicationStatusText)
data = data.sort_values(['ApplicationStatusText'])
#print(data['ApplicationStatusText'].head())
# data.to_excel('flory_data.xlsx')
data = data[~data.index.duplicated(keep='first')]
print(data.shape)
'''
>> Chi Square <<
chisquare = data[['OLDappformDisability', 'offer']]
chisquare.offer = chisquare.offer.astype('int64')
#print(chisquare.head)

chisquare = chisquare[chisquare.OLDappformDisability != '']
#print(chisquare.head)

crosstab = pd.crosstab(chisquare.OLDappformDisability, chisquare.offer, margins=True)
print(crosstab)

row_sum = crosstab.iloc[0:3,2].values
exp = []
for j in range(2):
    for val in ct.iloc[2,0:4].values:
        exp.append(val * row_sum[j] / ct.loc['All', 'All'])
print(exp)
'''

## >> Rename Data Names, like offer and disability

# data = data.dropna(subset='')

# a = data['ApplicationStatusText'].value_counts()
# print(a)


# series = data['Ethnicityrollup']
# series = series[~series.index.duplicated(keep='first')]
# b = series.value_counts(normalize= True) * 100
# print(b)

# Submission Number us blank, they never submitted it?
# If application status text is blank, submission id is always blank

# raw_data = pd.DataFrame()
# raw_data['ApplicationStatusText'] = data['ApplicationStatusText']
# raw_data['ivyleague'] = data['ivyleague']
# raw_data['treatment'] = data['treatteam']
# #raw_data['treatment'].astype('int')
# #a = raw_data.dtypes
# raw_data = raw_data[raw_data.treatment != 1.0]
# raw_data = raw_data[raw_data.treatment != 0.0]
# #print(raw_data.shape)
# raw_data.replace("", np.nan, inplace=True)
# #raw_data = raw_data[raw_data.ApplicationStatusText.notnull()]
# raw_data.dropna(subset = ['ApplicationStatusText'], inplace=True)

# print(raw_data['ivyleague'].value_counts())

''' Queries
# get number of data from Ivys
print(raw_data[(raw_data.ivyleague == 'Ivy-league')]['ApplicationStatusText'].value_counts())
print(raw_data[(raw_data.ivyleague == 'No Ivy-league')]['ApplicationStatusText'].value_counts())
'''

# raw_data = raw_data.loc[raw_data['treatment'] != 1 or 2]
# print(raw_data.shape)

# print(raw_data)


# a = data['Ethnicityrollup'].value_counts(normalize= True) * 100
# print(a)
