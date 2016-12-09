import csv
import numpy as np
import pandas as pd
from convert_data import redefine_data

def clean_data(path):
    with open(path, 'rb') as csvfile:
        raw_data = csv.reader(csvfile)

        # list_data keeps the raw data as a list of lists
        list_data = list(raw_data)
        list_without_heading = list_data[1:]
        feature_list = list_data[0]

        for row in list_without_heading:
            if row[-1] == 'NO' or row[-1] == '>30':
                row[-1] = 0
            elif row[-1] == '<30':
                row[-1] = 1
            else:
                print "error in label pre-processing"
                print row[-1]
                break

        # removing features what are not relevant based on manual observation
        # removed weight, payer_code and medical_speciality from data
        del feature_list[5]
        del feature_list[9]
        del feature_list[9]
        del feature_list[0]
        del feature_list[0]
        del feature_list[20]
        del feature_list[20]
        del feature_list[20]
        del feature_list[21]
        del feature_list[23]
        del feature_list[25]
        del feature_list[25]
        del feature_list[25]
        del feature_list[25]
        del feature_list[25]
        del feature_list[25]
        del feature_list[26]
        del feature_list[26]
        del feature_list[26]
        del feature_list[26]
        del feature_list[26]
        for row in list_without_heading:
            del row[5]
            del row[9]
            del row[9]
            del row[0]
            del row[0]
            del row[20]
            del row[20]
            del row[20]
            del row [21]
            del row [23]
            del row [25]
            del row [25]
            del row[25]
            del row[25]
            del row[25]
            del row[25]
            del row[26]
            del row[26]
            del row[26]
            del row[26]
            del row[26]

        # Using most_frequent class to fill missing values
        complete_data = fill_values(list_without_heading)

        np_data = np.array([np.array(rr) for rr in complete_data])
        # changing data in cloumns : 3, 4 and 5
        refactored_data = redefine_data(np_data)
        # check number of unique values in a column
        # 13 14 15 have bad values
        num = 28
        # # no 20 and 21 are useless
        # for col in range(num, num + 1):
        #     dict_for_race = {}
        #     print feature_list[col]
        #     for row in refactored_data:
        #         if row[col] not in dict_for_race:
        #             dict_for_race[row[col]] = 1
        #         else:
        #             dict_for_race[row[col]] += 1
        #     for x, y in dict_for_race.iteritems():
        #         print str(x) + " " + str(y)
        #     print "---------------------------------------------------------------"

        panda_data = pd.DataFrame(refactored_data)
        panda_data.columns = feature_list

        # splitting categorical data to binary form
        for column in ['gender', 'race', 'age', 'admission_type_id', 'discharge_disposition_id', 'admission_source_id']:
            dummy_data = pd.get_dummies(panda_data[column])
            del panda_data[column]
            panda_data[dummy_data.columns] = dummy_data
        np.empty_like(np_data)
        np.empty_like(refactored_data)

        data_from_df = panda_data.as_matrix()
        print data_from_df.shape


def fill_values(data):
    for row in data:
        if row[0] == '?':
            row[0] = 'AfricanAmerican'
        if row[1] == 'Unknown/Invalid':
            row[1] = 'Female'
    return data

















