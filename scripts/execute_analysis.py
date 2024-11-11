import pandas as pd
from loader_results import LoaderResults
from execution import ExecutionEasy

def get_models_to_load(lang, metric):
    models_to_load_shot0 = {
        'opr_gpt35': {'lang': lang, 'representation': 'openai_shot0', 'metric': metric},
        'opr_gemini10': {'lang': lang, 'representation': 'openai_shot0', 'metric': metric},
        'opr_llama3': {'lang': lang, 'representation': 'openai_shot0', 'metric': metric},
        'cr_gpt35': {'lang': lang, 'representation': 'code_shot0', 'metric': metric},
        'cr_gemini10': {'lang': lang, 'representation': 'code_shot0', 'metric': metric},
        'cr_llama3': {'lang': lang, 'representation': 'code_shot0', 'metric': metric}
    }

    models_to_load_shot1 = {
        'opr_gpt35_shot1': {'lang': lang, 'representation': 'openai_shot1', 'metric': metric},
        'opr_gemini10_shot1': {'lang': lang, 'representation': 'openai_shot1', 'metric': metric},
        'opr_llama3_shot1': {'lang': lang, 'representation': 'openai_shot1', 'metric': metric},
        'cr_gpt35_shot1': {'lang': lang, 'representation': 'code_shot1', 'metric': metric},
        'cr_gemini10_shot1': {'lang': lang, 'representation': 'code_shot1', 'metric': metric},
        'cr_llama3_shot1': {'lang': lang, 'representation': 'code_shot1', 'metric': metric}
    }
    return models_to_load_shot0, models_to_load_shot1

def execute(lang, metric, sql_complexity, file, metric_label):
    path_ds = '../dataset/text2sql4pm.tsv'
    df_dataset = pd.read_csv(path_ds, sep='\t')
    df_dataset.dropna(how='all', inplace=True)
    
    models_to_load_shot0, models_to_load_shot1 = get_models_to_load(lang, metric)
    
    results = LoaderResults()
    results.load_results(models_to_load_shot0)
    shot0_df = results.concat_all_results()

    results1 = LoaderResults()
    results1.load_results(models_to_load_shot1)
    shot1_df = results1.concat_all_results()

    # Concat important fields
    filters_columns = df_dataset[['Group_id', 'Utterance_id', 'Base_paraphrase','Domain_value_generic', 'English_utterance', 'Events_cases_classification', 'Projection_classification', 
                          'Condition_classification', 'Condition_group_classification', 'Projection_aggregation',
                          'Groupby', 'IUEN', 'Subselect_condition', 'Subselect_having', 'Subselect_from', 
                          'Subselect_with']]
    filters_columns = filters_columns.reset_index(drop=True)

    columns_result_shot0 = ['id_opr_gpt35', 'hardness_opr_gpt35', 'gold_opr_gpt35', 'predicted_opr_gpt35',
                            'score_opr_gpt35','predicted_opr_gemini10', 'score_opr_gemini10', 
                            'predicted_opr_llama3', 'score_opr_llama3', 'predicted_cr_gpt35', 'score_cr_gpt35', 
                            'predicted_cr_gemini10', 'score_cr_gemini10', 'predicted_cr_llama3', 'score_cr_llama3']
    columns_result_shot1 =  ['id_opr_gpt35_shot1', 'hardness_opr_gpt35_shot1', 'gold_opr_gpt35_shot1', 'predicted_opr_gpt35_shot1','score_opr_gpt35_shot1','predicted_opr_gemini10_shot1',
                            'score_opr_gemini10_shot1', 'predicted_opr_llama3_shot1', 'score_opr_llama3_shot1', 'predicted_cr_gpt35_shot1', 'score_cr_gpt35_shot1',
                            'predicted_cr_gemini10_shot1', 'score_cr_gemini10_shot1', 'predicted_cr_llama3_shot1', 
                            'score_cr_llama3_shot1']

    shot0_results = pd.concat([filters_columns, shot0_df[columns_result_shot0]], axis=1)
    shot1_results = pd.concat([filters_columns, shot1_df[columns_result_shot1]], axis=1)

    execution = ExecutionEasy()
    execution.execute(shot0_results, shot1_results, file, metric_label)
