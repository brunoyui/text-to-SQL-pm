import pandas as pd
from utils import calculate_percentages_counts
from sql_pattern import SQLPatternEasy
from graphs_plot import plot_and_save_graph_results

class Execution(object):
    models_results0 = ['score_opr_gpt35', 'score_cr_gpt35','score_opr_gemini10', 
            'score_cr_gemini10', 'score_opr_llama3', 'score_cr_llama3']
    models_results1 = ['score_opr_gpt35_shot1', 'score_cr_gpt35_shot1', 'score_opr_gemini10_shot1', 
            'score_cr_gemini10_shot1', 'score_opr_llama3_shot1', 'score_cr_llama3_shot1']
    def __init__(self, *args, **kwargs):
        pass
    def execute(self, shot0, shot1, file, metric_label):
        return None


class ExecutionEasy(Execution):
    def __init__(self, *args, **kwargs):
        self.sql_pattern = SQLPatternEasy()

    def execute(self, shot0, shot1, file, metric_label):
        filters = self.sql_pattern.get_filters()
        shot0_easy = shot0.query('hardness_opr_gpt35=="easy"')
        shot1_easy = shot1.query('hardness_opr_gpt35_shot1 =="easy"')
        df_filtered_shot0 = {}
        df_filtered_shot1 = {}

        for key, value in filters.items():
            df_filtered_shot0[key] = shot0_easy.query(value)
            df_filtered_shot1[key] = shot1_easy.query(value)
        
        percentages0 = []
        for key, value in df_filtered_shot0.items():
            percentages0 += calculate_percentages_counts(value, self.models_results0)

        percentages1 = []
        for key, value in df_filtered_shot1.items():
            print(value.columns)
            percentages1 += calculate_percentages_counts(value, self.models_results1)
        self.save_plt(file, metric_label, percentages0, percentages1)

    
    def save_plt(self, file, metric_label, percentages0, percentages1):
        categories = ['Sc', 'ScFc', 'ScGcFc$^+$', 'Ac', 'AcFc']
        x_pos = [0, 0.3, 0.6, 0.9, 1.2, 1.5,
                2.3, 2.6, 2.9, 3.2, 3.5, 3.8,
                4.6, 4.9, 5.2, 5.5, 5.8, 6.1,
                6.9, 7.2, 7.5, 7.8, 8.1, 8.4,
                9.2, 9.5, 9.8, 10.1, 10.4, 10.7]
        x_positions = [0.75, 3.05, 5.35, 7.65, 9.95]
        ax_text_pos = 90
        ax1_text_pos = 90
        ay_ticks = range(0, 90, 20)
        ay_ticks1 = range(0, 90, 20)
        hspace = 0.25 
        legend_anchor = (1.0, 1.4) 
        plot_and_save_graph_results(percentages0, percentages1, file, x_pos, x_positions, categories, 
            ax_text_pos, ax1_text_pos, ay_ticks, ay_ticks1, hspace, legend_anchor, metric_label)
