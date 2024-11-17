import pandas as pd
from utils import calculate_percentages_counts
from sql_pattern import SQLPatternEasy, SQLPatternMedium, SQLPatternHard, SQLPatternExtra, SQLPatternNoHardness
from graphs_plot import plot_and_save_graph_results

class Execution(object):
    models_results0 = ['score_opr_gpt35', 'score_cr_gpt35','score_opr_gemini10', 
            'score_cr_gemini10', 'score_opr_llama3', 'score_cr_llama3']
    models_results1 = ['score_opr_gpt35_shot1', 'score_cr_gpt35_shot1', 'score_opr_gemini10_shot1', 
            'score_cr_gemini10_shot1', 'score_opr_llama3_shot1', 'score_cr_llama3_shot1']
    sql_pattern = {}

    def __init__(self, *args, **kwargs):
        pass
    def execute(self, shot0, shot1, file, metric_label, metric):
        return None

    def filter_results(self, shot0, shot1, complexity):
        filters = self.sql_pattern.get_filters()
        shot0_complexity = shot0.query('hardness_opr_gpt35 == "' + complexity + '"')
        shot1_complexity = shot1.query('hardness_opr_gpt35_shot1 == "' + complexity + '"')
        df_filtered_shot0 = {}
        df_filtered_shot1 = {}

        for key, value in filters.items():
            df_filtered_shot0[key] = shot0_complexity.query(value)
            df_filtered_shot1[key] = shot1_complexity.query(value)
        
        return df_filtered_shot0, df_filtered_shot1

    def calculate_percentages(self, df_filtered_shot0, df_filtered_shot1, metric):
        percentages0 = []
        for key, value in df_filtered_shot0.items():
            percentages0 += calculate_percentages_counts(value, self.models_results0, metric)

        percentages1 = []
        for key, value in df_filtered_shot1.items():
            percentages1 += calculate_percentages_counts(value, self.models_results1, metric)
        return percentages0, percentages1

    def plot_configs(self):
        pass


class ExecutionEasy(Execution):
    def __init__(self, *args, **kwargs):
        self.sql_pattern = SQLPatternEasy()

    def execute(self, shot0, shot1, file, metric_label, metric):
        filters = self.sql_pattern.get_filters()
        df_filtered_shot0, df_filtered_shot1 = self.filter_results(shot0, shot1, 'easy')
        percentages0, percentages1 = self.calculate_percentages(df_filtered_shot0, df_filtered_shot1, metric)
        configs = self.plot_configs()
        plot_and_save_graph_results(percentages0, percentages1, file, **configs, metric_label=metric_label)

    def plot_configs(self):
        configs = {
            "categories": ['Sc', 'ScFc', 'ScGcFc$^+$', 'Ac', 'AcFc'],
            "x_pos": [0, 0.3, 0.6, 0.9, 1.2, 1.5,
                2.3, 2.6, 2.9, 3.2, 3.5, 3.8,
                4.6, 4.9, 5.2, 5.5, 5.8, 6.1,
                6.9, 7.2, 7.5, 7.8, 8.1, 8.4,
                9.2, 9.5, 9.8, 10.1, 10.4, 10.7],
            "x_positions": [0.75, 3.05, 5.35, 7.65, 9.95],
            "ax_text_pos": 90,
            "ax1_text_pos": 90,
            "ay_ticks": range(0, 90, 20),
            "ay_ticks1": range(0, 90, 20),
            "hspace": 0.25,
            "legend_anchor": (1.0, 1.4), 
            "fig_size": (20, 8)
        }
        return configs

