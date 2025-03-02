import pandas as pd
from loader_results import LoaderResults
from execution_by_model import ExecutionEasy, ExecutionMedium, ExecutionHard, ExecutionExtra, ExecutionNoHardness

def get_models_to_load(lang, metric):
    models_to_load_gpt35 = {
        'cr_gpt35': {'lang': lang, 'representation': 'code_shot0', 'metric': metric},
        'cr_gpt35_shot1': {'lang': lang, 'representation': 'code_shot1', 'metric': metric},
        'cr_gpt35_shot3': {'lang': lang, 'representation': 'code_shot3', 'metric': metric},
        'cr_gpt35_shot5': {'lang': lang, 'representation': 'code_shot5', 'metric': metric}
    }

    models_to_load_gemini10 = {
        'cr_gemini10': {'lang': lang, 'representation': 'code_shot0', 'metric': metric},
        'cr_gemini10_shot1': {'lang': lang, 'representation': 'code_shot1', 'metric': metric},
        'cr_gemini10_shot3': {'lang': lang, 'representation': 'code_shot3', 'metric': metric},
        'cr_gemini10_shot5': {'lang': lang, 'representation': 'code_shot5', 'metric': metric}
    }

    models_to_load_llama3 = {
        'opr_llama3_shot1': {'lang': lang, 'representation': 'openai_shot1', 'metric': metric},
        'cr_llama3': {'lang': lang, 'representation': 'code_shot0', 'metric': metric},
        'cr_llama3_shot1': {'lang': lang, 'representation': 'code_shot1', 'metric': metric},
        'cr_llama3_shot3': {'lang': lang, 'representation': 'code_shot3', 'metric': metric},
        'cr_llama3_shot5': {'lang': lang, 'representation': 'code_shot5', 'metric': metric}
    }

    return models_to_load_gpt35, models_to_load_gemini10, models_to_load_llama3

def get_execution(sql_complexity: str):
    if sql_complexity == "easy":
        execution = ExecutionEasy()
    elif sql_complexity == "medium":
        execution = ExecutionMedium()
    elif sql_complexity == "hard":
        execution = ExecutionHard()
    elif sql_complexity == "extra":
        execution = ExecutionExtra()
    elif sql_complexity == "no_hardness":
        execution = ExecutionNoHardness()
    
    return execution

def execute(sql_complexity, file):
    path_ds = '../dataset/text2sql4pm.tsv'
    df_dataset = pd.read_csv(path_ds, sep='\t')
    df_dataset.dropna(how='all', inplace=True)
    
    models_to_load_gpt35_en_em, models_to_load_gemini10, models_to_load_llama3 = get_models_to_load('EN', 'EM')
    models_to_load_gpt35_en_ex, models_to_load_gemini10, models_to_load_llama3 = get_models_to_load('EN', 'EX')
    models_to_load_gpt35_pt_em, models_to_load_gemini10, models_to_load_llama3 = get_models_to_load('PT', 'EM')
    models_to_load_gpt35_pt_ex, models_to_load_gemini10, models_to_load_llama3 = get_models_to_load('PT', 'EX')
    
    results_gpt35_en_em = LoaderResults()
    results_gpt35_en_em.load_results(models_to_load_gpt35_en_em)
    gpt35_df_en_em = results_gpt35_en_em.concat_all_results()

    results_gpt35_en_ex = LoaderResults()
    results_gpt35_en_ex.load_results(models_to_load_gpt35_en_ex)
    gpt35_df_en_ex = results_gpt35_en_ex.concat_all_results()

    results_gpt35_pt_em = LoaderResults()
    results_gpt35_pt_em.load_results(models_to_load_gpt35_pt_em)
    gpt35_df_pt_em = results_gpt35_pt_em.concat_all_results()

    results_gpt35_pt_ex = LoaderResults()
    results_gpt35_pt_ex.load_results(models_to_load_gpt35_pt_ex)
    gpt35_df_pt_ex = results_gpt35_pt_ex.concat_all_results()

    #results_gemini10 = LoaderResults()
    #results_gemini10.load_results(models_to_load_gemini10)
    #gemini10_df = results_gemini10.concat_all_results()
#
    #results_llama3 = LoaderResults()
    #results_llama3.load_results(models_to_load_llama3)
    #llama3_df = results_llama3.concat_all_results()

    # Concat important fields
    filters_columns = df_dataset[['Group_id', 'Utterance_id', 'Base_paraphrase','Domain_value_generic', 'English_utterance', 'Events_cases_classification', 'Projection_classification', 
                          'Condition_classification', 'Condition_group_classification', 'Projection_aggregation',
                          'Groupby', 'IUEN', 'Subselect_condition', 'Subselect_having', 'Subselect_from', 
                          'Subselect_with']]
    filters_columns = filters_columns.reset_index(drop=True)

    columns_result_gpt35 = ['id_cr_gpt35', 'hardness_cr_gpt35', 'gold_cr_gpt35', 
                        'predicted_cr_gpt35', 'score_cr_gpt35', 
                        'predicted_cr_gpt35_shot1', 'score_cr_gpt35_shot1',
                        'predicted_cr_gpt35_shot3', 'score_cr_gpt35_shot3',
                        'predicted_cr_gpt35_shot5', 'score_cr_gpt35_shot5']

    columns_result_gemini10 =  ['id_cr_gemini10', 'hardness_cr_gemini10','gold_cr_gemini10', 
                            'predicted_cr_gemini10', 'score_cr_gemini10',
                            'predicted_cr_gemini10_shot1', 'score_cr_gemini10_shot1',
                            'predicted_cr_gemini10_shot3', 'score_cr_gemini10_shot3',
                            'predicted_cr_gemini10_shot5', 'score_cr_gemini10_shot5']
    columns_result_llama3 =  ['id_cr_llama3', 'hardness_cr_llama3','gold_cr_llama3', 
                            'predicted_cr_llama3', 'score_cr_llama3',
                            'predicted_cr_llama3_shot1', 'score_cr_llama3_shot1']
                            #'predicted_cr_llama3_shot3', 'score_cr_llama3_shot3'
                            #'predicted_cr_llama3_shot5', 'score_cr_llama3_shot5']

    gpt35_results_en_em = pd.concat([filters_columns, gpt35_df_en_em[columns_result_gpt35]], axis=1)
    gpt35_results_en_ex = pd.concat([filters_columns, gpt35_df_en_ex[columns_result_gpt35]], axis=1)
    gpt35_results_pt_em = pd.concat([filters_columns, gpt35_df_pt_em[columns_result_gpt35]], axis=1)
    gpt35_results_pt_ex = pd.concat([filters_columns, gpt35_df_pt_ex[columns_result_gpt35]], axis=1)

    #gemini10_results = pd.concat([filters_columns, gemini10_df[columns_result_gemini10]], axis=1)
    #llama3_results = pd.concat([filters_columns, llama3_df[columns_result_llama3]], axis=1)

    models = {
        'gpt35': {
            'EM': {
                'PT': gpt35_results_pt_em,
                'EN': gpt35_results_en_em
            },
            'EX': {
                'PT': gpt35_results_pt_ex,
                'EN': gpt35_results_en_ex
            }
        }
    }

    execution = get_execution(sql_complexity)
    execution.execute(file, models)
