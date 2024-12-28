# I removed invalid use_tag runs by using the dataset excel.
subjects_dict = {
    'sub-jh101': ['01', '02', '03', '04'],
    'sub-jh102': ['01', '02', '03', '04', '05', '06'],
    'sub-jh103': ['01', '02', '03'],
    'sub-jh104': ['01', '02'],
    'sub-jh105': ['02', '04'],
    'sub-jh108': ['01', '06'],
    'sub-pt01':  ['01', '02', '03', '04'],
    'sub-pt2':   ['01', '02', '03'],
    'sub-pt3':   ['01', '02'],
    'sub-pt6':   ['01', '02', '03'],
    'sub-pt7':   ['01', '02', '03'],
    'sub-pt8':   ['01', '02', '03'],
    'sub-pt10':  ['01', '02', '03'],
    'sub-pt11':  ['01', '02', '03', '04'],
    'sub-pt12':  ['01', '02'],
    'sub-pt13':  ['01', '02', '03', '04'],
    'sub-pt14':  ['01', '02', '03'],
    'sub-pt15':  ['01', '02', '03', '04'],
    'sub-pt16':  ['01', '02', '03'],
    'sub-pt17':  ['02'],
    'sub-umf001': ['01'],
    'sub-ummc001': ['01', '02', '03'],
    'sub-ummc002': ['01', '02', '03'],
    'sub-ummc003': ['01', '02', '03'],
    'sub-ummc004': ['01', '02', '03'],
    'sub-ummc005': ['01', '02'],
    'sub-ummc006': ['01', '02', '03'],
    'sub-ummc007': ['01', '02', '03'],
    'sub-ummc008': ['01', '02', '03'],
    'sub-ummc009': ['01', '02', '03'],
}

FREQUENCY_BANDS = {
    'delta': (1, 3),
    'theta': (4, 7),
    'alpha': (8, 13),
    'beta': (14, 30),
    'gamma': (31, 50)
}

subject_keywords = {
    'sub-jh101': {
        '01': {
            'onset': ['SZ EVENT # (EEG SZ)'],
            'offset': ['Z ELECTROGRAPHIC END']
        },
        '02': {
            'onset': ['SZ EVENT # (EEG SZ)'],
            'offset': ['Z ELECTROGRAPHIC END']
        },
        '03': {
            'onset': ['SZ EVENT # (EEG SZ)'],
            'offset': ['Z ELECTROGRAPHIC END']
        },
        '04': {
            'onset': ['SZ EVENT # (EEG SZ)'],
            'offset': ['Z ELECTROGRAPHIC END']
        }
    },
    'sub-jh102': {
        '01': {
            'onset': ['Z CLINICAL ONSET'],
            'offset': ['Z ELECTROGRAPHIC END']
        },
        '02': {
            'onset': ['Z ELECTROGRAPHIC ONS'],
            'offset': ['Z ELECTROGRAPHIC END']
        },
        '03': {
            'onset': ['Z ELECTROGRAPHIC ONS'],
            'offset': ['Z SEIZURE OVER']
        },
        '04': {
            'onset': ['Z ELECTROGRAPHIC ONS'],
            'offset': ['Z RSF OVER']
        },
        '05': {
            'onset': ['Z ELELCTROGRAPHIC ON'],
            'offset': ['z clinical signs ove']
        },
        '06': {
            'onset': ['Z ELECTROGRAPHIC ONS'],
            'offset': ['Z RIGHT OVER']
        }
    },
    'sub-jh103': {
        '01': {
            'onset': ['SZ EVENT # (PB SZ)'],
            'offset': ['Z DEVOLUTION']
        },
        '02': {
            'onset': ['SZ EVENT # (PB SZ)'],
            'offset': ['Z ELECTROGRAPHIC END']
        },
        '03': {
            'onset': ['Z GENERALIZES'],
            'offset': ['Z ELECTROGRAPHIC END']
        }
    },
    'sub-jh104': {
        '01': {
            'onset': ['SZ EVENT # (PB SZ)'],
            'offset': ['Z DEVOLUTION']
        },
        '02': {
            'onset': ['SZ EVENT # (PB SZ)'],
            'offset': ['Z DEVOLUTION']
        }
    },
    'sub-jh105': {
        '02': {
            'onset': ['SZ EVENT # (PB SZ)'],
            'offset': ['Z EVENT OVER']
        },
        '04': {
            'onset': ['SZ EVENT # (PB SZ)'],
            'offset': ['Z OVER']
        }
    },
    'sub-jh108': {
        '01': {
            'onset': ['SZ EVENT #(PB SZ)'],
            'offset': ['END FAST']
        },
        '06': {
            'onset': ['SZ EVENT #(PB SZ)'],
            'offset': ['Z STOPPING']
        }

    },
    'sub-pt01': {
        '01': {
            'onset': ['onset'],
            'offset': ['offset']
        },
        '02': {
            'onset': ['AD1-3 onset'],
            'offset': ['offset']
        },
        '03': {
            'onset': ['onset'],
            'offset': ['offset']
        },
        '04': {
            'onset': ['definite onset'],
            'offset': ['offset']
        }
    },
    'sub-pt2': {
        '01': {
            'onset': ['?onset ?TT1 then PST'],
            'offset': ['offset']
        },
        '02': {
            'onset': ['clinical onset'],
            'offset': ['offset with attenuta']
        },
        '03': {
            'onset': ['definite onset'],
            'offset': ['offset with attenuat']
        }
    },
    'sub-pt3': {
        '01': {
            'onset': ['onset'],
            'offset': ['sz end']
        },
        '02': {
            'onset': ['clinical onset'],
            'offset': ['offset']
        }
    },
    'sub-pt6': {
        '01': {
            'onset': ['ictal onset'],
            'offset': ['offset']
        },
        '02': {
            'onset': ['clinical onset'],
            'offset': ['offset']
        },
        '03': {
            'onset': ['clinical onset'],
            'offset': ['offset']
        }
    },
    'sub-pt7': {
        '01': {
            'onset': ['onset'],
            'offset': ['offset']
        },
        '02': {
            'onset': ['onset'],
            'offset': ['offset']
        },
        '03': {
            'onset': ['onset'],
            'offset': ['offset']
        }
    },
    'sub-pt8': {
        '01': {
            'onset': ['onset'],
            'offset': ['offset']
        },
        '02': {
            'onset': ['onset'],
            'offset': ['offset']
        },
        '03': {
            'onset': ['onset'],
            'offset': ['offset']
        }
    },
    'sub-pt10': {
        '01': {
            'onset': ['onset'],
            'offset': ['offset']
        },
        '02': {
            'onset': ['onset'],
            'offset': ['offset']
        },
        '03': {
            'onset': ['onset'],
            'offset': ['offset']
        }
    },
    'sub-pt11': {
        '01': {
            'onset': ['onset'],
            'offset': ['offset']
        },
        '02': {
            'onset': ['onset'],
            'offset': ['offset']
        },
        '03': {
            'onset': ['start'],
            'offset': ['end']
        },
        '04': {
            'onset': ['onset'],
            'offset': ['offset']
        }
    },
    'sub-pt12': {
        '01': {
            'onset': ['onset TT3'],
            'offset': ['offset']
        },
        '02': {
            'onset': ['onset'],
            'offset': ['offset']
        }
    },
    'sub-pt13': {
        '01': {
            'onset': ['sz onset #18'],
            'offset': ['offset']
        },
        '02': {
            'onset': ['sz onset #19'],
            'offset': ['Offset']
        },
        '03': {
            'onset': ['SEIZURE #17 ONSET'],
            'offset': ['offset']
        },
        '04': {
            'onset': ['sz #12 onset'],
            'offset': ['offset']
        }
    },
    'sub-pt14': {
        '01': {
            'onset': ['EEG onset'],
            'offset': ['offset']
        },
        '02': {
            'onset': ['eeg onset'],
            'offset': ['offset']
        },
        '03': {
            'onset': ['DEFINITE ONSET'],
            'offset': ['offset']
        }
    },
    'sub-pt15': {
        '01': {
            'onset': ['Onset'],
            'offset': ['Offset']
        },
        '02': {
            'onset': ['Onset'],
            'offset': ['offset']
        },
        '03': {
            'onset': ['Onset'],
            'offset': ['definite off']
        },
        '04': {
            'onset': ['Onset'],
            'offset': ['Offset']
        }
    },
    'sub-pt16': {
        '01': {
            'onset': ['Onset'],
            'offset': ['Offset']
        },
        '02': {
            'onset': ['onset'],
            'offset': ['Offset']
        },
        '03': {
            'onset': ['onset'],
            'offset': ['offset']
        }
    },
    'sub-pt17': {
        '02': {
            'onset': ['onset'],
            'offset': ['offset']
        }
    },
    'sub-umf001': {
        '01': {
            'onset': ['eeg sz start'],
            'offset': ['eeg sz end']
        }
    },
    'sub-ummc001': {
        '01': {
            'onset': ['sz onset'],
            'offset': []
        },
        '02': {
            'onset': ['sz onset'],
            'offset': []
        },
        '03': {
            'onset': ['sz onset'],
            'offset': []
        }
    },
    'sub-ummc002': {
        '01': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        },
        '02': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        },
        '03': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        }
    },
    'sub-ummc003': {
        '01': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        },
        '02': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        },
        '03': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        }
    },
    'sub-ummc004': {
        '01': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        },
        '02': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        },
        '03': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        }
    },
    'sub-ummc005': {
        '01': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        },
        '02': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        }
    },
    'sub-ummc006': {
        '01': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        },
        '02': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        },
        '03': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        }
    },
    'sub-ummc007': {
        '01': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        },
        '02': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        },
        '03': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        }
    },
    'sub-ummc008': {
        '01': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        },
        '02': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        },
        '03': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        }
    },
    'sub-ummc009': {
        '01': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        },
        '02': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        },
        '03': {
            'onset': ['sz onset'],
            'offset': ['sz offset']
        }
    }
}



