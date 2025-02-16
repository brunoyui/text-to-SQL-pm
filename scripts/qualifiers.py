import pandas as pd
from utils import calculate_percentages_counts

BASE_TOTAL = 205
PARAPHRASE_TOTAL = 1450
BP_TOTAL = 1655

class Qualifier(object):
    base_paraphrase = {}
    results_c = {
        'gpt35': ['score_cr_gpt35', 'score_cr_gpt35_shot1','score_cr_gpt35_shot3', 
            'score_cr_gpt35_shot5'],
        'llama3': ['score_cr_llama3', 'score_cr_llama3_shot1', 'score_cr_llama3_shot3',
            'score_cr_llama3_shot5'] 
    }
    
    def __init__(self, base_paraphrase, *args, **kwargs):
        self.base_paraphrase = base_paraphrase
        pass

    def get_results_em(self, model_name, column):
        total_em = self.base_paraphrase.query("hardness_cr_" + model_name + " != 'no_hardness'")[column].value_counts()
        #print(total_em)
        total_ok = [self.base_paraphrase.query(c + " == 'True' and hardness_cr_" + model_name + " != 'no_hardness'")[column].value_counts() for c in self.results_c[model_name]] 
        return total_em, total_ok

    def get_results_ex(self, model_name, column):
        total_ex = self.base_paraphrase[column].value_counts()
        total_ok = [self.base_paraphrase.query(c + " == 1")[column].value_counts() for c in self.results_c[model_name]] 
        return total_ex, total_ok

#Event and Case Level (PMp)
class Qualifier1(Qualifier):
    def __init__(self, base_paraphrase, *args, **kwargs):
        super().__init__(base_paraphrase, *args, **kwargs)

#Perspective Level (PMp)
class Qualifier2(Qualifier):
    def __init__(self, base_paraphrase, *args, **kwargs):
        purpose = base_paraphrase
        purpose['Purpose_classification'] = purpose['Purpose_classification'].str.split(';')
        purpose = purpose.explode('Purpose_classification')
        purpose['Purpose_classification_class'] = purpose['Purpose_classification'].str.split(' - ').str.get(0)
        super().__init__(purpose, *args, **kwargs)

#Process mining concepts on SELECT (PMp)
class Qualifier3(Qualifier):
    def __init__(self, base_paraphrase, *args, **kwargs):
        projection = base_paraphrase
        projection['Projection_classification'] = projection['Projection_classification'].str.split(';')
        projection = projection.explode('Projection_classification')
        super().__init__(projection, *args, **kwargs)

#Process mining concepts on WHERE (PMp)
class Qualifier4(Qualifier):
    def __init__(self, base_paraphrase, *args, **kwargs):
        condition = base_paraphrase
        condition['Condition_classification'] = condition['Condition_classification'].str.split(';')
        condition = condition.explode('Condition_classification')
        super().__init__(condition, *args, **kwargs)

#WH question Level (NLp)
class Qualifier5(Qualifier):
    def __init__(self, base_paraphrase, *args, **kwargs):
        wh_question = base_paraphrase
        wh_question['Wh_classification'] = wh_question['Wh_classification'].str.split(';')
        wh_question = wh_question.explode('Wh_classification')
        super().__init__(wh_question, *args, **kwargs)

#Aggregation on SELECT (SQLp)
class Qualifier6(Qualifier):
    def __init__(self, base_paraphrase, *args, **kwargs):
        super().__init__(base_paraphrase, *args, **kwargs)

#Have GROUP BY (SQLp)
class Qualifier7(Qualifier):
    def __init__(self, base_paraphrase, *args, **kwargs):
        super().__init__(base_paraphrase, *args, **kwargs)

#SQL complexity (SQLp)
class Qualifier8(Qualifier):
    def __init__(self, base_paraphrase, *args, **kwargs):
        super().__init__(base_paraphrase, *args, **kwargs)

#Value, generic or domain (PMp)
class Qualifier9(Qualifier):
    def __init__(self, base_paraphrase, *args, **kwargs):
        super().__init__(base_paraphrase, *args, **kwargs)