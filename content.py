
def Content():
    # About each data set,ex Ab_LR_1: Ab=About LR = Linear Regression, 1 : First data set
    LR_1_Name = 'Student Grade Data Set'
    LR_1_About = '''This data approach student achievement in secondary education of two Portuguese schools. The data attributes include student grades,
                    demographic, social and school related features and it was collected by using school reports and questionnaires. The data is collected
                    for performance in mathematics. The target is to predict grade 3 (G3) given the data. The actual G3 scored by the kids are included in
                    the data set. Click visualize to see how the co-effecients vary as we go through the data, vizualisation for how the error reduces over
                    time is also available'''
    LR_1_Len = 395
    LR_1_Col = 33
    LR_1_Col_names = ['G1', 'G2', 'G3', 'studytime', 'health']
    LR_1_Obj = 'G3'
    LR_1_Type = 'Whole Data Set'
    LR_1_Source = 'https://archive.ics.uci.edu/ml/datasets/Student+Performance'
    LR_1_data = 'student-mat.csv'
    LR_1_sep = ';'

    LR_2_Name = 'Data Set 2'
    LR_2_About = ''' Need to write something about data'''
    LR_2_Len = 649
    LR_2_Col = 33
    LR_2_Col_names = 'Grade 1, Grade 2, Studytime, Health etc'
    LR_2_Obj = 'To predict Grade 3'
    LR_2_Type = 'Answer Provided'
    LR_2_Source = 'https://archive.ics.uci.edu/ml/datasets/Student+Performance'
    LR_2_data = 'Yet to add'

    LR_3_Name = 'Data Set 3'
    LR_3_About = ''' Need to write something about data'''
    LR_3_Len = '395'
    LR_3_Col = '33'
    LR_3_Col_names = 'Grade 1, Grade 2, Studytime, Health etc'
    LR_3_Obj = 'To predict Grade 3'
    LR_3_Type = 'Answer Provided'
    LR_3_Source = 'https://archive.ics.uci.edu/ml/datasets/Student+Performance'
    LR_3_data = 'Yet to add'

    Content_dict = {'Linear Regression':[[LR_1_Name,LR_1_About,LR_1_Len,LR_1_Col,LR_1_Col_names,LR_1_Obj,LR_1_Type,LR_1_Source,LR_1_data,LR_1_sep],
                                         [LR_2_Name,LR_2_About,LR_2_Len,LR_2_Col,LR_2_Col_names,LR_2_Obj,LR_2_Type,LR_2_Source, LR_2_data],
                                         [LR_3_Name,LR_3_About,LR_3_Len,LR_3_Col,LR_3_Col_names,LR_3_Obj,LR_3_Type,LR_3_Source, LR_3_data]],
                    'Logistic Regression':[['Data Set 1 log', 'Link if used'],
                                         ['Data Set 2 log', 'Link if used'],
                                         ['Data Set 3 log', 'Link if used']],
                    'Nueral Networks': [['Data Set 1 NN', 'Link if used'],
                                          ['Data Set 2 NN', 'Link if used'],
                                          ['Data Set 3 NN', 'Link if used']]
                    }



    return Content_dict



