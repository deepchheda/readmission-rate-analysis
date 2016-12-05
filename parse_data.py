import csv
import numpy as np
import pandas as pd

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
        del feature_list [9]
        del feature_list [0]
        for row in list_without_heading:
            del row[5]
            del row[9]
            del row[9]
            del row[0]

        # check number of unique values in a column
        #
        # for col in range(2,3):
        #     dict_for_race = {}
        #     print feature_list[col]
        #     for row in list_without_heading:
        #         if row[col] not in dict_for_race:
        #             dict_for_race[row[col]] = 1
        #         else:
        #             dict_for_race[row[col]] += 1
        #     for x, y in dict_for_race.iteritems():
        #         print str(x) + " " + str(y)
        #     print "---------------------------------------------------------------"



        # Using most_frequent class to fill missing values
        complete_data = fill_values(list_without_heading)



        np_data = np.array([np.array(rr) for rr in complete_data])
        # le = preprocessing.LabelEncoder()
        # le.fit(["Male", "Female"])
        # np_data[:, 2] = le.transform(np_data[:,2])


        #
        # dict_for_race = {}
        # print feature_list[2]
        # for row in np_data:
        #     if row[2] not in dict_for_race:
        #         dict_for_race[row[2]] = 1
        #     else:
        #         dict_for_race[row[2]] += 1
        # for x, y in dict_for_race.iteritems():
        #     print str(x) + " " + str(y)

        panda_data = pd.DataFrame(np_data)
        panda_data.columns = feature_list

        # splitting categorical data to binary form
        for column in ['gender', 'age', 'admission_type_id', 'discharge_disposition_id', 'admission_source_id']:
            dummy_data = pd.get_dummies(panda_data[column])
            del panda_data[column]
            panda_data[dummy_data.columns] = dummy_data
        print panda_data.columns[45:]


def fill_values(data):
    for row in data:
        if row[1] == '?':
            row[1] = 'AfricanAmerican'
        if row[2] == 'Unknown/Invalid':
            row[2] = 'Female'
    return data

















