import pandas as pd
from utils import calculate_percentages_counts
from sql_pattern import SQLPatternEasy, SQLPatternMedium, SQLPatternHard, SQLPatternExtra, SQLPatternNoHardness
from graphs_plot import plot_and_save_graph_results_by_model, plot_and_save_graph_results_no_hardness

class ExecutionByModel(object):
    results_c = {
        'gpt35': ['score_cr_gpt35', 'score_cr_gpt35_shot1','score_cr_gpt35_shot3', 
            'score_cr_gpt35_shot5'],
        'gemini10': ['score_cr_gemini10', 'score_cr_gemini10_shot1', 'score_cr_gemini10_shot3', 
            'score_cr_gemini10_shot5'],
        'llama3': ['score_cr_llama3', 'score_cr_llama3_shot1']
    }

    sql_pattern = {}
    sql_cat = ''

    def __init__(self, *args, **kwargs):
        pass

    def plot(self, data, file):
        plot_and_save_graph_results_by_model(data, file)

    def execute(self, file, models):
        filters = self.sql_pattern.get_filters()
        
        df_models = self.filter_results(self.sql_cat, models)
        percentages = self.calculate_percentages(df_models)
        self.plot(percentages['gpt35'], file)
        print(percentages)

    def filter_results(self, complexity, models):
        filters = self.sql_pattern.get_filters()
        df_models = {}

        for k, model in models.items():
            df_models[k] = {}
            for m, lang in model.items():
                df_models[k][m] = {}
                for l, mm in lang.items():
                    hardness_c = 'hardness_cr_' + k + ' == "' + complexity + '"'
                    df_model_complexity = mm.query(hardness_c)
                    df_filtered_models = {}
                    for key, value in filters.items():
                        df_filtered_models[key] = df_model_complexity.query(value)
                    
                    df_models[k][m][l] = df_filtered_models
        return df_models

    def calculate_percentages(self, df_models):
        percentages = {}

        for k, model in df_models.items():
            percentages[k] = {}
            for m, lang in model.items():
                percentages[k][m] = {}
                for l, mm in lang.items():
                    percentage_templates = {}
                    for key, value in mm.items():
                        percentage_templates[key] = calculate_percentages_counts(value, self.results_c[k], m)
                    
                    percentages[k][m][l] = percentage_templates
        return percentages

    def plot_configs(self):
        pass


class ExecutionEasy(ExecutionByModel):
    def __init__(self, *args, **kwargs):
        self.sql_pattern = SQLPatternEasy()
        self.sql_cat = 'easy'

class ExecutionMedium(ExecutionByModel):
    def __init__(self, *args, **kwargs):
        self.sql_pattern = SQLPatternMedium()
        self.sql_cat = 'medium'

class ExecutionHard(ExecutionByModel):
    def __init__(self, *args, **kwargs):
        self.sql_pattern = SQLPatternHard()
        self.sql_cat = 'hard'

class ExecutionExtra(ExecutionByModel):
    def __init__(self, *args, **kwargs):
        self.sql_pattern = SQLPatternExtra()
        self.sql_cat = 'extra'

class ExecutionNoHardness(ExecutionByModel):
    def __init__(self, *args, **kwargs):
        self.sql_pattern = SQLPatternNoHardness()
        self.sql_cat = 'no_hardness'

    def plot(self, data, file):
        plot_and_save_graph_results_no_hardness(data, file)