# Combined dictionary for all subjects and runs
surgery_outcome_dict = {
    ('sub-jh101', '01'): {
        'channels': ['LAF1', 'LAF2', 'LAF3', 'LAF4', 'LAF5', 'LAF6', 'LAF7', 'LAF8', 'LAT1', 'LAT2', 'LAT3', 'LAT6', 'LAT7', 'LAT8', 'LAT9', 'LMT1', 'LAF9', 'LAF10', 'LMT2', 'LMT3', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LAD1', 'LAD2', 'LAD3', 'LAD4', 'LAD5', 'LAD6', '$LAF9', '$LAF10', 'LAD7', 'LAD8', 'LAH1', 'LAH2', 'LAH3', 'LAH4', 'LAH5', 'LAH6', 'LAH8', 'LPH1', 'LPH2', 'LPH3', 'LPH4', 'LPH5', 'LPH6', 'LPH7', 'LPH8', 'LTG1', 'LTG2', 'LTG3', 'LTG4', 'LTG5', 'LTG6', 'LTG7', 'LTG8', 'LTG9', 'LTG10', 'LTG11', 'LTG12', 'LTG13', 'LTG14', 'LTG15', 'LTG19', 'LTG20', 'LTG21', 'LTG22', 'LTG23', 'LTG24', 'LTG25', 'LTG26', 'LTG27', 'LTG28', 'LTG29', 'LTG30', 'LTG31', 'LTG32', 'LTG33', 'LTG34', 'LTG35', 'LTG36', 'LTG37', 'LTG38', 'LTG39', 'LTG40', 'LTG41', 'LTG42', 'LTG43', 'LTG44', 'LTG45', 'LTG46', 'LTG47', 'LTG48', 'LTG51', 'LTG52', 'LTG53', 'LTG54', 'LTG55', 'LTG56', 'LTG57', 'LTG58', 'LTG59', 'LTG60', 'LTG61', 'LTG62', 'LTG63', 'LTG64'],
        'soz_channels': ['LAT1', 'LAT2', 'LAT6', 'LAT7', 'LAH6'],
        'surgery_outcome': 'F'
    },
    ('sub-jh101', '02'): {
        'channels': ['LAF1', 'LAF2', 'LAF3', 'LAF4', 'LAF5', 'LAF6', 'LAF7', 'LAF8', 'LAT1', 'LAT2', 'LAT3', 'LAT6', 'LAT7', 'LAT8', 'LAT9', 'LMT1', 'LAF9', 'LAF10', 'LMT2', 'LMT3', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LAD1', 'LAD2', 'LAD3', 'LAD4', 'LAD5', 'LAD6', '$LAF9', '$LAF10', 'LAD7', 'LAD8', 'LAH1', 'LAH2', 'LAH3', 'LAH4', 'LAH5', 'LAH6', 'LAH8', 'LPH1', 'LPH2', 'LPH3', 'LPH4', 'LPH5', 'LPH6', 'LPH7', 'LPH8', 'LTG1', 'LTG2', 'LTG3', 'LTG4', 'LTG5', 'LTG6', 'LTG7', 'LTG8', 'LTG9', 'LTG10', 'LTG11', 'LTG12', 'LTG13', 'LTG14', 'LTG15', 'LTG19', 'LTG20', 'LTG21', 'LTG22', 'LTG23', 'LTG24', 'LTG25', 'LTG26', 'LTG27', 'LTG28', 'LTG29', 'LTG30', 'LTG31', 'LTG32', 'LTG33', 'LTG34', 'LTG35', 'LTG36', 'LTG37', 'LTG38', 'LTG39', 'LTG40', 'LTG41', 'LTG42', 'LTG43', 'LTG44', 'LTG45', 'LTG46', 'LTG47', 'LTG48', 'LTG51', 'LTG52', 'LTG53', 'LTG54', 'LTG55', 'LTG56', 'LTG57', 'LTG58', 'LTG59', 'LTG60', 'LTG61', 'LTG62', 'LTG63', 'LTG64'],
        'soz_channels': ['LAT1', 'LAT2', 'LAT6', 'LAT7', 'LAH6'],
        'surgery_outcome': 'F'
    },
    ('sub-jh101', '03'): {
        'channels': ['LAF1', 'LAF2', 'LAF3', 'LAF4', 'LAF5', 'LAF6', 'LAF7', 'LAF8', 'LAT1', 'LAT2', 'LAT3', 'LAT6', 'LAT7', 'LAT8', 'LAT9', 'LMT1', 'LAF9', 'LAF10', 'LMT2', 'LMT3', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LAD1', 'LAD2', 'LAD3', 'LAD4', 'LAD5', 'LAD6', '$LAF9', '$LAF10', 'LAD7', 'LAD8', 'LAH1', 'LAH2', 'LAH3', 'LAH4', 'LAH5', 'LAH6', 'LAH8', 'LPH1', 'LPH2', 'LPH3', 'LPH4', 'LPH5', 'LPH6', 'LPH7', 'LPH8', 'LTG1', 'LTG2', 'LTG3', 'LTG4', 'LTG5', 'LTG6', 'LTG7', 'LTG8', 'LTG9', 'LTG10', 'LTG11', 'LTG12', 'LTG13', 'LTG14', 'LTG15', 'LTG19', 'LTG20', 'LTG21', 'LTG22', 'LTG23', 'LTG24', 'LTG25', 'LTG26', 'LTG27', 'LTG28', 'LTG29', 'LTG30', 'LTG31', 'LTG32', 'LTG33', 'LTG34', 'LTG35', 'LTG36', 'LTG37', 'LTG38', 'LTG39', 'LTG40', 'LTG41', 'LTG42', 'LTG43', 'LTG44', 'LTG45', 'LTG46', 'LTG47', 'LTG48', 'LTG51', 'LTG52', 'LTG53', 'LTG54', 'LTG55', 'LTG56', 'LTG57', 'LTG58', 'LTG59', 'LTG60', 'LTG61', 'LTG62', 'LTG63', 'LTG64'],
        'soz_channels': ['LAT1', 'LAT2', 'LAT6', 'LAT7', 'LAH6'],
        'surgery_outcome': 'F'
    },
    ('sub-jh101', '04'): {
        'channels': ['LAF1', 'LAF2', 'LAF3', 'LAF4', 'LAF5', 'LAF6', 'LAF7', 'LAF8', 'LAT1', 'LAT2', 'LAT3', 'LAT6', 'LAT7', 'LAT8', 'LAT9', 'LMT1', 'LAF9', 'LAF10', 'LMT2', 'LMT3', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LAD1', 'LAD2', 'LAD3', 'LAD4', 'LAD5', 'LAD6', '$LAF9', '$LAF10', 'LAD7', 'LAD8', 'LAH1', 'LAH2', 'LAH3', 'LAH4', 'LAH5', 'LAH6', 'LAH8', 'LPH1', 'LPH2', 'LPH3', 'LPH4', 'LPH5', 'LPH6', 'LPH7', 'LPH8', 'LTG1', 'LTG2', 'LTG3', 'LTG4', 'LTG5', 'LTG6', 'LTG7', 'LTG8', 'LTG9', 'LTG10', 'LTG11', 'LTG12', 'LTG13', 'LTG14', 'LTG15', 'LTG19', 'LTG20', 'LTG21', 'LTG22', 'LTG23', 'LTG24', 'LTG25', 'LTG26', 'LTG27', 'LTG28', 'LTG29', 'LTG30', 'LTG31', 'LTG32', 'LTG33', 'LTG34', 'LTG35', 'LTG36', 'LTG37', 'LTG38', 'LTG39', 'LTG40', 'LTG41', 'LTG42', 'LTG43', 'LTG44', 'LTG45', 'LTG46', 'LTG47', 'LTG48', 'LTG51', 'LTG52', 'LTG53', 'LTG54', 'LTG55', 'LTG56', 'LTG57', 'LTG58', 'LTG59', 'LTG60', 'LTG61', 'LTG62', 'LTG63', 'LTG64'],
        'soz_channels': ['LAT1', 'LAT2', 'LAT6', 'LAT7', 'LAH6'],
        'surgery_outcome': 'F'
    },
    ('sub-jh102', '01'): {
        'channels': ['LAF1', 'LAF3', 'LAF5', 'LAF7', 'LAF8', 'LMF1', 'LMF2', 'LMF3', 'LMF6', 'LMF7', 'LMF8', 'LPF1', 'LPF2', 'LPF3', 'LPF4', 'LPF5', 'LPF6', 'LPF7', 'LPF8', 'LMF4', 'LMF5', 'LSF1', 'LSF2', 'LSF3', 'LSF4', 'LSF5', 'LSF6', 'LSF7', 'LSF8', 'LAT1', 'LAT2', 'LAT3', 'LAT4', 'LAT5', 'LAT6', 'LBT1', '$LMF4', '$LMF5', 'LBT2', 'LBT3', 'LBT4', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LTF1', 'LTF2', 'LTF3', 'LTF4', 'LTF5', 'LTF6', 'LTF7', 'LTF8', 'RAF1', 'RAF2', 'RAF3', 'RAF4', 'RAF5', 'RAF6', 'RAF7', 'RAF8', 'RMF1', 'RMF2', 'RMF3', 'RMF4', 'RMF5', 'RMF6', 'RMF7', 'RMF8', 'RPF1', 'RPF2', 'RPF3', 'RPF4', 'RPF5', 'RPF6', 'RPF7', 'RPF8', 'RSF1', 'RSF2', 'RSF3', 'RSF4', 'RSF5', 'RSF6', 'RSF7', 'RSF8', 'RAT1', 'RAT2', 'RAT3', 'RAT4', 'RAT5', 'RAT6', 'RBT1', 'RBT2', 'RBT3', 'RBT4', 'RPT1', 'RPT2', 'RPT3', 'RPT4', 'RPT5', 'RPT6', 'RPT7', 'RPT8', 'RTF1', 'RTF2', 'RTF3', 'RTF4', 'RTF5', 'RTF6', 'RTF7', 'RTF8'],
        'soz_channels': ['RAT1', 'RAT2'],
        'surgery_outcome': 'NR'
    },
    ('sub-jh102', '02'): {
        'channels': ['LAF1', 'LAF3', 'LAF5', 'LAF7', 'LAF8', 'LMF1', 'LMF2', 'LMF3', 'LMF6', 'LMF7', 'LMF8', 'LPF1', 'LPF2', 'LPF3', 'LPF4', 'LPF5', 'LPF6', 'LPF7', 'LPF8', 'LMF4', 'LMF5', 'LSF1', 'LSF2', 'LSF3', 'LSF4', 'LSF5', 'LSF6', 'LSF7', 'LSF8', 'LAT1', 'LAT2', 'LAT3', 'LAT4', 'LAT5', 'LAT6', 'LBT1', '$LMF4', '$LMF5', 'LBT2', 'LBT3', 'LBT4', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LTF1', 'LTF2', 'LTF3', 'LTF4', 'LTF5', 'LTF6', 'LTF7', 'LTF8', 'RAF1', 'RAF2', 'RAF3', 'RAF4', 'RAF5', 'RAF6', 'RAF7', 'RAF8', 'RMF1', 'RMF2', 'RMF3', 'RMF4', 'RMF5', 'RMF6', 'RMF7', 'RMF8', 'RPF1', 'RPF2', 'RPF3', 'RPF4', 'RPF5', 'RPF6', 'RPF7', 'RPF8', 'RSF1', 'RSF2', 'RSF3', 'RSF4', 'RSF5', 'RSF6', 'RSF7', 'RSF8', 'RAT1', 'RAT2', 'RAT3', 'RAT4', 'RAT5', 'RAT6', 'RBT1', 'RBT2', 'RBT3', 'RBT4', 'RPT1', 'RPT2', 'RPT3', 'RPT4', 'RPT5', 'RPT6', 'RPT7', 'RPT8', 'RTF1', 'RTF2', 'RTF3', 'RTF4', 'RTF5', 'RTF6', 'RTF7', 'RTF8'],
        'soz_channels': ['RAT1', 'RAT2'],
        'surgery_outcome': 'NR'
    },
    ('sub-jh102', '03'): {
        'channels': ['LAF1', 'LAF3', 'LAF5', 'LAF7', 'LAF8', 'LMF1', 'LMF2', 'LMF3', 'LMF6', 'LMF7', 'LMF8', 'LPF1', 'LPF2', 'LPF3', 'LPF4', 'LPF5', 'LPF6', 'LPF7', 'LPF8', 'LMF4', 'LMF5', 'LSF1', 'LSF2', 'LSF3', 'LSF4', 'LSF5', 'LSF6', 'LSF7', 'LSF8', 'LAT1', 'LAT2', 'LAT3', 'LAT4', 'LAT5', 'LAT6', 'LBT1', '$LMF4', '$LMF5', 'LBT2', 'LBT3', 'LBT4', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LTF1', 'LTF2', 'LTF3', 'LTF4', 'LTF5', 'LTF6', 'LTF7', 'LTF8', 'RAF1', 'RAF2', 'RAF3', 'RAF4', 'RAF5', 'RAF6', 'RAF7', 'RAF8', 'RMF1', 'RMF2', 'RMF3', 'RMF4', 'RMF5', 'RMF6', 'RMF7', 'RMF8', 'RPF1', 'RPF2', 'RPF3', 'RPF4', 'RPF5', 'RPF6', 'RPF7', 'RPF8', 'RSF1', 'RSF2', 'RSF3', 'RSF4', 'RSF5', 'RSF6', 'RSF7', 'RSF8', 'RAT1', 'RAT2', 'RAT3', 'RAT4', 'RAT5', 'RAT6', 'RBT1', 'RBT2', 'RBT3', 'RBT4', 'RPT1', 'RPT2', 'RPT3', 'RPT4', 'RPT5', 'RPT6', 'RPT7', 'RPT8', 'RTF1', 'RTF2', 'RTF3', 'RTF4', 'RTF5', 'RTF6', 'RTF7', 'RTF8'],
        'soz_channels': ['RAT1', 'RAT2'],
        'surgery_outcome': 'NR'
    },
    ('sub-jh102', '04'): {
        'channels': ['LAF1', 'LAF3', 'LAF5', 'LAF7', 'LAF8', 'LMF1', 'LMF2', 'LMF3', 'LMF6', 'LMF7', 'LMF8', 'LPF1', 'LPF2', 'LPF3', 'LPF4', 'LPF5', 'LPF6', 'LPF7', 'LPF8', 'LMF4', 'LMF5', 'LSF1', 'LSF2', 'LSF3', 'LSF4', 'LSF5', 'LSF6', 'LSF7', 'LSF8', 'LAT1', 'LAT2', 'LAT3', 'LAT4', 'LAT5', 'LAT6', 'LBT1', '$LMF4', '$LMF5', 'LBT2', 'LBT3', 'LBT4', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LTF1', 'LTF2', 'LTF3', 'LTF4', 'LTF5', 'LTF6', 'LTF7', 'LTF8', 'RAF1', 'RAF2', 'RAF3', 'RAF4', 'RAF5', 'RAF6', 'RAF7', 'RAF8', 'RMF1', 'RMF2', 'RMF3', 'RMF4', 'RMF5', 'RMF6', 'RMF7', 'RMF8', 'RPF1', 'RPF2', 'RPF3', 'RPF4', 'RPF5', 'RPF6', 'RPF7', 'RPF8', 'RSF1', 'RSF2', 'RSF3', 'RSF4', 'RSF5', 'RSF6', 'RSF7', 'RSF8', 'RAT1', 'RAT2', 'RAT3', 'RAT4', 'RAT5', 'RAT6', 'RBT1', 'RBT2', 'RBT3', 'RBT4', 'RPT1', 'RPT2', 'RPT3', 'RPT4', 'RPT5', 'RPT6', 'RPT7', 'RPT8', 'RTF1', 'RTF2', 'RTF3', 'RTF4', 'RTF5', 'RTF6', 'RTF7', 'RTF8'],
        'soz_channels': ['RAT1', 'RAT2'],
        'surgery_outcome': 'NR'
    },
    ('sub-jh102', '05'): {
        'channels': ['LAF1', 'LAF3', 'LAF5', 'LAF7', 'LAF8', 'LMF1', 'LMF2', 'LMF3', 'LMF6', 'LMF7', 'LMF8', 'LPF1', 'LPF2', 'LPF3', 'LPF4', 'LPF5', 'LPF6', 'LPF7', 'LPF8', 'LMF4', 'LMF5', 'LSF1', 'LSF2', 'LSF3', 'LSF4', 'LSF5', 'LSF6', 'LSF7', 'LSF8', 'LAT1', 'LAT2', 'LAT3', 'LAT4', 'LAT5', 'LAT6', 'LBT1', '$LMF4', '$LMF5', 'LBT2', 'LBT3', 'LBT4', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LTF1', 'LTF2', 'LTF3', 'LTF4', 'LTF5', 'LTF6', 'LTF7', 'LTF8', 'RAF1', 'RAF2', 'RAF3', 'RAF4', 'RAF5', 'RAF6', 'RAF7', 'RAF8', 'RMF1', 'RMF2', 'RMF3', 'RMF4', 'RMF5', 'RMF6', 'RMF7', 'RMF8', 'RPF1', 'RPF2', 'RPF3', 'RPF4', 'RPF5', 'RPF6', 'RPF7', 'RPF8', 'RSF1', 'RSF2', 'RSF3', 'RSF4', 'RSF5', 'RSF6', 'RSF7', 'RSF8', 'RAT1', 'RAT2', 'RAT3', 'RAT4', 'RAT5', 'RAT6', 'RBT1', 'RBT2', 'RBT3', 'RBT4', 'RPT1', 'RPT2', 'RPT3', 'RPT4', 'RPT5', 'RPT6', 'RPT7', 'RPT8', 'RTF1', 'RTF2', 'RTF3', 'RTF4', 'RTF5', 'RTF6', 'RTF7', 'RTF8'],
        'soz_channels': ['RAT1', 'RAT2'],
        'surgery_outcome': 'NR'
    },
    ('sub-jh102', '06'): {
        'channels': ['LAF1', 'LAF3', 'LAF5', 'LAF7', 'LAF8', 'LMF1', 'LMF2', 'LMF3', 'LMF6', 'LMF7', 'LMF8', 'LPF1', 'LPF2', 'LPF3', 'LPF4', 'LPF5', 'LPF6', 'LPF7', 'LPF8', 'LMF4', 'LMF5', 'LSF1', 'LSF2', 'LSF3', 'LSF4', 'LSF5', 'LSF6', 'LSF7', 'LSF8', 'LAT1', 'LAT2', 'LAT3', 'LAT4', 'LAT5', 'LAT6', 'LBT1', '$LMF4', '$LMF5', 'LBT2', 'LBT3', 'LBT4', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8', 'LTF1', 'LTF2', 'LTF3', 'LTF4', 'LTF5', 'LTF6', 'LTF7', 'LTF8', 'RAF1', 'RAF2', 'RAF3', 'RAF4', 'RAF5', 'RAF6', 'RAF7', 'RAF8', 'RMF1', 'RMF2', 'RMF3', 'RMF4', 'RMF5', 'RMF6', 'RMF7', 'RMF8', 'RPF1', 'RPF2', 'RPF3', 'RPF4', 'RPF5', 'RPF6', 'RPF7', 'RPF8', 'RSF1', 'RSF2', 'RSF3', 'RSF4', 'RSF5', 'RSF6', 'RSF7', 'RSF8', 'RAT1', 'RAT2', 'RAT3', 'RAT4', 'RAT5', 'RAT6', 'RBT1', 'RBT2', 'RBT3', 'RBT4', 'RPT1', 'RPT2', 'RPT3', 'RPT4', 'RPT5', 'RPT6', 'RPT7', 'RPT8', 'RTF1', 'RTF2', 'RTF3', 'RTF4', 'RTF5', 'RTF6', 'RTF7', 'RTF8'],
        'soz_channels': ['RAT1', 'RAT2'],
        'surgery_outcome': 'NR'
    },
    ('sub-jh103', '01'): {
        'channels': ['ABT1', 'ABT2', 'ABT3', 'ABT4', 'MBT1', 'MBT2', 'MBT3', 'MBT4', 'PBT3', 'PBT4', 'RAD1', 'RAD2', 'RAD3', 'RAD4', 'RAD5', 'RAD6', 'RAD7', 'PBT1', 'PBT2', 'RHD1', 'RHD2', 'RHD3', 'RHD4', 'RHD5', 'RHD6', 'RHD7', 'RHD8', 'RHD9', '$PBT1', '$PBT2', 'RTG1', 'RTG2', 'RTG3', 'RTG4', 'RTG5', 'RTG6', 'RTG7', 'RTG8', 'RTG9', 'RTG10', 'RTG11', 'RTG12', 'RTG13', 'RTG14', 'RTG15', 'RTG16', 'RTG17', 'RTG19', 'RTG20', 'RTG23', 'RTG24', 'RTG25', 'RTG27', 'RTG28', 'RTG29', 'RTG30', 'RTG31', 'RTG32', 'RTG33', 'RTG34', 'RTG35', 'RTG36', 'RTG37', 'RTG38', 'RTG39', 'RTG40', 'RTG41', 'RTG42', 'RTG43', 'RTG44', 'RTG45', 'RTG46', 'RTG47', 'RTG48', 'RTG49', 'RTG50', 'RTG51', 'RTG52', 'RTG53', 'RTG54', 'RTG55', 'RTG56', 'RTG57', 'RTG58', 'RTG59', 'RTG60', 'RTG61', 'RTG62', 'RTG63', 'RTG64'],
        'soz_channels': ['RTG40', 'RTG48', 'RAD1', 'RAD2', 'RAD3', 'RAD4', 'RAD5', 'RAD6', 'RAD7', 'RAD8', 
    'RHD1', 'RHD2', 'RHD3', 'RHD4', 'RHD5', 'RHD6', 'RHD7', 'RHD8', 'RHD9'],
        'surgery_outcome': 'F'
    },
    ('sub-jh103', '02'): {
        'channels': ['ABT1', 'ABT2', 'ABT3', 'ABT4', 'MBT1', 'MBT2', 'MBT3', 'MBT4', 'PBT3', 'PBT4', 'RAD1', 'RAD2', 'RAD3', 'RAD4', 'RAD5', 'RAD6', 'RAD7', 'PBT1', 'PBT2', 'RHD1', 'RHD2', 'RHD3', 'RHD4', 'RHD5', 'RHD6', 'RHD7', 'RHD8', 'RHD9', '$PBT1', '$PBT2', 'RTG1', 'RTG2', 'RTG3', 'RTG4', 'RTG5', 'RTG6', 'RTG7', 'RTG8', 'RTG9', 'RTG10', 'RTG11', 'RTG12', 'RTG13', 'RTG14', 'RTG15', 'RTG16', 'RTG17', 'RTG19', 'RTG20', 'RTG23', 'RTG24', 'RTG25', 'RTG27', 'RTG28', 'RTG29', 'RTG30', 'RTG31', 'RTG32', 'RTG33', 'RTG34', 'RTG35', 'RTG36', 'RTG37', 'RTG38', 'RTG39', 'RTG40', 'RTG41', 'RTG42', 'RTG43', 'RTG44', 'RTG45', 'RTG46', 'RTG47', 'RTG48', 'RTG49', 'RTG50', 'RTG51', 'RTG52', 'RTG53', 'RTG54', 'RTG55', 'RTG56', 'RTG57', 'RTG58', 'RTG59', 'RTG60', 'RTG61', 'RTG62', 'RTG63', 'RTG64'],
        'soz_channels': ['RTG40', 'RTG48', 'RAD1', 'RAD2', 'RAD3', 'RAD4', 'RAD5', 'RAD6', 'RAD7', 'RAD8', 
    'RHD1', 'RHD2', 'RHD3', 'RHD4', 'RHD5', 'RHD6', 'RHD7', 'RHD8', 'RHD9'],
        'surgery_outcome': 'F'
    },
    ('sub-jh103', '03'): {
        'channels': ['ABT1', 'ABT2', 'ABT3', 'ABT4', 'MBT1', 'MBT2', 'MBT3', 'MBT4', 'PBT3', 'PBT4', 'RAD1', 'RAD2', 'RAD3', 'RAD4', 'RAD5', 'RAD6', 'RAD7', 'PBT1', 'PBT2', 'RHD1', 'RHD2', 'RHD3', 'RHD4', 'RHD5', 'RHD6', 'RHD7', 'RHD8', 'RHD9', '$PBT1', '$PBT2', 'RTG1', 'RTG2', 'RTG3', 'RTG4', 'RTG5', 'RTG6', 'RTG7', 'RTG8', 'RTG9', 'RTG10', 'RTG11', 'RTG12', 'RTG13', 'RTG14', 'RTG15', 'RTG16', 'RTG17', 'RTG19', 'RTG20', 'RTG23', 'RTG24', 'RTG25', 'RTG27', 'RTG28', 'RTG29', 'RTG30', 'RTG31', 'RTG32', 'RTG33', 'RTG34', 'RTG35', 'RTG36', 'RTG37', 'RTG38', 'RTG39', 'RTG40', 'RTG41', 'RTG42', 'RTG43', 'RTG44', 'RTG45', 'RTG46', 'RTG47', 'RTG48', 'RTG49', 'RTG50', 'RTG51', 'RTG52', 'RTG53', 'RTG54', 'RTG55', 'RTG56', 'RTG57', 'RTG58', 'RTG59', 'RTG60', 'RTG61', 'RTG62', 'RTG63', 'RTG64'],
        'soz_channels': ['RTG40', 'RTG48', 'RAD1', 'RAD2', 'RAD3', 'RAD4', 'RAD5', 'RAD6', 'RAD7', 'RAD8', 
    'RHD1', 'RHD2', 'RHD3', 'RHD4', 'RHD5', 'RHD6', 'RHD7', 'RHD8', 'RHD9'],
        'surgery_outcome': 'F'
    },
    ('sub-jh104', '01'): {
        'channels': ['LAF1', 'LAF3', 'LAF5', 'LAF7', 'LAF4', 'LAF6', 'LAF8', 'LMF1', 'LMF2', 'LMF3', 'LMF6', 'LMF7', 'LMF8', 'LPF1', 'LPF2', 'LPF3', 'LPF4', 'LPF5', 'LPF6', 'LPF7', 'LPF8', 'LMF4', 'LMF5', 'LFP1', 'LFP2', 'LFP3', 'LFP4', 'LFP5', 'LFP6', 'LFP7', 'LFP8', 'LAD1', 'LAD2', 'LAD3', 'LAD4', 'LAD5', 'LAD6', 'LAD7', '$LMF4', '$LMF5', 'LAD8', 'LHD1', 'LHD2', 'LHD3', 'LHD4', 'LHD5', 'LHD6', 'LHD7', 'LHD8', 'LAT1', 'LAT2', 'LAT3', 'LAT4', 'ABT1', 'ABT2', 'ABT3', 'ABT4', 'MBT1', 'MBT2', 'MBT3', 'MBT4', 'MBT5', 'MBT6', 'PBT4', 'PBT5', 'PBT6', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8'],
        'soz_channels': ['LAT1', 'LAT2', 'MBT4', 'MBT5', 'MBT6', 'PBT4'],
        'surgery_outcome': 'NR'
    },
    ('sub-jh104', '02'): {
        'channels': ['LAF1', 'LAF3', 'LAF5', 'LAF7', 'LAF4', 'LAF6', 'LAF8', 'LMF1', 'LMF2', 'LMF3', 'LMF6', 'LMF7', 'LMF8', 'LPF1', 'LPF2', 'LPF3', 'LPF4', 'LPF5', 'LPF6', 'LPF7', 'LPF8', 'LMF4', 'LMF5', 'LFP1', 'LFP2', 'LFP3', 'LFP4', 'LFP5', 'LFP6', 'LFP7', 'LFP8', 'LAD1', 'LAD2', 'LAD3', 'LAD4', 'LAD5', 'LAD6', 'LAD7', '$LMF4', '$LMF5', 'LAD8', 'LHD1', 'LHD2', 'LHD3', 'LHD4', 'LHD5', 'LHD6', 'LHD7', 'LHD8', 'LAT1', 'LAT2', 'LAT3', 'LAT4', 'ABT1', 'ABT2', 'ABT3', 'ABT4', 'MBT1', 'MBT2', 'MBT3', 'MBT4', 'MBT5', 'MBT6', 'PBT4', 'PBT5', 'PBT6', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LPT7', 'LPT8'],
        'soz_channels': ['LAT1', 'LAT2', 'MBT4', 'MBT5', 'MBT6', 'PBT4'],
        'surgery_outcome': 'NR'
    },
    ('sub-jh105', '02'): {
        'channels': ['RFS1', 'RFS2', 'RFS3', 'RFS4', 'RFS5', 'RFS6', 'RPG1', 'RPG2', 'RPG5', 'RPG6', 'RPG8', 'RPG9', 'RPG10', 'RPG11', 'RPG12', 'RPG13', 'RPG14', 'RPG15', 'RPG3', 'RPG4', 'RPG16', 'RPG17', 'RPG18', 'RPG19', 'RPG20', 'RPG21', 'RPG22', 'RPG23', 'RPG24', 'RPG25', 'RPG26', 'RPG27', 'RPG28', 'RPG29', 'RPG30', '$RPG3', '$RPG4', 'RPG31', 'RPG32', 'RPG33', 'RPG34', 'RPG36', 'RPG37', 'RPG38', 'RPG40', 'RPG41', 'RPG42', 'RPG43', 'RPG44', 'RPG45', 'RPG46', 'RPG47', 'RPG48', 'PSI1', 'PSI2', 'PSI3', 'PSI4', 'PSI5', 'PSI6', 'PSI7', 'PSI8', 'PDI1', 'PDI2', 'PDI3', 'PDI4', 'ASI1', 'ASI2', 'ASI3', 'ASI4', 'ASI5', 'ASI6', 'APD1', 'APD2', 'APD3', 'APD4', 'APD5', 'APD6', 'APD7', 'APD8', 'PPD1', 'PPD2', 'PPD3', 'PPD4', 'PPD5', 'PPD6', 'PPD7', 'PPD8'],
        'soz_channels': ['RPG4', 'RPG5', 'RPG12', 'RPG13', 'RPG14', 'RPG20', 'RPG21', 
    'APD1', 'APD2', 'APD3', 'APD4', 'APD5', 'APD6', 'APD7', 'APD8', 
    'PPD1', 'PPD2', 'PPD3', 'PPD4', 'PPD5', 'PPD6', 'PPD7', 'PPD8', 
    'ASI3', 'PSI5', 'PSI6'],
        'surgery_outcome': 'S'
    },
    ('sub-jh105', '04'): {
        'channels': ['RFS1', 'RFS2', 'RFS3', 'RFS4', 'RFS5', 'RFS6', 'RPG1', 'RPG2', 'RPG5', 'RPG6', 'RPG8', 'RPG9', 'RPG10', 'RPG11', 'RPG12', 'RPG13', 'RPG14', 'RPG15', 'RPG3', 'RPG4', 'RPG16', 'RPG17', 'RPG18', 'RPG19', 'RPG20', 'RPG21', 'RPG22', 'RPG23', 'RPG24', 'RPG25', 'RPG26', 'RPG27', 'RPG28', 'RPG29', 'RPG30', '$RPG3', '$RPG4', 'RPG31', 'RPG32', 'RPG33', 'RPG34', 'RPG36', 'RPG37', 'RPG38', 'RPG40', 'RPG41', 'RPG42', 'RPG43', 'RPG44', 'RPG45', 'RPG46', 'RPG47', 'RPG48', 'PSI1', 'PSI2', 'PSI3', 'PSI4', 'PSI5', 'PSI6', 'PSI7', 'PSI8', 'PDI1', 'PDI2', 'PDI3', 'PDI4', 'ASI1', 'ASI2', 'ASI3', 'ASI4', 'ASI5', 'ASI6', 'APD1', 'APD2', 'APD3', 'APD4', 'APD5', 'APD6', 'APD7', 'APD8', 'PPD1', 'PPD2', 'PPD3', 'PPD4', 'PPD5', 'PPD6', 'PPD7', 'PPD8'],
        'soz_channels': ['RPG4', 'RPG5', 'RPG12', 'RPG13', 'RPG14', 'RPG20', 'RPG21', 
    'APD1', 'APD2', 'APD3', 'APD4', 'APD5', 'APD6', 'APD7', 'APD8', 
    'PPD1', 'PPD2', 'PPD3', 'PPD4', 'PPD5', 'PPD6', 'PPD7', 'PPD8', 
    'ASI3', 'PSI5', 'PSI6'],
        'surgery_outcome': 'S'
    },
    ('sub-jh108', '01'): {
        'channels': ['RSI1', 'RSI2', 'RSI3', 'RSI4', 'RSI5', 'RSI6', 'RSI7', 'RSI8', 'RDI3', 'RDI4', 'RDI5', 'RDI6', 'RDI7', 'RDI8', 'RAF1', 'RAF2', 'RAF3', 'RAF4', 'RAF5', 'RDI1', 'RDI2', 'RAF6', 'RAF7', 'RAF8', 'RIF1', 'RIF2', 'RIF3', 'RIF4', 'RIF5', 'RIF6', 'RPP1', 'RPP2', 'RPP3', 'RPP4', 'RPP5', 'RPP6', '$RDI1', '$RDI2', 'RPP7', 'RPP8', 'RIP1', 'RIP2', 'RIP3', 'RIP4', 'RIP5', 'RIP6', 'RIP7', 'RIP8', 'RAT1', 'RAT2', 'RAT3', 'RAT4', 'RAT5', 'RAT6', 'RST1', 'RST2', 'RST3', 'RST4', 'RST5', 'RST6', 'RST7', 'RST8', 'RBT1', 'RBT2', 'RBT3', 'RBT4', 'RPT1', 'RPT2', 'RPT3', 'RPT4', 'RPT5', 'RPT6', 'LSI1', 'LSI2', 'LSI3', 'LSI4', 'LSI5', 'LSI6', 'LSI7', 'LSI8', 'LDI1', 'LDI2', 'LDI3', 'LDI4', 'LDI5', 'LDI6', 'LDI7', 'LDI8', 'LAF1', 'LAF2', 'LAF3', 'LAF4', 'LAF5', 'LAF6', 'LIF1', 'LIF2', 'LIF3', 'LIF4', 'LIF5', 'LIF6', 'LPP1', 'LPP2', 'LPP3', 'LPP4', 'LPP5', 'LPP6', 'LPP7', 'LPP8', 'LIP1', 'LIP2', 'LIP3', 'LIP4', 'LIP5', 'LIP6', 'LIP7', 'LIP8', 'LAT1', 'LAT2', 'LAT3', 'LAT4', 'LAT5', 'LAT6', 'LST1', 'LST2', 'LST3', 'LST4', 'LST5', 'LST6', 'LST7', 'LST8', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LBT1', 'LBT2', 'LBT3', 'LBT4'],
        'soz_channels': ['RDI1', 'RDI2', 'RDI3', 'RDI4', 
    'RSI1', 'RSI2', 'RSI3', 'RSI4'],
        'surgery_outcome': 'F'
    },
    ('sub-pt01', '01'): {
        'channels': ['G1', 'G2', 'G3', 'G4', 'G7', 'G8', 'G9', 'G10', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G11', 'G12', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'ATT1', 'ATT2', 'ATT3', 'ATT4', 'ATT5', 'ATT6', '$G11', '$G12', 'ATT7', 'ATT8', 'PLT1', 'PLT2', 'PLT3', 'PLT4', 'PLT5', 'PLT6', 'AST1', 'AST2', 'AST3', 'AST4', 'PST1', 'PST2', 'PST3', 'PST4', 'AD1', 'AD2', 'AD3', 'AD4', 'PD1', 'PD2', 'PD3', 'PD4', 'SF1', 'SF2', 'SF3', 'SF4', 'SF5', 'SF6', 'IF1', 'IF2', 'IF3', 'IF4', 'IF5', 'IF6', 'ILT1', 'ILT2', 'ILT3', 'ILT4', 'MLT1', 'MLT2', 'MLT3', 'MLT4', 'SLT1', 'SLT2', 'SLT3', 'SLT4'],
        'soz_channels': ['PD1', 'PD2', 'PD3', 'PD4', 
    'AD1', 'AD2', 'AD3', 'AD4', 
    'ATT1', 'ATT2'],
        'surgery_outcome': 'S'
    },
    ('sub-pt01', '02'): {
        'channels': ['G1', 'G2', 'G3', 'G4', 'G7', 'G8', 'G9', 'G10', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G11', 'G12', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'ATT1', 'ATT2', 'ATT3', 'ATT4', 'ATT5', 'ATT6', '$G11', '$G12', 'ATT7', 'ATT8', 'PLT1', 'PLT2', 'PLT3', 'PLT4', 'PLT5', 'PLT6', 'AST1', 'AST2', 'AST3', 'AST4', 'PST1', 'PST2', 'PST3', 'PST4', 'AD1', 'AD2', 'AD3', 'AD4', 'PD1', 'PD2', 'PD3', 'PD4', 'SF1', 'SF2', 'SF3', 'SF4', 'SF5', 'SF6', 'IF1', 'IF2', 'IF3', 'IF4', 'IF5', 'IF6', 'ILT1', 'ILT2', 'ILT3', 'ILT4', 'MLT1', 'MLT2', 'MLT3', 'MLT4', 'SLT1', 'SLT2', 'SLT3', 'SLT4'],
        'soz_channels': ['PD1', 'PD2', 'PD3', 'PD4', 
    'AD1', 'AD2', 'AD3', 'AD4', 
    'ATT1', 'ATT2'],
        'surgery_outcome': 'S'
    },
    ('sub-pt01', '03'): {
        'channels': ['G1', 'G2', 'G3', 'G4', 'G7', 'G8', 'G9', 'G10', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G11', 'G12', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'ATT1', 'ATT2', 'ATT3', 'ATT4', 'ATT5', 'ATT6', '$G11', '$G12', 'ATT7', 'ATT8', 'PLT1', 'PLT2', 'PLT3', 'PLT4', 'PLT5', 'PLT6', 'AST1', 'AST2', 'AST3', 'AST4', 'PST1', 'PST2', 'PST3', 'PST4', 'AD1', 'AD2', 'AD3', 'AD4', 'PD1', 'PD2', 'PD3', 'PD4', 'SF1', 'SF2', 'SF3', 'SF4', 'SF5', 'SF6', 'IF1', 'IF2', 'IF3', 'IF4', 'IF5', 'IF6', 'ILT1', 'ILT2', 'ILT3', 'ILT4', 'MLT1', 'MLT2', 'MLT3', 'MLT4', 'SLT1', 'SLT2', 'SLT3', 'SLT4'],
        'soz_channels': ['PD1', 'PD2', 'PD3', 'PD4', 
    'AD1', 'AD2', 'AD3', 'AD4', 
    'ATT1', 'ATT2'],
        'surgery_outcome': 'S'
    },
    ('sub-pt01', '04'): {
        'channels': ['G1', 'G2', 'G3', 'G4', 'G7', 'G8', 'G9', 'G10', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G11', 'G12', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'ATT1', 'ATT2', 'ATT3', 'ATT4', 'ATT5', 'ATT6', '$G11', '$G12', 'ATT7', 'ATT8', 'PLT1', 'PLT2', 'PLT3', 'PLT4', 'PLT5', 'PLT6', 'AST1', 'AST2', 'AST3', 'AST4', 'PST1', 'PST2', 'PST3', 'PST4', 'AD1', 'AD2', 'AD3', 'AD4', 'PD1', 'PD2', 'PD3', 'PD4', 'SF1', 'SF2', 'SF3', 'SF4', 'SF5', 'SF6', 'IF1', 'IF2', 'IF3', 'IF4', 'IF5', 'IF6', 'ILT1', 'ILT2', 'ILT3', 'ILT4', 'MLT1', 'MLT2', 'MLT3', 'MLT4', 'SLT1', 'SLT2', 'SLT3', 'SLT4'],
        'soz_channels': ['PD1', 'PD2', 'PD3', 'PD4', 
    'AD1', 'AD2', 'AD3', 'AD4', 
    'ATT1', 'ATT2'],
        'surgery_outcome': 'S'
    },
    ('sub-pt2', '01'): {
        'channels': ['G1', 'G2', 'G3', 'G4', 'G7', 'G8', 'G9', 'G10', 'G13', 'G14', 'G15', 'G16', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G11', 'G12', 'G24', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6', '$G11', '$G12', 'AST3', 'AST4', 'MST1', 'MST2', 'MST3', 'MST4', 'PST1', 'PST2', 'PST3', 'PST4', 'OF1', 'OF2', 'OF3', 'OF4', 'LF1', 'LF2', 'LF3', 'LF4', 'LF5', 'LF6', 'AST1', 'AST2', 'LP1', 'LP2', 'LP3', 'LP4', 'LP5', 'LP6'],
        'soz_channels': ['PST1', 'PST2', 'PST3', 'PST4', 
    'AST1', 'AST2', 
    'MST1', 'MST2'],
        'surgery_outcome': 'S'
    },
    ('sub-pt2', '02'): {
        'channels': ['G1', 'G2', 'G3', 'G4', 'G7', 'G8', 'G9', 'G10', 'G13', 'G14', 'G15', 'G16', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G11', 'G12', 'G24', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6', '$G11', '$G12', 'AST3', 'AST4', 'MST1', 'MST2', 'MST3', 'MST4', 'PST1', 'PST2', 'PST3', 'PST4', 'OF1', 'OF2', 'OF3', 'OF4', 'LF1', 'LF2', 'LF3', 'LF4', 'LF5', 'LF6', 'AST1', 'AST2', 'LP1', 'LP2', 'LP3', 'LP4', 'LP5', 'LP6'],
        'soz_channels': ['PST1', 'PST2', 'PST3', 'PST4', 
    'AST1', 'AST2', 
    'MST1', 'MST2'],
        'surgery_outcome': 'S'
    },
    ('sub-pt2', '03'): {
        'channels': ['G1', 'G2', 'G3', 'G4', 'G7', 'G8', 'G9', 'G10', 'G13', 'G14', 'G15', 'G16', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G11', 'G12', 'G24', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6', '$G11', '$G12', 'AST3', 'AST4', 'MST1', 'MST2', 'MST3', 'MST4', 'PST1', 'PST2', 'PST3', 'PST4', 'OF1', 'OF2', 'OF3', 'OF4', 'LF1', 'LF2', 'LF3', 'LF4', 'LF5', 'LF6', 'AST1', 'AST2', 'LP1', 'LP2', 'LP3', 'LP4', 'LP5', 'LP6'],
        'soz_channels': ['PST1', 'PST2', 'PST3', 'PST4', 
    'AST1', 'AST2', 
    'MST1', 'MST2'],
        'surgery_outcome': 'S'
    },
    ('sub-pt3', '01'): {
        'channels': ['TG3', 'TG4', 'TG5', 'TG6', 'TG11', 'TG13', 'TG18', 'TG19', 'TG20', 'TG22', 'TG27', 'TG28', 'TG29', 'TG30', 'TG31', 'TG32', 'TT1', 'TT2', 'TT3', 'TT4', 'AST1', 'TG24', 'TG26', 'AST2', 'AST3', 'AST4', 'MST1', 'MST2', 'MST3', 'MST4', 'PST1', 'PST2', 'PST3', 'PST4', 'OF1', 'OF2', 'OF3', 'OF4', '$TG24', '$TG26', 'IFP1', 'IFP2', 'IFP3', 'IFP4', 'MFP1', 'MFP2', 'MFP3', 'MFP4', 'MFP5', 'SFP1', 'SFP2', 'SFP3', 'SFP4', 'SFP5', 'SFP6', 'SFP7', 'SFP8', 'IH1', 'IH2', 'IH3', 'IH4', 'IH5', 'IH6', 'FG1', 'FG2', 'FG3', 'FG4', 'FG5', 'FG6', 'FG7', 'FG8', 'FG9', 'FG10', 'FG11', 'FG12', 'FG13', 'FG14', 'FG15', 'FG16', 'FG17', 'FG18', 'FG19', 'FG20', 'FG21', 'FG22', 'FG23', 'FG24', 'FG25', 'FG26', 'FG27', 'FG28', 'FG29', 'FG30', 'FG31', 'FG32', 'ILF1', 'ILF3', 'ILF5', 'ILF7'],
        'soz_channels': ['OF1', 'OF2', 'OF3', 'OF4', 
    'MFP2', 'MFP3', 
    'IFP1', 'IFP2', 'IFP3', 
    'SFP1', 'SFP2', 'SFP3', 
    'FG1', 'FG2', 'FG3', 'FG4', 'FG5', 'FG6', 'FG7', 'FG8', 
    'FG9', 'FG10', 'FG11', 'FG12', 'FG13', 'FG14', 'FG15', 
    'FG16', 'FG17', 'FG18', 'FG19', 'FG20', 'FG21', 'FG22', 
    'FG23', 'FG24', 'FG25'],
        'surgery_outcome': 'S'
    },
    ('sub-pt3', '02'): {
        'channels': ['TG3', 'TG4', 'TG5', 'TG6', 'TG11', 'TG13', 'TG18', 'TG19', 'TG20', 'TG22', 'TG27', 'TG28', 'TG29', 'TG30', 'TG31', 'TG32', 'TT1', 'TT2', 'TT3', 'TT4', 'AST1', 'TG24', 'TG26', 'AST2', 'AST3', 'AST4', 'MST1', 'MST2', 'MST3', 'MST4', 'PST1', 'PST2', 'PST3', 'PST4', 'OF1', 'OF2', 'OF3', 'OF4', '$TG24', '$TG26', 'IFP1', 'IFP2', 'IFP3', 'IFP4', 'MFP1', 'MFP2', 'MFP3', 'MFP4', 'MFP5', 'SFP1', 'SFP2', 'SFP3', 'SFP4', 'SFP5', 'SFP6', 'SFP7', 'SFP8', 'IH1', 'IH2', 'IH3', 'IH4', 'IH5', 'IH6', 'FG1', 'FG2', 'FG3', 'FG4', 'FG5', 'FG6', 'FG7', 'FG8', 'FG9', 'FG10', 'FG11', 'FG12', 'FG13', 'FG14', 'FG15', 'FG16', 'FG17', 'FG18', 'FG19', 'FG20', 'FG21', 'FG22', 'FG23', 'FG24', 'FG25', 'FG26', 'FG27', 'FG28', 'FG29', 'FG30', 'FG31', 'FG32', 'ILF1', 'ILF3', 'ILF5', 'ILF7'],
        'soz_channels': ['OF1', 'OF2', 'OF3', 'OF4', 
    'MFP2', 'MFP3', 
    'IFP1', 'IFP2', 'IFP3', 
    'SFP1', 'SFP2', 'SFP3', 
    'FG1', 'FG2', 'FG3', 'FG4', 'FG5', 'FG6', 'FG7', 'FG8', 
    'FG9', 'FG10', 'FG11', 'FG12', 'FG13', 'FG14', 'FG15', 
    'FG16', 'FG17', 'FG18', 'FG19', 'FG20', 'FG21', 'FG22', 
    'FG23', 'FG24', 'FG25'],
        'surgery_outcome': 'S'
    },
    ('sub-pt6', '01'): {
        'channels': ['RFT1', 'RFT2', 'RFT3', 'RFT4', 'RFT5', 'RFT6', 'RALT1', 'RALT2', 'RALT3', 'RALT4', 'RAST1', 'RAST2', 'RAST3', 'RAST4', 'RPST1', 'RPST2', 'RPST3', 'RPST4', 'RPLT1', 'RPLT2', 'RPLT3', 'RALT5', 'RALT6', 'RPLT4', 'RPLT5', 'RPLT6', 'RAH1', 'RAH2', 'RAH3', 'RAH4', 'RPH1', 'RPH2', 'RPH3', 'RPH4', 'RA1', 'RA2', 'RA3', 'RA4', '$RALT5', '$RALT6', 'LFT1', 'LFT2', 'LFT3', 'LFT4', 'LFT5', 'LFT6', 'LALT1', 'LALT2', 'LALT3', 'LALT4', 'LALT5', 'LALT6', 'LAST1', 'LAST2', 'LAST3', 'LAST4', 'LPST1', 'LPST2', 'LPST3', 'LPST4', 'LPLT2', 'LPLT3', 'LPLT4', 'LPLT5', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LAH1', 'LAH2', 'LAH3', 'LAH4', 'LPH1', 'LPH2', 'LPH3', 'LPH4', 'LA1', 'LA2', 'LA3', 'LA4'],
        'soz_channels': ['LA1', 'LA2', 'LA3', 'LA4',
    'LAH1', 'LAH2', 'LAH3', 'LAH4',
    'LPH1', 'LPH2', 'LPH3', 'LPH4'],
        'surgery_outcome': 'F'
    },
    ('sub-pt6', '02'): {
        'channels': ['RFT1', 'RFT2', 'RFT3', 'RFT4', 'RFT5', 'RFT6', 'RALT1', 'RALT2', 'RALT3', 'RALT4', 'RAST1', 'RAST2', 'RAST3', 'RAST4', 'RPST1', 'RPST2', 'RPST3', 'RPST4', 'RPLT1', 'RPLT2', 'RPLT3', 'RALT5', 'RALT6', 'RPLT4', 'RPLT5', 'RPLT6', 'RAH1', 'RAH2', 'RAH3', 'RAH4', 'RPH1', 'RPH2', 'RPH3', 'RPH4', 'RA1', 'RA2', 'RA3', 'RA4', '$RALT5', '$RALT6', 'LFT1', 'LFT2', 'LFT3', 'LFT4', 'LFT5', 'LFT6', 'LALT1', 'LALT2', 'LALT3', 'LALT4', 'LALT5', 'LALT6', 'LAST1', 'LAST2', 'LAST3', 'LAST4', 'LPST1', 'LPST2', 'LPST3', 'LPST4', 'LPLT2', 'LPLT3', 'LPLT4', 'LPLT5', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LAH1', 'LAH2', 'LAH3', 'LAH4', 'LPH1', 'LPH2', 'LPH3', 'LPH4', 'LA1', 'LA2', 'LA3', 'LA4'],
        'soz_channels': ['LA1', 'LA2', 'LA3', 'LA4',
    'LAH1', 'LAH2', 'LAH3', 'LAH4',
    'LPH1', 'LPH2', 'LPH3', 'LPH4'],
        'surgery_outcome': 'F'
    },
    ('sub-pt6', '03'): {
        'channels': ['RFT1', 'RFT2', 'RFT3', 'RFT4', 'RFT5', 'RFT6', 'RALT1', 'RALT2', 'RALT3', 'RALT4', 'RAST1', 'RAST2', 'RAST3', 'RAST4', 'RPST1', 'RPST2', 'RPST3', 'RPST4', 'RPLT1', 'RPLT2', 'RPLT3', 'RALT5', 'RALT6', 'RPLT4', 'RPLT5', 'RPLT6', 'RAH1', 'RAH2', 'RAH3', 'RAH4', 'RPH1', 'RPH2', 'RPH3', 'RPH4', 'RA1', 'RA2', 'RA3', 'RA4', '$RALT5', '$RALT6', 'LFT1', 'LFT2', 'LFT3', 'LFT4', 'LFT5', 'LFT6', 'LALT1', 'LALT2', 'LALT3', 'LALT4', 'LALT5', 'LALT6', 'LAST1', 'LAST2', 'LAST3', 'LAST4', 'LPST1', 'LPST2', 'LPST3', 'LPST4', 'LPLT2', 'LPLT3', 'LPLT4', 'LPLT5', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'LAH1', 'LAH2', 'LAH3', 'LAH4', 'LPH1', 'LPH2', 'LPH3', 'LPH4', 'LA1', 'LA2', 'LA3', 'LA4'],
        'soz_channels': ['LA1', 'LA2', 'LA3', 'LA4',
    'LAH1', 'LAH2', 'LAH3', 'LAH4',
    'LPH1', 'LPH2', 'LPH3', 'LPH4'],
        'surgery_outcome': 'F'
    },
    ('sub-pt7', '01'): {
        'channels': ['MFP1', 'MFP2', 'MFP3', 'MFP4', 'LFP1', 'LFP2', 'LFP5', 'LSF1', 'LSF2', 'LSF3', 'LSF4', 'LSF5', 'LSF6', 'MT1', 'LFP3', 'LFP4', 'MT2', 'MT3', 'MT4', 'MT5', 'MT6', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', '$LFP3', '$LFP4', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'G37', 'G38', 'G39', 'G40', 'G41', 'G42', 'G43', 'G44', 'G45', 'G46', 'G47', 'G48', 'G51', 'G52', 'G53', 'G54', 'G55', 'G56', 'G60', 'G61', 'G62', 'G63', 'G64', 'PF1', 'PF2', 'PF3', 'PF4', 'PF5', 'PF6', 'AT1', 'AT2', 'AT3', 'AT4', 'AT5', 'AT6', 'PT1', 'PT2', 'PT3', 'PT4', 'PT5', 'PT6'],
        'soz_channels': ['LFP3', 'MFP1', 'PT2', 'PT3', 'PT4', 'PT5', 
    'MT2', 'MT3', 'AT3', 'AT4', 
    'G29', 'G30', 'G39', 'G40', 'G45', 'G46'],
        'surgery_outcome': 'F'
    },
    ('sub-pt7', '02'): {
        'channels': ['MFP1', 'MFP2', 'MFP3', 'MFP4', 'LFP1', 'LFP2', 'LFP5', 'LSF1', 'LSF2', 'LSF3', 'LSF4', 'LSF5', 'LSF6', 'MT1', 'LFP3', 'LFP4', 'MT2', 'MT3', 'MT4', 'MT5', 'MT6', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', '$LFP3', '$LFP4', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'G37', 'G38', 'G39', 'G40', 'G41', 'G42', 'G43', 'G44', 'G45', 'G46', 'G47', 'G48', 'G51', 'G52', 'G53', 'G54', 'G55', 'G56', 'G60', 'G61', 'G62', 'G63', 'G64', 'PF1', 'PF2', 'PF3', 'PF4', 'PF5', 'PF6', 'AT1', 'AT2', 'AT3', 'AT4', 'AT5', 'AT6', 'PT1', 'PT2', 'PT3', 'PT4', 'PT5', 'PT6'],
        'soz_channels': ['LFP3', 'MFP1', 'PT2', 'PT3', 'PT4', 'PT5', 
    'MT2', 'MT3', 'AT3', 'AT4', 
    'G29', 'G30', 'G39', 'G40', 'G45', 'G46'],
        'surgery_outcome': 'F'
    },
    ('sub-pt7', '03'): {
        'channels': ['MFP1', 'MFP2', 'MFP3', 'MFP4', 'LFP1', 'LFP2', 'LFP5', 'LSF1', 'LSF2', 'LSF3', 'LSF4', 'LSF5', 'LSF6', 'MT1', 'LFP3', 'LFP4', 'MT2', 'MT3', 'MT4', 'MT5', 'MT6', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', '$LFP3', '$LFP4', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'G37', 'G38', 'G39', 'G40', 'G41', 'G42', 'G43', 'G44', 'G45', 'G46', 'G47', 'G48', 'G51', 'G52', 'G53', 'G54', 'G55', 'G56', 'G60', 'G61', 'G62', 'G63', 'G64', 'PF1', 'PF2', 'PF3', 'PF4', 'PF5', 'PF6', 'AT1', 'AT2', 'AT3', 'AT4', 'AT5', 'AT6', 'PT1', 'PT2', 'PT3', 'PT4', 'PT5', 'PT6'],
        'soz_channels': ['LFP3', 'MFP1', 'PT2', 'PT3', 'PT4', 'PT5', 
    'MT2', 'MT3', 'AT3', 'AT4', 
    'G29', 'G30', 'G39', 'G40', 'G45', 'G46'],
        'surgery_outcome': 'F'
    },
    ('sub-pt8', '01'): {
        'channels': ['TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6', 'AST1', 'AST2', 'AST3', 'AST4', 'MST3', 'MST4', 'PST1', 'PST2', 'PST3', 'PST4', 'PPST1', 'PPST2', 'PPST3', 'PPST4', 'MST1', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'G17', 'G18', '$MST1', '$MST2', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'TO6', 'TO5', 'TO4', 'TO3', 'TO2', 'TO1'],
        'soz_channels': ['MST3', 'MST4', 'TO6', 'TO5', 
    'G22', 'G23', 'G29', 'G30', 'G31', 
    'G19', 'G20', 'G21', 'G28', 
    'PO8', 'PO9', 'PO10'],
        'surgery_outcome': 'S'
    },
    ('sub-pt8', '02'): {
        'channels': ['TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6', 'AST1', 'AST2', 'AST3', 'AST4', 'MST3', 'MST4', 'PST1', 'PST2', 'PST3', 'PST4', 'PPST1', 'PPST2', 'PPST3', 'PPST4', 'MST1', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'G17', 'G18', '$MST1', '$MST2', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'TO6', 'TO5', 'TO4', 'TO3', 'TO2', 'TO1'],
        'soz_channels': ['MST3', 'MST4', 'TO6', 'TO5', 
    'G22', 'G23', 'G29', 'G30', 'G31', 
    'G19', 'G20', 'G21', 'G28', 
    'PO8', 'PO9', 'PO10'],
        'surgery_outcome': 'S'
    },
    ('sub-pt8', '03'): {
        'channels': ['TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6', 'AST1', 'AST2', 'AST3', 'AST4', 'MST3', 'MST4', 'PST1', 'PST2', 'PST3', 'PST4', 'PPST1', 'PPST2', 'PPST3', 'PPST4', 'MST1', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'G17', 'G18', '$MST1', '$MST2', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'TO6', 'TO5', 'TO4', 'TO3', 'TO2', 'TO1'],
        'soz_channels': ['MST3', 'MST4', 'TO6', 'TO5', 
    'G22', 'G23', 'G29', 'G30', 'G31', 
    'G19', 'G20', 'G21', 'G28', 
    'PO8', 'PO9', 'PO10'],
        'surgery_outcome': 'S'
    },
    ('sub-pt10', '01'): {
        'channels': ['OF1', 'OF2', 'OF3', 'TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6', 'AST3', 'AST4', 'MST1', 'MST2', 'MST3', 'MST4', 'PST1', 'PST2', 'PST3', 'PST4', 'FP35', 'AST1', 'AST2', 'FP36', 'FP37', 'FP38', 'FP39', 'FP40', 'FP43', 'FP44', 'FP45', 'FP46', 'FP47', 'FP48', '$AST1', '$AST2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G20', 'G21', 'G22', 'G23', 'G24', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6',
    'AST1', 'AST2', 'MST1', 'MST2'],
        'surgery_outcome': 'F'
    },
    ('sub-pt10', '02'): {
        'channels': ['OF1', 'OF2', 'OF3', 'TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6', 'AST3', 'AST4', 'MST1', 'MST2', 'MST3', 'MST4', 'PST1', 'PST2', 'PST3', 'PST4', 'FP35', 'AST1', 'AST2', 'FP36', 'FP37', 'FP38', 'FP39', 'FP40', 'FP43', 'FP44', 'FP45', 'FP46', 'FP47', 'FP48', '$AST1', '$AST2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G20', 'G21', 'G22', 'G23', 'G24', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6',
    'AST1', 'AST2', 'MST1', 'MST2'],
        'surgery_outcome': 'F'
    },
    ('sub-pt10', '03'): {
        'channels': ['OF1', 'OF2', 'OF3', 'TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6', 'AST3', 'AST4', 'MST1', 'MST2', 'MST3', 'MST4', 'PST1', 'PST2', 'PST3', 'PST4', 'FP35', 'AST1', 'AST2', 'FP36', 'FP37', 'FP38', 'FP39', 'FP40', 'FP43', 'FP44', 'FP45', 'FP46', 'FP47', 'FP48', '$AST1', '$AST2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G20', 'G21', 'G22', 'G23', 'G24', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6',
    'AST1', 'AST2', 'MST1', 'MST2'],
        'surgery_outcome': 'F'
    },
    ('sub-pt11', '01'): {
        'channels': ['RAM4', 'RAM5', 'RAM6', 'RAM7', 'RAL5', 'RAL6', 'RAL7', 'RG3', 'RG4', 'RG5', 'RG6', 'RG7', 'RG8', 'RG9', 'RG10', 'RG11', 'RG12', 'RG13', 'RG1', 'RG2', 'RG14', 'RG15', 'RG16', 'RG17', 'RG18', 'RG19', 'RG20', 'RG21', 'RG22', 'RG23', 'RG24', 'RG26', 'RG27', 'RG28', '$RG1', '$RG2', 'RG29', 'RG30', 'RG31', 'RG32', 'RG33', 'RG34', 'RG35', 'RG36', 'RG37', 'RG38', 'RG39', 'RG40', 'RG41', 'RG42', 'RG43', 'RG44', 'RG45', 'RG46', 'RG47', 'RG48', 'RPG12', 'RPG11', 'RPG10', 'RPG9', 'RGP8', 'RPG7', 'RPG6', 'RPG5', 'RPG4', 'RPG3', 'RPG2', 'RPG1', 'LG1', 'LG2', 'LG3', 'LG4', 'LG5', 'LG6', 'LG7', 'LG8', 'LG9', 'LG10', 'LG11', 'LG12'],
        'soz_channels': ['RG24', 'RG39', 'RG40', 'RG22', 'RG23', 'RG24', 'RG31', 
    'RG39', 'RG40', 'RG48', 'RG2', 'RG3', 'RG4', 'RG5', 
    'RG6', 'RG7', 'RG8'],
        'surgery_outcome': 'S'
    },
    ('sub-pt11', '02'): {
        'channels': ['RAM4', 'RAM5', 'RAM6', 'RAM7', 'RAL5', 'RAL6', 'RAL7', 'RG3', 'RG4', 'RG5', 'RG6', 'RG7', 'RG8', 'RG9', 'RG10', 'RG11', 'RG12', 'RG13', 'RG1', 'RG2', 'RG14', 'RG15', 'RG16', 'RG17', 'RG18', 'RG19', 'RG20', 'RG21', 'RG22', 'RG23', 'RG24', 'RG26', 'RG27', 'RG28', '$RG1', '$RG2', 'RG29', 'RG30', 'RG31', 'RG32', 'RG33', 'RG34', 'RG35', 'RG36', 'RG37', 'RG38', 'RG39', 'RG40', 'RG41', 'RG42', 'RG43', 'RG44', 'RG45', 'RG46', 'RG47', 'RG48', 'RPG12', 'RPG11', 'RPG10', 'RPG9', 'RGP8', 'RPG7', 'RPG6', 'RPG5', 'RPG4', 'RPG3', 'RPG2', 'RPG1', 'LG1', 'LG2', 'LG3', 'LG4', 'LG5', 'LG6', 'LG7', 'LG8', 'LG9', 'LG10', 'LG11', 'LG12'],
        'soz_channels': ['RG24', 'RG39', 'RG40', 'RG22', 'RG23', 'RG24', 'RG31', 
    'RG39', 'RG40', 'RG48', 'RG2', 'RG3', 'RG4', 'RG5', 
    'RG6', 'RG7', 'RG8'],
        'surgery_outcome': 'S'
    },
    ('sub-pt11', '03'): {
        'channels': ['RG1', 'RG2', 'RG3', 'RG4', 'RG5', 'RG6', 'RG7', 'RG8', 'RG9', 'RG10', 'RG13', 'RG14', 'RG15', 'RG16', 'RG17', 'RG18', 'RG19', 'RG20', 'RG21', 'RG22', 'RG23', 'RG11', 'RG12', 'RG24', 'RG26', 'RG27', 'R28', 'R29', 'R30', 'RG31', 'R32', 'RG33', 'RG34', 'RG35', 'RG36', 'RG37', 'RG38', '$RG11', '$RG12', 'RG39', 'RG40', 'RG41', 'RG42', 'RG43', 'RG44', 'RG45', 'RG46', 'R47', 'RG48', 'RLG10', 'RLG9', 'RLG8', 'RLG7', 'RLG6', 'RLG5', 'RLG4', 'RLG3', 'RLG22', 'RLG11', 'RAM1', 'RAM2', 'RAM3', 'RAM4', 'RAM5', 'RAM6', 'RAM7', 'RAL1', 'RAL2', 'RAL3', 'RAL5', 'RAL6', 'RAL7'],
        'soz_channels': ['RG24', 'RG39', 'RG40', 'RG22', 'RG23', 'RG24', 'RG31', 
    'RG39', 'RG40', 'RG48', 'RG2', 'RG3', 'RG4', 'RG5', 
    'RG6', 'RG7', 'RG8'],
        'surgery_outcome': 'S'
    },
    ('sub-pt11', '04'): {
        'channels': ['RG1', 'RG2', 'RG3', 'RG4', 'RG5', 'RG6', 'RG7', 'RG8', 'RG9', 'RG10', 'RG13', 'RG14', 'RG15', 'RG16', 'RG17', 'RG18', 'RG19', 'RG20', 'RG21', 'RG22', 'RG23', 'RG11', 'RG12', 'RG24', 'RG26', 'RG27', 'R28', 'R29', 'R30', 'RG31', 'R32', 'RG33', 'RG34', 'RG35', 'RG36', 'RG37', 'RG38', '$RG11', '$RG12', 'RG39', 'RG40', 'RG41', 'RG42', 'RG43', 'RG44', 'RG45', 'RG46', 'R47', 'RG48', 'RLG10', 'RLG9', 'RLG8', 'RLG7', 'RLG6', 'RLG5', 'RLG4', 'RLG3', 'RLG22', 'RLG11', 'RAM1', 'RAM2', 'RAM3', 'RAM4', 'RAM5', 'RAM6', 'RAM7', 'RAL1', 'RAL2', 'RAL3', 'RAL5', 'RAL6', 'RAL7'],
        'soz_channels': ['RG24', 'RG39', 'RG40', 'RG22', 'RG23', 'RG24', 'RG31', 
    'RG39', 'RG40', 'RG48', 'RG2', 'RG3', 'RG4', 'RG5', 
    'RG6', 'RG7', 'RG8'],
        'surgery_outcome': 'S'
    },
    ('sub-pt12', '01'): {
        'channels': ['OF1', 'OF2', 'OF3', 'OF4', 'TT1', 'TT2', 'TT5', 'TT6', 'AST1', 'AST2', 'AST3', 'AST4', 'MST1', 'MST2', 'MST3', 'MST4', 'PST1', 'TT3', 'TT4', 'PST2', 'PST3', 'PST4', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', '$TT3', '$TT4', 'G13', 'G14', 'G15', 'G16', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'TO1', 'TO2', 'TO3', 'TO4'],
        'soz_channels': ['TT1', 'TT2', 'TT3', 'TT4', 'TT5', 
    'AST1', 'AST2', 'MST1', 'MST2'],
        'surgery_outcome': 'F'
    },
    ('sub-pt12', '02'): {
        'channels': ['OF1', 'OF2', 'OF3', 'OF4', 'TT1', 'TT2', 'TT5', 'TT6', 'AST1', 'AST2', 'AST3', 'AST4', 'MST1', 'MST2', 'MST3', 'MST4', 'PST1', 'TT3', 'TT4', 'PST2', 'PST3', 'PST4', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', '$TT3', '$TT4', 'G13', 'G14', 'G15', 'G16', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'TO1', 'TO2', 'TO3', 'TO4'],
        'soz_channels': ['TT1', 'TT2', 'TT3', 'TT4', 'TT5', 
    'AST1', 'AST2', 'MST1', 'MST2'],
        'surgery_outcome': 'F'
    },
    ('sub-pt13', '01'): {
        'channels': ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G11', 'G12', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'G33', 'G34', 'G35', 'G36', 'G37', 'G38', '$G11', '$G12', 'G39', 'G40', 'G41', 'G42', 'G43', 'G44', 'G45', 'G46', 'G47', 'G48', 'G49', 'G50', 'G51', 'G52', 'G53', 'G54', 'G55', 'G56', 'G57', 'G58', 'G59', 'G60', 'G61', 'G62', 'LF1', 'LF2', 'LF3', 'LF4', 'LF5', 'LF6', 'FP5', 'FP6', 'AP1', 'AP2', 'AP3', 'AP4', 'AP5', 'AP6', 'PP1', 'PP2', 'PP3', 'PP4', 'PP5', 'PP6', 'RAIH1', 'RAIH2', 'RAIH4', 'RAIH5', 'RAIH6', 'RMIH1', 'RMIH2', 'RMIH3', 'RMIH4', 'RPIH1', 'RPIH3', 'RPIH4', 'RPIH5', 'RPIH6', 'RPPIH1', 'RPPIH3', 'RPPIH4', 'RPPIH5', 'RPPIH6', 'LMIH1', 'LMIH2', 'LMIH3', 'LMIH4', 'MF1', 'MF2', 'MF3', 'MF4', 'MF5', 'MF6', 'LPPIH1', 'LPPIH2', 'LPPIH3', 'LPPIH4', 'LPPIH5', 'LPPIH6'],
        'soz_channels': ['G1', 'G2', 'G9', 'G10', 'G17', 'G18'],
        'surgery_outcome': 'S'
    },
    ('sub-pt13', '02'): {
        'channels': ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G11', 'G12', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'G33', 'G34', 'G35', 'G36', 'G37', 'G38', '$G11', '$G12', 'G39', 'G40', 'G41', 'G42', 'G43', 'G44', 'G45', 'G46', 'G47', 'G48', 'G49', 'G50', 'G51', 'G52', 'G53', 'G54', 'G55', 'G56', 'G57', 'G58', 'G59', 'G60', 'G61', 'G62', 'LF1', 'LF2', 'LF3', 'LF4', 'LF5', 'LF6', 'FP5', 'FP6', 'AP1', 'AP2', 'AP3', 'AP4', 'AP5', 'AP6', 'PP1', 'PP2', 'PP3', 'PP4', 'PP5', 'PP6', 'RAIH1', 'RAIH2', 'RAIH4', 'RAIH5', 'RAIH6', 'RMIH1', 'RMIH2', 'RMIH3', 'RMIH4', 'RPIH1', 'RPIH3', 'RPIH4', 'RPIH5', 'RPIH6', 'RPPIH1', 'RPPIH3', 'RPPIH4', 'RPPIH5', 'RPPIH6', 'LMIH1', 'LMIH2', 'LMIH3', 'LMIH4', 'MF1', 'MF2', 'MF3', 'MF4', 'MF5', 'MF6', 'LPPIH1', 'LPPIH2', 'LPPIH3', 'LPPIH4', 'LPPIH5', 'LPPIH6'],
        'soz_channels': ['G1', 'G2', 'G9', 'G10', 'G17', 'G18'],
        'surgery_outcome': 'S'
    },
    ('sub-pt13', '03'): {
        'channels': ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G11', 'G12', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'G33', 'G34', 'G35', 'G36', 'G37', 'G38', '$G11', '$G12', 'G39', 'G40', 'G41', 'G42', 'G43', 'G44', 'G45', 'G46', 'G47', 'G48', 'G49', 'G50', 'G51', 'G52', 'G53', 'G54', 'G55', 'G56', 'G57', 'G58', 'G59', 'G60', 'G61', 'G62', 'LF1', 'LF2', 'LF3', 'LF4', 'LF5', 'LF6', 'FP5', 'FP6', 'AP1', 'AP2', 'AP3', 'AP4', 'AP5', 'AP6', 'PP1', 'PP2', 'PP3', 'PP4', 'PP5', 'PP6', 'RAIH1', 'RAIH2', 'RAIH4', 'RAIH5', 'RAIH6', 'RMIH1', 'RMIH2', 'RMIH3', 'RMIH4', 'RPIH1', 'RPIH3', 'RPIH4', 'RPIH5', 'RPIH6', 'RPPIH1', 'RPPIH3', 'RPPIH4', 'RPPIH5', 'RPPIH6', 'LMIH1', 'LMIH2', 'LMIH3', 'LMIH4', 'MF1', 'MF2', 'MF3', 'MF4', 'MF5', 'MF6', 'LPPIH1', 'LPPIH2', 'LPPIH3', 'LPPIH4', 'LPPIH5', 'LPPIH6'],
        'soz_channels': ['G1', 'G2', 'G9', 'G10', 'G17', 'G18'],
        'surgery_outcome': 'S'
    },
    ('sub-pt13', '04'): {
        'channels': ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G11', 'G12', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32', 'G33', 'G34', 'G35', 'G36', 'G37', 'G38', '$G11', '$G12', 'G39', 'G40', 'G41', 'G42', 'G43', 'G44', 'G45', 'G46', 'G47', 'G48', 'G49', 'G50', 'G51', 'G52', 'G53', 'G54', 'G55', 'G56', 'G57', 'G58', 'G59', 'G60', 'G61', 'G62', 'LF1', 'LF2', 'LF3', 'LF4', 'LF5', 'LF6', 'FP5', 'FP6', 'AP1', 'AP2', 'AP3', 'AP4', 'AP5', 'AP6', 'PP1', 'PP2', 'PP3', 'PP4', 'PP5', 'PP6', 'RAIH1', 'RAIH2', 'RAIH4', 'RAIH5', 'RAIH6', 'RMIH1', 'RMIH2', 'RMIH3', 'RMIH4', 'RPIH1', 'RPIH3', 'RPIH4', 'RPIH5', 'RPIH6', 'RPPIH1', 'RPPIH3', 'RPPIH4', 'RPPIH5', 'RPPIH6', 'LMIH1', 'LMIH2', 'LMIH3', 'LMIH4', 'MF1', 'MF2', 'MF3', 'MF4', 'MF5', 'MF6', 'LPPIH1', 'LPPIH2', 'LPPIH3', 'LPPIH4', 'LPPIH5', 'LPPIH6'],
        'soz_channels': ['G1', 'G2', 'G9', 'G10', 'G17', 'G18'],
        'surgery_outcome': 'S'
    },
    ('sub-pt14', '01'): {
        'channels': ['G2', 'G3', 'G4', 'G8', 'G10', 'G11', 'G12', 'G16', 'G18', 'G19', 'G20', 'G21', 'G22', 'G24', 'G27', 'G28', 'G13', 'G14', 'G29', 'G30', 'G31', 'G32', 'TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6', 'AST1', 'AST2', 'AST3', 'AST4', 'MST1', '$G13', '$G14', 'MST2', 'MST3', 'MST4', 'PST1', 'PST2', 'PST3', 'PPST1', 'PPST2', 'PPST3', 'PPST4', 'PT1', 'PT2', "PT3'", 'PT4', 'PT5', 'PT6', 'LF1', 'LF2', 'LF3', 'LF4', 'LF5', 'LF6', 'OF1', 'OF2', 'OF3', 'OF4'],
        'soz_channels': ['TT1', 'TT2', 'TT3', 'AST1', 'AST2', 'MST1', 'MST2'],
        'surgery_outcome': 'F'
    },
    ('sub-pt14', '02'): {
        'channels': ['G2', 'G3', 'G4', 'G8', 'G10', 'G11', 'G12', 'G16', 'G18', 'G19', 'G20', 'G21', 'G22', 'G24', 'G27', 'G28', 'G13', 'G14', 'G29', 'G30', 'G31', 'G32', 'TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6', 'AST1', 'AST2', 'AST3', 'AST4', 'MST1', '$G13', '$G14', 'MST2', 'MST3', 'MST4', 'PST1', 'PST2', 'PST3', 'PPST1', 'PPST2', 'PPST3', 'PPST4', 'PT1', 'PT2', "PT3'", 'PT4', 'PT5', 'PT6', 'LF1', 'LF2', 'LF3', 'LF4', 'LF5', 'LF6', 'OF1', 'OF2', 'OF3', 'OF4'],
        'soz_channels': ['TT1', 'TT2', 'TT3', 'AST1', 'AST2', 'MST1', 'MST2'],
        'surgery_outcome': 'F'
    },
    ('sub-pt14', '03'): {
        'channels': ['G2', 'G3', 'G4', 'G8', 'G10', 'G11', 'G12', 'G16', 'G18', 'G19', 'G20', 'G21', 'G22', 'G24', 'G27', 'G28', 'G13', 'G14', 'G29', 'G30', 'G31', 'G32', 'TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6', 'AST1', 'AST2', 'AST3', 'AST4', 'MST1', '$G13', '$G14', 'MST2', 'MST3', 'MST4', 'PST1', 'PST2', 'PST3', 'PPST1', 'PPST2', 'PPST3', 'PPST4', 'PT1', 'PT2', "PT3'", 'PT4', 'PT5', 'PT6', 'LF1', 'LF2', 'LF3', 'LF4', 'LF5', 'LF6', 'OF1', 'OF2', 'OF3', 'OF4'],
        'soz_channels': ['TT1', 'TT2', 'TT3', 'AST1', 'AST2', 'MST1', 'MST2'],
        'surgery_outcome': 'F'
    },
    ('sub-pt15', '01'): {
        'channels': ['G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G11', 'G12', 'G15', 'G16', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G27', 'G28', 'G29', 'G13', 'G14', 'G30', 'G31', 'G32', 'TT1', 'TT2', 'TT3', 'TT4', 'TT6', 'AST1', 'AST2', 'AST3', 'AST4', 'MST1', 'MST2', '$G13', '$G14', 'MST3', 'MST4', 'PST1', 'PST2', 'PPST1', 'PPST2', 'PPST3', 'PPST4', 'TO1', 'TO2', 'TO3', 'TO4', 'TO5', 'TO6', 'TP1', 'TP2', 'TP3', 'TP4', 'TP5', 'TP6', 'OF1', 'OF3', 'OF4', 'LIF1', 'LIF2', 'LIF3', 'LIF4', 'LIF5', 'LIF6', 'LSF1', 'LSF2', 'LSF3', 'LSF4', 'LSF5', 'LSF6', 'LSF7'],
        'soz_channels': ['TT1', 'TT2', 'TT3', 'TT4', 'AST1', 'AST2', 'AST3', 'AST4', 'MST1', 'MST2', 
    'G2', 'G3', 'G4', 'G5', 'G10', 'G11', 'G12', 'G13'],
        'surgery_outcome': 'S'
    },
    ('sub-pt15', '02'): {
        'channels': ['G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G11', 'G12', 'G15', 'G16', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G27', 'G28', 'G29', 'G13', 'G14', 'G30', 'G31', 'G32', 'TT1', 'TT2', 'TT3', 'TT4', 'TT6', 'AST1', 'AST2', 'AST3', 'AST4', 'MST1', 'MST2', '$G13', '$G14', 'MST3', 'MST4', 'PST1', 'PST2', 'PPST1', 'PPST2', 'PPST3', 'PPST4', 'TO1', 'TO2', 'TO3', 'TO4', 'TO5', 'TO6', 'TP1', 'TP2', 'TP3', 'TP4', 'TP5', 'TP6', 'OF1', 'OF3', 'OF4', 'LIF1', 'LIF2', 'LIF3', 'LIF4', 'LIF5', 'LIF6', 'LSF1', 'LSF2', 'LSF3', 'LSF4', 'LSF5', 'LSF6', 'LSF7'],
        'soz_channels': ['TT1', 'TT2', 'TT3', 'TT4', 'AST1', 'AST2', 'AST3', 'AST4', 'MST1', 'MST2', 
    'G2', 'G3', 'G4', 'G5', 'G10', 'G11', 'G12', 'G13'],
        'surgery_outcome': 'S'
    },
    ('sub-pt15', '03'): {
        'channels': ['G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G11', 'G12', 'G15', 'G16', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G27', 'G28', 'G29', 'G13', 'G14', 'G30', 'G31', 'G32', 'TT1', 'TT2', 'TT3', 'TT4', 'TT6', 'AST1', 'AST2', 'AST3', 'AST4', 'MST1', 'MST2', '$G13', '$G14', 'MST3', 'MST4', 'PST1', 'PST2', 'PPST1', 'PPST2', 'PPST3', 'PPST4', 'TO1', 'TO2', 'TO3', 'TO4', 'TO5', 'TO6', 'TP1', 'TP2', 'TP3', 'TP4', 'TP5', 'TP6', 'OF1', 'OF3', 'OF4', 'LIF1', 'LIF2', 'LIF3', 'LIF4', 'LIF5', 'LIF6', 'LSF1', 'LSF2', 'LSF3', 'LSF4', 'LSF5', 'LSF6', 'LSF7'],
        'soz_channels': ['TT1', 'TT2', 'TT3', 'TT4', 'AST1', 'AST2', 'AST3', 'AST4', 'MST1', 'MST2', 
    'G2', 'G3', 'G4', 'G5', 'G10', 'G11', 'G12', 'G13'],
        'surgery_outcome': 'S'
    },
    ('sub-pt15', '04'): {
        'channels': ['G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G11', 'G12', 'G15', 'G16', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G27', 'G28', 'G29', 'G13', 'G14', 'G30', 'G31', 'G32', 'TT1', 'TT2', 'TT3', 'TT4', 'TT6', 'AST1', 'AST2', 'AST3', 'AST4', 'MST1', 'MST2', '$G13', '$G14', 'MST3', 'MST4', 'PST1', 'PST2', 'PPST1', 'PPST2', 'PPST3', 'PPST4', 'TO1', 'TO2', 'TO3', 'TO4', 'TO5', 'TO6', 'TP1', 'TP2', 'TP3', 'TP4', 'TP5', 'TP6', 'OF1', 'OF3', 'OF4', 'LIF1', 'LIF2', 'LIF3', 'LIF4', 'LIF5', 'LIF6', 'LSF1', 'LSF2', 'LSF3', 'LSF4', 'LSF5', 'LSF6', 'LSF7'],
        'soz_channels': ['TT1', 'TT2', 'TT3', 'TT4', 'AST1', 'AST2', 'AST3', 'AST4', 'MST1', 'MST2', 
    'G2', 'G3', 'G4', 'G5', 'G10', 'G11', 'G12', 'G13'],
        'surgery_outcome': 'S'
    },
    ('sub-pt16', '01'): {
        'channels': ['OF1', 'OF2', 'OF3', 'OF4', 'TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6', 'AST3', 'AST4', 'MST1', 'MST2', 'MST3', 'MST4', 'PST1', 'PST2', 'PST3', 'PST4', 'G4', 'AST1', 'AST2', 'G5', 'G6', 'G7', 'G8', 'G12', 'G13', 'G14', 'G15', 'G16', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', '$AST1', '$AST2', 'G24', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'AST1'],
        'surgery_outcome': 'S'
    },
    ('sub-pt16', '02'): {
        'channels': ['OF1', 'OF2', 'OF3', 'OF4', 'TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6', 'AST3', 'AST4', 'MST1', 'MST2', 'MST3', 'MST4', 'PST1', 'PST2', 'PST3', 'PST4', 'G4', 'AST1', 'AST2', 'G5', 'G6', 'G7', 'G8', 'G12', 'G13', 'G14', 'G15', 'G16', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', '$AST1', '$AST2', 'G24', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'AST1'],
        'surgery_outcome': 'S'
    },
    ('sub-pt16', '03'): {
        'channels': ['OF1', 'OF2', 'OF3', 'OF4', 'TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6', 'AST3', 'AST4', 'MST1', 'MST2', 'MST3', 'MST4', 'PST1', 'PST2', 'PST3', 'PST4', 'G4', 'AST1', 'AST2', 'G5', 'G6', 'G7', 'G8', 'G12', 'G13', 'G14', 'G15', 'G16', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', '$AST1', '$AST2', 'G24', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'AST1'],
        'surgery_outcome': 'S'
    },
    ('sub-pt17', '02'): {
        'channels': ['OF1', 'OF2', 'OF3', 'OF4', 'TT1', 'TT2', 'TT3', 'TT4', 'TT5', 'TT6', 'AST3', 'AST4', 'MST1', 'MST2', 'MST3', 'MST4', 'PST1', 'PST2', 'PST3', 'PST4', 'G4', 'AST1', 'AST2', 'G5', 'G6', 'G7', 'G8', 'G12', 'G13', 'G14', 'G15', 'G16', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', '$AST1', '$AST2', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['TT1', 'TT2'],
        'surgery_outcome': 'S'
    },
    ('sub-umf001', '01'): {
        'channels': ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9', 'C10', 'C11', 'C12', 'C13', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21', 'C22', 'C23', 'C24', 'C25', 'C26', 'C27', 'C28', 'C29', 'C30', 'C31', 'C32', 'C33', 'C34', 'C35', 'C36', 'C37', 'C38', 'C39', 'C40', 'C41', 'C42', 'C43', 'C44', 'C45', 'C46', 'C47', 'C48', 'C49', 'C50', 'C51', 'C52', 'C53', 'C54', 'C55', 'C56', 'C57', 'C58', 'C59', 'C60', 'C61', 'C62', 'C63', 'C64', 'BTM1', 'BTM2', 'BTM3', 'BTM4', 'BTM5', 'BTM6', 'BTP1', 'BTP2', 'BTP3', 'BTP4', 'BTP5', 'BTP6'],
        'soz_channels': ['BTM1', 'BTM2', 'BTM3', 'BTM4', 'BTM5', 'BTM6', 
    'BTP1', 'BTP2', 'BTP3', 'BTP4', 'BTP5', 'BTP6', 
    'C33', 'C34', 'C41', 'C42', 'C43', 'C49', 'C50', 
    'C51', 'C52', 'C53', 'C54', 'C55', 'C56', 'C57', 
    'C58', 'C59', 'C60', 'C61', 'C62', 'C63', 'C64'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc001', '01'): {
        'channels': ['GP1', 'GP2', 'GP3', 'GP4', 'GP5', 'GP6', 'GP7', 'GP8', 'GP9', 'GP10', 'GP11', 'GP12', 'GP13', 'GP14', 'GP15', 'GP16', 'GP17', 'GP18', 'GP19', 'GP20', 'GP21', 'GP22', 'GP24', 'GP25', 'GP26', 'GP27', 'GP28', 'GP29', 'GP31', 'GP32', 'F1', 'F3', 'F4', 'F5', 'F6', 'GA1', 'GA2', 'GA3', 'GA4', 'GA5', 'GA6', 'GA7', 'GA8', 'GA9', 'GA10', 'GA11', 'GA12', 'GA13', 'GA14', 'GA15', 'GA16', 'GA17', 'GA18', 'GA19', 'GA20', 'GA21', 'GA22', 'GA23', 'GA24', 'GA25', 'GA26', 'GA27', 'GA28', 'GA29', 'GA30', 'GA31', 'GA32', 'OFS1', 'OFS2', 'OFS3', 'OFS4', 'OFI1', 'OFI2', 'OFI3', 'OFI4', 'OFI5', 'TS2', 'TS3', 'TS4', 'TS5', 'TS6', 'TI2', 'TI3', 'TI4', 'TI5', 'TI6', 'TI7'],
        'soz_channels': ['GP13', 'GP21', 'GP29'],
        'surgery_outcome': 'NR'
    },
    ('sub-ummc001', '02'): {
        'channels': ['GP1', 'GP2', 'GP3', 'GP4', 'GP5', 'GP6', 'GP7', 'GP8', 'GP9', 'GP10', 'GP11', 'GP12', 'GP13', 'GP14', 'GP15', 'GP16', 'GP17', 'GP18', 'GP19', 'GP20', 'GP21', 'GP22', 'GP24', 'GP25', 'GP26', 'GP27', 'GP28', 'GP29', 'GP31', 'GP32', 'F1', 'F3', 'F4', 'F5', 'F6', 'GA1', 'GA2', 'GA3', 'GA4', 'GA5', 'GA6', 'GA7', 'GA8', 'GA9', 'GA10', 'GA11', 'GA12', 'GA13', 'GA14', 'GA15', 'GA16', 'GA17', 'GA18', 'GA19', 'GA20', 'GA21', 'GA22', 'GA23', 'GA24', 'GA25', 'GA26', 'GA27', 'GA28', 'GA29', 'GA30', 'GA31', 'GA32', 'OFS1', 'OFS2', 'OFS3', 'OFS4', 'OFI1', 'OFI2', 'OFI3', 'OFI4', 'OFI5', 'TS2', 'TS3', 'TS4', 'TS5', 'TS6', 'TI2', 'TI3', 'TI4', 'TI5', 'TI6', 'TI7'],
        'soz_channels': ['GP13', 'GP21', 'GP29'],
        'surgery_outcome': 'NR'
    },
    ('sub-ummc001', '03'): {
        'channels': ['GP1', 'GP2', 'GP3', 'GP4', 'GP5', 'GP6', 'GP7', 'GP8', 'GP9', 'GP10', 'GP11', 'GP12', 'GP13', 'GP14', 'GP15', 'GP16', 'GP17', 'GP18', 'GP19', 'GP20', 'GP21', 'GP22', 'GP24', 'GP25', 'GP26', 'GP27', 'GP28', 'GP29', 'GP31', 'GP32', 'F1', 'F3', 'F4', 'F5', 'F6', 'GA1', 'GA2', 'GA3', 'GA4', 'GA5', 'GA6', 'GA7', 'GA8', 'GA9', 'GA10', 'GA11', 'GA12', 'GA13', 'GA14', 'GA15', 'GA16', 'GA17', 'GA18', 'GA19', 'GA20', 'GA21', 'GA22', 'GA23', 'GA24', 'GA25', 'GA26', 'GA27', 'GA28', 'GA29', 'GA30', 'GA31', 'GA32', 'OFS1', 'OFS2', 'OFS3', 'OFS4', 'OFI1', 'OFI2', 'OFI3', 'OFI4', 'OFI5', 'TS2', 'TS3', 'TS4', 'TS5', 'TS6', 'TI2', 'TI3', 'TI4', 'TI5', 'TI6', 'TI7'],
        'soz_channels': ['GP13', 'GP21', 'GP29'],
        'surgery_outcome': 'NR'
    },
    ('sub-ummc002', '01'): {
        'channels': ['LFUP3', 'LFUP4', 'LFUP5', 'LFUP6', 'LFL1', 'LFL2', 'LFL3', 'LFL4', 'LFL5', 'LFL6', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G24', 'G25', 'G26', 'G28', 'G29', 'G30', 'G31', 'G32', 'ANT1', 'ANT2', 'ANT3', 'ANT4', 'MEST1', 'MEST2', 'MEST3', 'MEST4', 'MEST5', 'MEST6', 'SUBT2', 'SUBT3', 'SUBT4'],
        'soz_channels': ['ANT1', 'ANT2', 'ANT3', 'MEST1', 'MEST2', 'MEST3', 'MEST4', 'ATT1', 'ATT2', 'ATT3'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc002', '02'): {
        'channels': ['SUPF3', 'SUPF4', 'SUPF5', 'SUPF6', 'IF1', 'IF2', 'IF3', 'IF4', 'IF5', 'IF6', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G24', 'G25', 'G26', 'G28', 'G29', 'G30', 'G31', 'G32', 'ANT1', 'ANT2', 'ANT3', 'ANT4', 'MEST1', 'MEST2', 'MEST3', 'MEST4', 'MEST5', 'MEST6', 'SUBT2', 'SUBT3', 'SUBT4'],
        'soz_channels': ['ANT1', 'ANT2', 'ANT3', 'MEST1', 'MEST2', 'MEST3', 'MEST4', 'ATT1', 'ATT2', 'ATT3'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc002', '03'): {
        'channels': ['SUPF3', 'SUPF4', 'SUPF5', 'SUPF6', 'IF1', 'IF2', 'IF3', 'IF4', 'IF5', 'IF6', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G24', 'G25', 'G26', 'G28', 'G29', 'G30', 'G31', 'G32', 'ANT1', 'ANT2', 'ANT3', 'ANT4', 'MEST1', 'MEST2', 'MEST3', 'MEST4', 'MEST5', 'MEST6', 'SUBT2', 'SUBT3', 'SUBT4'],
        'soz_channels': ['ANT1', 'ANT2', 'ANT3', 'MEST1', 'MEST2', 'MEST3', 'MEST4', 'ATT1', 'ATT2', 'ATT3'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc003', '01'): {
        'channels': ['LF3', 'LF4', 'LF5', 'LF6', 'SF1', 'SF2', 'SF3', 'SF4', 'ANTT1', 'ANTT2', 'ANTT3', 'ANTT4', 'MEST1', 'MEST2', 'MEST3', 'MEST4', 'MEST5', 'MEST6', 'G3', 'G4', 'G5', 'G6', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G15', 'G16', 'G17', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['MEST3', 'MEST4', 'MEST5', 'G4', 'G10', 'G12', 'G18', 'G19', 'G20', 'G26', 'G27', 'G28'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc003', '02'): {
        'channels': ['LF3', 'LF4', 'LF5', 'LF6', 'SF1', 'SF2', 'SF3', 'SF4', 'ANTT1', 'ANTT2', 'ANTT3', 'ANTT4', 'MEST1', 'MEST2', 'MEST3', 'MEST4', 'MEST5', 'MEST6', 'G3', 'G4', 'G5', 'G6', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G15', 'G16', 'G17', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['MEST3', 'MEST4', 'MEST5', 'G4', 'G10', 'G12', 'G18', 'G19', 'G20', 'G26', 'G27', 'G28'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc003', '03'): {
        'channels': ['LF3', 'LF4', 'LF5', 'LF6', 'SF1', 'SF2', 'SF3', 'SF4', 'ANTT1', 'ANTT2', 'ANTT3', 'ANTT4', 'MEST1', 'MEST2', 'MEST3', 'MEST4', 'MEST5', 'MEST6', 'G3', 'G4', 'G5', 'G6', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G15', 'G16', 'G17', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['MEST3', 'MEST4', 'MEST5', 'G4', 'G10', 'G12', 'G18', 'G19', 'G20', 'G26', 'G27', 'G28'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc004', '01'): {
        'channels': ['LF3', 'LF4', 'LF5', 'LF6', 'SF1', 'SF2', 'SF3', 'SF4', 'SF5', 'SF6', 'AT1', 'AT2', 'AT3', 'AT4', 'AT5', 'AT6', 'ST1', 'ST2', 'ST3', 'ST4', 'G1', 'G2', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G11', 'G12', 'G13', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['AT1', 'AT2'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc004', '02'): {
        'channels': ['LF3', 'LF4', 'LF5', 'LF6', 'SF1', 'SF2', 'SF3', 'SF4', 'SF5', 'SF6', 'AT1', 'AT2', 'AT3', 'AT4', 'AT5', 'AT6', 'ST1', 'ST2', 'ST3', 'ST4', 'G1', 'G2', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G11', 'G12', 'G13', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['AT1', 'AT2'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc004', '03'): {
        'channels': ['LF3', 'LF4', 'LF5', 'LF6', 'SF1', 'SF2', 'SF3', 'SF4', 'SF5', 'SF6', 'AT1', 'AT2', 'AT3', 'AT4', 'AT5', 'AT6', 'ST1', 'ST2', 'ST3', 'ST4', 'G1', 'G2', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G11', 'G12', 'G13', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['AT1', 'AT2'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc005', '01'): {
        'channels': ['F3', 'F4', 'F5', 'F6', 'AT1', 'AT2', 'AT3', 'AT4', 'AT5', 'AT6', 'PT1', 'PT2', 'PT3', 'PT4', 'PT5', 'PT6', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['AT1', 'AT2', 'G17', 'G19', 'G25', 'G27'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc005', '02'): {
        'channels': ['F3', 'F4', 'F5', 'F6', 'AT1', 'AT2', 'AT3', 'AT4', 'AT5', 'AT6', 'PT1', 'PT2', 'PT3', 'PT4', 'PT5', 'PT6', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['AT1', 'AT2', 'G17', 'G19', 'G25', 'G27'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc006', '01'): {
        'channels': ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'SF1', 'SF2', 'SF3', 'SF4', 'SF5', 'SF6', 'MEST1', 'MEST2', 'MEST3', 'MEST4', 'MEST5', 'MEST6', 'MT1', 'MT2', 'MT3', 'MT4', 'G3', 'G4', 'G5', 'G7', 'G8', 'G11', 'G12', 'G13', 'G15', 'G16', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G28', 'G29', 'G30', 'G31', 'G32', 'POST2', 'POST3', 'POST4', 'POST5', 'POST6', 'LAT2', 'LAT3', 'LAT4'],
        'soz_channels': ['MT1', 'MT2', 'MT3', 'MT4', 'MEST1', 'MEST2', 'MEST3', 'MEST4', 'MEST5'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc006', '02'): {
        'channels': ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'SF1', 'SF2', 'SF3', 'SF4', 'SF5', 'SF6', 'MEST1', 'MEST2', 'MEST3', 'MEST4', 'MEST5', 'MEST6', 'MT1', 'MT2', 'MT3', 'MT4', 'G3', 'G4', 'G5', 'G7', 'G8', 'G11', 'G12', 'G13', 'G15', 'G16', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G28', 'G29', 'G30', 'G31', 'G32', 'POST2', 'POST3', 'POST4', 'POST5', 'POST6', 'LAT2', 'LAT3', 'LAT4'],
        'soz_channels': ['MT1', 'MT2', 'MT3', 'MT4', 'MEST1', 'MEST2', 'MEST3', 'MEST4', 'MEST5'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc006', '03'): {
        'channels': ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'SF1', 'SF2', 'SF3', 'SF4', 'SF5', 'SF6', 'MEST1', 'MEST2', 'MEST3', 'MEST4', 'MEST5', 'MEST6', 'MT1', 'MT2', 'MT3', 'MT4', 'G3', 'G4', 'G5', 'G7', 'G8', 'G11', 'G12', 'G13', 'G15', 'G16', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G28', 'G29', 'G30', 'G31', 'G32', 'POST2', 'POST3', 'POST4', 'POST5', 'POST6', 'LAT2', 'LAT3', 'LAT4'],
        'soz_channels': ['MT1', 'MT2', 'MT3', 'MT4', 'MEST1', 'MEST2', 'MEST3', 'MEST4', 'MEST5'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc007', '01'): {
        'channels': ['LANT1', 'LANT2', 'LANT3', 'LANT4', 'LANT5', 'LANT6', 'LMES1', 'LMES2', 'LMES3', 'LMES4', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'RANT1', 'RANT2', 'RANT3', 'RANT4', 'RANT5', 'RANT6', 'RMES1', 'RMES2', 'RMES3', 'RMES4', 'RPT1', 'RPT2', 'RPT3', 'RPT4', 'RPT5', 'RPT6'],
        'soz_channels': ['LMES1', 'LMES2', 'LMES3', 'LMES4'],
        'surgery_outcome': 'NR'
    },
    ('sub-ummc007', '02'): {
        'channels': ['LANT1', 'LANT2', 'LANT3', 'LANT4', 'LANT5', 'LANT6', 'LMES1', 'LMES2', 'LMES3', 'LMES4', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'RANT1', 'RANT2', 'RANT3', 'RANT4', 'RANT5', 'RANT6', 'RMES1', 'RMES2', 'RMES3', 'RMES4', 'RPT1', 'RPT2', 'RPT3', 'RPT4', 'RPT5', 'RPT6'],
        'soz_channels': ['LMES1', 'LMES2', 'LMES3', 'LMES4'],
        'surgery_outcome': 'NR'
    },
    ('sub-ummc007', '03'): {
        'channels': ['LANT1', 'LANT2', 'LANT3', 'LANT4', 'LANT5', 'LANT6', 'LMES1', 'LMES2', 'LMES3', 'LMES4', 'LPT3', 'LPT4', 'LPT5', 'LPT6', 'RANT1', 'RANT2', 'RANT3', 'RANT4', 'RANT5', 'RANT6', 'RMES1', 'RMES2', 'RMES3', 'RMES4', 'RPT1', 'RPT2', 'RPT3', 'RPT4', 'RPT5', 'RPT6'],
        'soz_channels': ['LMES1', 'LMES2', 'LMES3', 'LMES4'],
        'surgery_outcome': 'NR'
    },
    ('sub-ummc008', '01'): {
        'channels': ['F3', 'F4', 'F5', 'F6', 'SF1', 'SF2', 'SF3', 'SF4', 'SF5', 'SF6', 'AT1', 'AT2', 'AT3', 'AT4', 'MT1', 'MT2', 'MT3', 'MT4', 'PT1', 'PT2', 'PT3', 'PT4', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['G1', 'G2', 'G3', 'G4', 'G5', 'G9', 'G10', 'G11', 'G12', 'G13', 
    'G17', 'G18', 'G19', 'G20', 'G21', 'AT1', 'AT2', 'AT3', 'AT4', 
    'MT1', 'MT2', 'MT3', 'MT4'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc008', '02'): {
        'channels': ['F3', 'F4', 'F5', 'F6', 'SF1', 'SF2', 'SF3', 'SF4', 'SF5', 'SF6', 'AT1', 'AT2', 'AT3', 'AT4', 'MT1', 'MT2', 'MT3', 'MT4', 'PT1', 'PT2', 'PT3', 'PT4', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['G1', 'G2', 'G3', 'G4', 'G5', 'G9', 'G10', 'G11', 'G12', 'G13', 
    'G17', 'G18', 'G19', 'G20', 'G21', 'AT1', 'AT2', 'AT3', 'AT4', 
    'MT1', 'MT2', 'MT3', 'MT4'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc008', '03'): {
        'channels': ['F3', 'F4', 'F5', 'F6', 'SF1', 'SF2', 'SF3', 'SF4', 'SF5', 'SF6', 'AT1', 'AT2', 'AT3', 'AT4', 'MT1', 'MT2', 'MT3', 'MT4', 'PT1', 'PT2', 'PT3', 'PT4', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G20', 'G21', 'G22', 'G23', 'G24', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['G1', 'G2', 'G3', 'G4', 'G5', 'G9', 'G10', 'G11', 'G12', 'G13', 
    'G17', 'G18', 'G19', 'G20', 'G21', 'AT1', 'AT2', 'AT3', 'AT4', 
    'MT1', 'MT2', 'MT3', 'MT4'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc009', '01'): {
        'channels': ['F3', 'F4', 'F5', 'F6', 'AT1', 'AT2', 'AT3', 'AT4', 'AT5', 'AT6', 'PT1', 'PT2', 'PT3', 'PT4', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G21', 'G22', 'G23', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['G4', 'G5', 'G6', 'G7', 'G12', 'G14', 
    'PT1', 'PT2', 'PT3', 'PT4', 
    'AT1', 'AT2', 'AT3', 'AT4'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc009', '02'): {
        'channels': ['F3', 'F4', 'F5', 'F6', 'AT1', 'AT2', 'AT3', 'AT4', 'AT5', 'AT6', 'PT1', 'PT2', 'PT3', 'PT4', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G21', 'G22', 'G23', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['G4', 'G5', 'G6', 'G7', 'G12', 'G14', 
    'PT1', 'PT2', 'PT3', 'PT4', 
    'AT1', 'AT2', 'AT3', 'AT4'],
        'surgery_outcome': 'S'
    },
    ('sub-ummc009', '03'): {
        'channels': ['F3', 'F4', 'F5', 'F6', 'AT1', 'AT2', 'AT3', 'AT4', 'AT5', 'AT6', 'PT1', 'PT2', 'PT3', 'PT4', 'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 'G10', 'G11', 'G12', 'G13', 'G14', 'G15', 'G16', 'G17', 'G18', 'G19', 'G21', 'G22', 'G23', 'G24', 'G25', 'G26', 'G27', 'G28', 'G29', 'G30', 'G31', 'G32'],
        'soz_channels': ['G4', 'G5', 'G6', 'G7', 'G12', 'G14', 
    'PT1', 'PT2', 'PT3', 'PT4', 
    'AT1', 'AT2', 'AT3', 'AT4'],
        'surgery_outcome': 'S'
    },
}