class ExecutionMedium(Execution):
    def __init__(self, *args, **kwargs):
        self.sql_pattern = SQLPatternMedium()

    def execute(self, shot0, shot1, file, metric_label, metric):
        filters = self.sql_pattern.get_filters()
        df_filtered_shot0, df_filtered_shot1 = self.filter_results(shot0, shot1, 'medium')
        percentages0, percentages1 = self.calculate_percentages(df_filtered_shot0, df_filtered_shot1, metric)
        configs = self.plot_configs()
        plot_and_save_graph_results(percentages0, percentages1, file, **configs, metric_label=metric_label)

    def plot_configs(self):
        configs = {
            "categories": ['Sc$^+$', 'ScGc', 'Sc$^+$Fc$^+$', 'Sc$^+$GcFc$^+$', 'Acc$^+$Gc', 'Ac(c$^+$)$^*$Fc$^+$(Gc)$^*$', '(Ac)$^+$c(Fc)$^*$GcFc'],
            "x_pos": [0, 0.3, 0.6, 0.9, 1.2, 1.5,
                      2.3, 2.6, 2.9, 3.2, 3.5, 3.8,
                      4.6, 4.9, 5.2, 5.5, 5.8, 6.1,
                      6.9, 7.2, 7.5, 7.8, 8.1, 8.4,
                      9.2, 9.5, 9.8, 10.1, 10.4, 10.7,
                      11.5, 11.8, 12.1, 12.4, 12.7, 13,
                      13.8, 14.1, 14.4, 14.7, 15, 15.3],
            "x_positions": [0.75, 3.05, 5.35, 7.65, 9.95, 12.25, 14.55],
            "ax_text_pos": 90,
            "ax1_text_pos": 90,
            "ay_ticks": range(0, 90, 20),
            "ay_ticks1": range(0, 90, 20),
            "hspace": 0.25,
            "legend_anchor": (1.0, 1.4), 
            "fig_size": (24, 8)
        }
        return configs

class ExecutionHard(Execution):
    def __init__(self, *args, **kwargs):
        self.sql_pattern = SQLPatternHard()

    def execute(self, shot0, shot1, file, metric_label, metric):
        filters = self.sql_pattern.get_filters()
        df_filtered_shot0, df_filtered_shot1 = self.filter_results(shot0, shot1, 'hard')
        percentages0, percentages1 = self.calculate_percentages(df_filtered_shot0, df_filtered_shot1, metric)
        configs = self.plot_configs()
        plot_and_save_graph_results(percentages0, percentages1, file, **configs, metric_label=metric_label)

    def plot_configs(self):
        configs = {
            "categories": ['Sc$^+$Fc$^+$(Gc)$^*$', 'ScFSc', 'ScFcGcFc', 'ScGcFSc', 'AcFSc', 'AccFc$^+$Gc', 'SIE'],
            "x_pos": [0, 0.3, 0.6, 0.9, 1.2, 1.5,
                      2.3, 2.6, 2.9, 3.2, 3.5, 3.8,
                      4.6, 4.9, 5.2, 5.5, 5.8, 6.1,
                      6.9, 7.2, 7.5, 7.8, 8.1, 8.4,
                      9.2, 9.5, 9.8, 10.1, 10.4, 10.7,
                      11.5, 11.8, 12.1, 12.4, 12.7, 13,
                      13.8, 14.1, 14.4, 14.7, 15, 15.3],
            "x_positions": [0.75, 3.05, 5.35, 7.65, 9.95, 12.25, 14.55],
            "ax_text_pos": 90,
            "ax1_text_pos": 105,
            "ay_ticks": range(0, 90, 20),
            "ay_ticks1": range(0, 110, 20),
            "hspace": 0.45,
            "legend_anchor": (1.0, 1.4),
            "fig_size": (32, 8)
        }
        return configs


