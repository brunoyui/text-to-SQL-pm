import pandas as pd

class LoaderResults(object):
    def __init__(self, *args, **kwargs):
        self.results = {}
        self.representation_path_EN = {
            'openai_shot0': '../results/english/openAI-representation_0-shot/evaluations/',
            'code_shot0': '../results/english/code-representation_0-shot/evaluations/',
            'openai_shot1': '../results/english/openAI-representation_1-shot/evaluations/',
            'code_shot1': '../results/english/code-representation_1-shot/evaluations/',
            'code_shot3': '../results/english/code-representation_3-shot/evaluations/',
            'code_shot5': '../results/english/code-representation_5-shot/evaluations/'
        }
        self.representation_path_PT = {
            'openai_shot0': '../results/portuguese/openAI-representation_0-shot/evaluations/',
            'code_shot0': '../results/portuguese/code-representation_0-shot/evaluations/',
            'openai_shot1': '../results/portuguese/openAI-representation_1-shot/evaluations/',
            'code_shot1': '../results/portuguese/code-representation_1-shot/evaluations/',
            'code_shot3': '../results/portuguese/code-representation_3-shot/evaluations/',
            'code_shot5': '../results/portuguese/code-representation_5-shot/evaluations/'
        }

    def get_data_frame_results(self, path, model):
        tmp_df = pd.read_csv(path, sep='\t', header = None)
        tmp_df.columns = ['id_' + model, 'predicted_' + model, 'gold_' + model, 'hardness_' + model, 'score_' + model]
        return tmp_df

    def load_results(self, models_r: dict):
        for key, value in models_r.items():
            file_path = self.__dict__[f"representation_path_{value['lang']}"][value['representation']] + 'scores_' + key + '_'  + value['metric'] + ".tsv"
            tmp_df = self.get_data_frame_results(file_path, key)
            self.results[key] = tmp_df

    def concat_all_results(self):
        tmp_df = pd.DataFrame()
        for value in self.results.values():
            tmp_df = pd.concat([tmp_df, value], axis=1)
        return tmp_df