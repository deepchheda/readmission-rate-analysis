convert_features = [{'1': 'Emergency', '2': 'Emergency', '3': 'Elective', '4':'Newborn', '5': 'NotAvailable',
                     '6': 'NotAvailable', '7': 'TraumaCenter', '8': 'NotAvailable'},
                    {'1':'dis_home',
                     '2':'dis_another',
                     '3':'dis_nursing',
                     '4':'dis_icf',
                     '5':'dis_another',
                     '6':'dis_home_health',
                     '7':'left_ama',
                     '8':'dis_home_health',
                     '9':'inpatient_this',
                     '10':'noenatal',
                     '11':'dead',
                     '12':'still',
                     '13':'dis_home',
                     '14':'med_facility',
                     '15':'dis_here',
                     '16':'dis_out_other',
                     '17':'still',
                     '18':'null_discharge_disposition',
                     '19':'dead',
                     '20':'dead_med',
                     '21':'dead',
                     '22':'rehab',
                     '23':'dis_long',
                     '24':'dis_nursing',
                     '25':'null_discharge_disposition',
                     '26':'null_discharge_disposition',
                     '27':'dis_another',
                     '28':'dis_psy',
                     '29':'dis_cah',
                     '30':'dis_another'},
                    {'1': 'Referral', '2':'Referral', '3': 'Referral', '4': 'Transfer', '5': 'Transfer', '6': 'Transfer',
                     '10': 'Transfer', '18': 'Transfer', '22':'Transfer', '25': 'Transfer', '26': 'Transfer',
                     '7': 'EmergencyRoom', '8': 'CourtAndLaw', '9': 'null_admissionSource', '15': 'null_admissionSource',
                     '17': 'null_admissionSource', '20':'null_admissionSource',
                     '21': 'null_admissionSource', '11': 'NormalDelivary', '12': 'PrematureDelivary', '13':'SickBaby',
                     '14':'ExtramuralBirth', '19':'ReadmissionToSame', '24': 'ExtramuralBirth', '23':'BornInside'}
                    ]


def redefine_data(data):
    for feature in [3, 4, 5]:
        for d in data:
           d[feature] = convert_features[feature-3][d[feature]]
    return data