class ExecutionExtra(Execution):
    def __init__(self, *args, **kwargs):
        self.sql_pattern = SQLPatternExtra()

    def execute(self, shot0, shot1, file, metric_label, metric):
        filters = self.sql_pattern.get_filters()
        df_filtered_shot0, df_filtered_shot1 = self.filter_results(shot0, shot1, 'extra')
        percentages0, percentages1 = self.calculate_percentages(df_filtered_shot0, df_filtered_shot1, metric)
        configs = self.plot_configs()
        plot_and_save_graph_results(percentages0, percentages1, file, **configs, metric_label=metric_label)

    def plot_configs(self):
        configs = {
            "categories": ['ScFc$^+$(Gc)$^*$', 'ScFSc(Fc)$^*$(Gc)$^*$', 'Sc(Fc)$^*$GcFSc', 'Acc$^+$Fc$^*$Gc$^*$', 'AcFSc', 'AccGc(FSc)$^*$', 'SU'],
            "x_pos": [0, 0.3, 0.6, 0.9, 1.2, 1.5,
                      2.3, 2.6, 2.9, 3.2, 3.5, 3.8,
                      4.6, 4.9, 5.2, 5.5, 5.8, 6.1,
                      6.9, 7.2, 7.5, 7.8, 8.1, 8.4,
                      9.2, 9.5, 9.8, 10.1, 10.4, 10.7,
                      11.5, 11.8, 12.1, 12.4, 12.7, 13,
                      13.8, 14.1, 14.4, 14.7, 15, 15.3],
            "x_positions": [0.75, 3.05, 5.35, 7.65, 9.95, 12.25, 14.55],
            "ax_text_pos": 90,
            "ax1_text_pos": 105,
            "ay_ticks": range(0, 90, 20),
            "ay_ticks1": range(0, 110, 20),
            "hspace": 0.35,
            "legend_anchor": (1.0, 1.4), 
            "fig_size": (32, 8)
        }
        return configs

class ExecutionNoHardness(Execution):
    def __init__(self, *args, **kwargs):
        self.sql_pattern = SQLPatternNoHardness()

    def execute(self, shot0, shot1, file, metric_label, metric):
        filters = self.sql_pattern.get_filters()
        df_filtered_shot0, df_filtered_shot1 = self.filter_results(shot0, shot1, 'no_hardness')
        percentages0, percentages1 = self.calculate_percentages(df_filtered_shot0, df_filtered_shot1, metric)
        configs = self.plot_configs()
        plot_and_save_graph_results(percentages0, percentages1, file, **configs, metric_label=metric_label)

    def plot_configs(self):
        configs = {
            "categories": ['Sc$^+$Fc$^+$(Gc)$^*$', 'Sc$^+$Gc(Fc)$^*$', 'Sc$^+$(Fc)$^*$FSc(Gc)$^*$', 'Sc$^+$RS(Fc)$^*$', 'Ac(c)$^*$Fc$^+$(Gc)$^*$', 'AccFScGc', 'AccGc', 'Ac(c)$^*$RS(Fc)$^*$(Gc)$^*$', 'S(UE)$^+$', 'WS'],
            "x_pos": [0, 0.3, 0.6, 0.9, 1.2, 1.5,
                      2.3, 2.6, 2.9, 3.2, 3.5, 3.8,
                      4.6, 4.9, 5.2, 5.5, 5.8, 6.1,
                      6.9, 7.2, 7.5, 7.8, 8.1, 8.4,
                      9.2, 9.5, 9.8, 10.1, 10.4, 10.7,
                      11.5, 11.8, 12.1, 12.4, 12.7, 13,
                      13.8, 14.1, 14.4, 14.7, 15, 15.3,
                      16.1, 16.4, 16.7, 17, 17.3, 17.6,
                      18.4, 18.7, 19, 19.3, 19.6, 19.9,
                      20.8, 21.1, 21.4, 21.7, 22, 22.3],
            "x_positions": [0.75, 3.05, 5.35, 7.65, 9.95, 12.25, 14.55, 16.85, 19.15, 21.55],
            "ax_text_pos": 90,
            "ax1_text_pos": 90,
            "ay_ticks": range(0, 90, 20),
            "ay_ticks1": range(0, 90, 20),
            "hspace": 0.40,
            "legend_anchor": (1.0, 1.4),
            "fig_size": (40, 8)
        }
        return configs